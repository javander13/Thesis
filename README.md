# General

This is the `/home/jantina/code` drive. Here is where all the code is stored for:

- downloading the images from CoralNet
- extracting the metadata for each downloaded source
- preprocessing the images
- creating dense labels through superpixel augmentation
- training a semantic segmentation model


## model

All the scripts necessary to train a semantic segmentation model and predict labels for new images.

- `config.py`: configuration for the model

- `dataset.py`: dataset class

- `utils.py`: useful functions and classes

- `train` folder: training notebooks for the different semantic segmentation model

- `predict` folder: use the trained and saved models to do predictions on the test set

- `inference` folder:  use the trained and saved models to do predictions on the Eilat set
    
    
## preprocessing

- `masks.ipynb`: shows the images with their annotations, and most importantly create
a mask for each image, containing numbers from [1;255],
where each number represents a label and 255 is the 0 (no label).

- `scraper.ipynb`: downloads the images from CoralNet website for a specific source.

- `sources_metadata.ipynb`: extracts the metadata from all downloaded CoralNet sources.

- `preprocess_mask.py`: contains the function to change the masks from 207 classes to 10

- `preprocess_mask.ipynb`: transforms all the masks for the dataset to the new classes

- `preprocess_inference.py`: contains the function to remap the Eilat segmentation masks

- `preprocess_inference.ipynb`: transforms all the masks for the Eilat dataset to the new classes

- `transformations.ipynb`: play around with different data augmentations


## superpixels

Contains the scripts need to generate superpixels and augmented ground truth images.

- `superpixels_setup.ipynb` allows to set up the dataset structure through command lines

- `superpixel_generation.ipynb` allows to run the superpixel generation and groundtruth augmentation piece by piece