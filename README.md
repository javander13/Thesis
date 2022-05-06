# General

This is the `/home/jantina/CoralNet` drive. Here is where all the code is stored for:

- downloading the images from CoralNet
- extracting the metadata for each downloaded source
- preprocessing the images
- creating dense labels through superpixel augmentation
- training a semantic segmentation model


## Image_Metadata

Contains `sources_metadata.ipynb` that extracts the metadata from all CoralNet sources.


## Patches

Contains `patches.ipynb` that extracts patches around each label, for every image of a source.

Contains `patch_image_classifier.ipynb` that trains an image classifier on the created patches.


## Preprocessing

Contains `masks.ipynb` that allows to show the images with their annotations, and most importantly create
a mask for each image, containing numbers from [1;255] where each number represents a label and 255 is the 0 (no label).


## Scraping

Contains `scraper.ipynb` that dowloads the images from CoralNet website for a specific source.


## Segmentation_Model

All the scripts necessary to train a semantic segmentation model and predict labels for new images.

- `config.py` contains the configuration for the model
- `dataset.py` contains the dataset class with image transformations
    - `dataset_images.py` for images
    - `dataset_tensors.py` for tensors
    - `dataset_tensors_small.py` for small set of tensors -> loads all from disk in `init`
- `model.py` contains the UNet model from scratch, not used !
- `predict.ipynb` allows to use the trained and saved model to do semantic segmentation on new images
- `tensors.ipynb` allows to build tensors for every image and save them -> speed up training loop !
- `train_images.ipynb` train a semantic segmentation model on images
- `train_tensors.ipynb` train a semantic segmentation model on tensors


## Superpixels

Contains the scripts need to generate superpixels and augmented ground truth images.

- `superpixels_setup.ipynb` allows to set up the dataset structure through command lines
- `superpixel_generation.ipynb` allows to run the superpixel generation and groundtruth augmentation piece by piece

