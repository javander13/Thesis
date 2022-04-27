
# import the necessary packages
import os
import torch


# base path of the dataset
DATASET_PATH = os.path.join("/data/jantina/CoralNet/WAPA_RFM/")

# define the path to the images and masks dataset
IMAGE_DATASET_PATH = os.path.join(DATASET_PATH, "images")
MASK_DATASET_PATH = os.path.join(DATASET_PATH, "labels")

# define the test split
TEST_SPLIT = 0.15

# determine the device to be used for training and evaluation
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# determine if we will be pinning memory during data loading
PIN_MEMORY = True if DEVICE == "cuda" else False

# define the number of channels in the input, number of classes, and
# number of levels in the U-Net model
NUM_CHANNELS = 3
NUM_CLASSES = 133
NUM_LEVELS = 3

# initialize learning rate, number of epochs to train for, and the batch size
NUM_EPOCHS = 40
BATCH_SIZE = 64
INIT_LR = 1e-4 * BATCH_SIZE / 256

# define the input image dimensions
# Power of two
INPUT_IMAGE_WIDTH = 128
INPUT_IMAGE_HEIGHT = 128

# define the path to the base output directory
BASE_OUTPUT = "/data/jantina/CoralNet/WAPA_RFM/output/"

# define the path to the output serialized model, model training plot, and
# testing image paths
MODEL_PATH = os.path.join(BASE_OUTPUT, "unet.pth")
PLOT_PATH = os.path.join(BASE_OUTPUT, "plot.png")
TEST_PATHS = os.path.join(BASE_OUTPUT, "test_paths.txt")
