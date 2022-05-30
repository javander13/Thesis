# import the necessary packages
from skimage import io
from torch.utils.data import Dataset

import numpy as np
import torch
import torchvision.transforms.functional as TF


class Dataset(Dataset):
    def __init__(self, imagePaths, labelPaths, maskPaths, transform=None):
        # store the image, label, mask filepaths, 
        # and augmentation transforms
        self.imagePaths = imagePaths
        self.labelPaths = labelPaths
        self.maskPaths = maskPaths
        self.transform = transform

    def __len__(self):
        # return the size of the dataset
        return len(self.imagePaths)

    def __getitem__(self, idx):
        # grab the paths from the current index
        imagePath = self.imagePaths[idx]
        labelPath = self.labelPaths[idx]
        maskPath = self.maskPaths[idx]
        
        # load the image, label and mask from disk
        image = io.imread(imagePath)
        label = io.imread(labelPath)
        mask = io.imread(maskPath)
            
        # apply transformations
        if self.transform is not None:
            transformed = self.transform(image=image, mask=label, mask2=mask)
            image = transformed["image"]
            label = transformed["mask"]
            mask = transformed["mask2"]
            
        # convert label and mask to long tensor
        label = label.type(torch.LongTensor)
        mask = mask.type(torch.LongTensor)
            
        return image, label, mask
