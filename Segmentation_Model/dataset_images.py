# import the necessary packages
from skimage import io
from torch.utils.data import Dataset
from torchvision import transforms

import cv2
import numpy as np
import random
import torch
import torchvision.transforms.functional as TF


class Dataset(Dataset):
    def __init__(self, imagePaths, maskPaths):
        # store the image and mask filepaths, and augmentation transforms
        self.imagePaths = imagePaths
        self.maskPaths = maskPaths

    def __len__(self):
        # return the size of the dataset
        return len(self.imagePaths)

    def __getitem__(self, idx):
        # grab the paths from the current index
        imagePath = self.imagePaths[idx]
        maskPath = self.maskPaths[idx]
        # load the image and mask from disk
        image = io.imread(imagePath)
        mask = io.imread(maskPath)

        # apply the transformations to image and mask
        PIL = transforms.ToPILImage()
        image = PIL(image)
        mask = PIL(mask)

        # Random crop
        crop = transforms.RandomResizedCrop(128)
        i, j, h, w = crop.get_params(image, scale=(0.08, 1.0), ratio=(0.75, 1.33))
        image = TF.resized_crop(image, i, j, h, w, (128, 128), transforms.InterpolationMode.BILINEAR)
        mask = TF.resized_crop(mask, i, j, h, w, (128, 128), transforms.InterpolationMode.BILINEAR)

        # Random horizontal flipping
        if random.random() > 0.5:
            image = TF.hflip(image)
            mask = TF.hflip(mask)
      
        image = TF.to_tensor(image)
        normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])
        image = normalize(image)
        
        asarray = lambda x: torch.tensor(np.array(x), dtype=torch.long)
        mask = asarray(mask)
        
        # return a tuple of the image and its mask
        return [image, mask]
