# import the necessary packages
import os
import torch


# base path of the dataset
DATASET_PATH = os.path.join("/data/jantina/data/CoralNet/dataset/")


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
INIT_LR = 1e-4 * BATCH_SIZE


# define the path to the base output directory
BASE_OUTPUT = "/data/jantina/data/CoralNet/dataset/output/"


# define the path to the output serialized model, model training plot, 
# and testing image paths
MODEL_PATH = os.path.join(BASE_OUTPUT, "unet.pth")
TEST_PATHS = os.path.join(BASE_OUTPUT, "test_paths.txt")