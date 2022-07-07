# import the necessary packages
import os
import torch


# base path of the dataset
DATASET_PATH = os.path.join("/data/jantina/CoralNet/dataset/")


# define the path to the images and labels
IMAGE_DATASET_PATH = os.path.join(DATASET_PATH, "images")
LABEL_DATASET_PATH = os.path.join(DATASET_PATH, "labels")
LABEL_DENSE_DATASET_PATH = os.path.join(DATASET_PATH, "labels_dense")
MASK_DATASET_PATH = os.path.join(DATASET_PATH, "masks")


# determine the device to be used for training and evaluation
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


# determine if we will be pinning memory during data loading
PIN_MEMORY = True if DEVICE == "cuda" else False


# initialize learning rate, number of epochs to train for, and the batch size
NUM_EPOCHS = 100
BATCH_SIZE = 700 
INIT_LR = 10*(1e-4 * BATCH_SIZE / 10)


# define the path to the base output directory
BASE_OUTPUT = "/data/jantina/CoralNet/dataset/output/"


# define the path to the output serialized model, model training plot, 
# and testing image paths
MODEL_PATH = os.path.join(BASE_OUTPUT, "unet.pth")
TEST_PATHS = os.path.join(BASE_OUTPUT, "test_paths.txt")


'''Needed for the UNet from scratch

# define the input image dimensions
# Power of two
INPUT_IMAGE_WIDTH = 128
INPUT_IMAGE_HEIGHT = 128

# define the number of channels in the input, number of classes, and
# number of levels in the U-Net model
NUM_CHANNELS = 3
NUM_CLASSES = 256
NUM_LEVELS = 3
'''