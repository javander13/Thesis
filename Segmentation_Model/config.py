# import the necessary packages
import os
import torch


# base path of the dataset
DATASET_PATH = os.path.join("/data/jantina/CoralNet/dataset/")


# define the path to the images and masks dataset
IMAGE_DATASET_PATH = os.path.join(DATASET_PATH, "images")
MASK_DATASET_PATH = os.path.join(DATASET_PATH, "labels")


# define the test split
VAL_SPLIT = 0.15


# determine the device to be used for training and evaluation
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


# determine if we will be pinning memory during data loading
PIN_MEMORY = True if DEVICE == "cuda" else False


# initialize learning rate, number of epochs to train for, and the batch size
NUM_EPOCHS = 40
BATCH_SIZE = 128 
INIT_LR = 10*(1e-4 * BATCH_SIZE / 256)


# define the path to the base output directory
BASE_OUTPUT = "/data/jantina/CoralNet/dataset/output/"


# define the path to the output serialized model, model training plot, 
# and testing image paths
MODEL_PATH = os.path.join(BASE_OUTPUT, "unet.pth")
PLOT_PATH = os.path.join(BASE_OUTPUT, "plot.png")
TEST_PATHS = os.path.join(BASE_OUTPUT, "test_paths.txt")


'''Needed for the tensors

# define the path to the images and masks tensors
IMAGE_TENSOR_PATH = os.path.join(DATASET_PATH, "images_tensor")
MASK_TENSOR_PATH = os.path.join(DATASET_PATH, "labels_tensor")
'''


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