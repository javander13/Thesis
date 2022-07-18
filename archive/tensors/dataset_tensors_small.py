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
        # store the image and mask filepaths 
        self.imagePaths = np.array(imagePaths)
        self.maskPaths = np.array(maskPaths)
        
        self.images = []
        self.masks = []
        for imagePath in self.imagePaths:
            self.images.append(torch.load(imagePath))
        self.images = torch.stack(self.images)

        for maskPath in self.maskPaths:
            self.masks.append(torch.load(maskPath))
        self.masks = torch.stack(self.masks)

    def __len__(self):
        # return the size of the dataset
        return len(self.images)

    def __getitem__(self, idx):       
        # grab the paths from the current index
        # and load the tensor
        image = (self.images[idx])
        mask = (self.masks[idx])

        # random crop
        crop = transforms.RandomResizedCrop(128)
        i, j, h, w = crop.get_params(image, scale=(0.08, 1.0), ratio=(0.75, 1.33))
        image = TF.resized_crop(image, i, j, h, w, (128, 128), transforms.InterpolationMode.BILINEAR)
        mask = TF.resized_crop(mask, i, j, h, w, (128, 128), transforms.InterpolationMode.BILINEAR).squeeze()
        
        # random horizontal flipping
        if random.random() > 0.5:
            image = TF.hflip(image)
            mask = TF.hflip(mask)
        
        # return a tuple of the image and its mask
        return image, mask
