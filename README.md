# RATAug
A tool made by Gavin Haynes for a Senior Design Project

## Description
Augments segmentation training data, giving a more robust dataset.

## Dependencies
python3.10, numpy, opencv, glob

## Usage
python3 augment.py input_folder scale output_folder
  
  
input_folder, output_folder: the names of your input and ouput folders
  
scale: the number of times you apply augmentation to each image, scaling the total number of images by a constant
