# import the necessary packages
from skimage import io
from torch.utils.data import Dataset

import numpy as np
import torch
import torchvision.transforms.functional as TF


class Dataset(Dataset):
    def __init__(self, imagePaths, maskPaths, transform=None):
        # store the image and mask filepaths, and augmentation transforms
        self.imagePaths = imagePaths
        self.maskPaths = maskPaths
        self.transform = transform

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
        
        # apply transformations
        if self.transform is not None:
            transformed = self.transform(image=image, mask=mask)
            image = transformed["image"]
            mask = transformed["mask"]
            
        # convert mask to long tensor
        mask = mask.type(torch.LongTensor)
            
        return image, mask
