# augment.py
# Gavin Haynes
# Dataset Augmentation Tool for Senior Design Project: RAT
# Take an annotated dataset, apply augmentations, and generate a new one

# Usage: python3 augment.py aug1 thresh1 thresh2 aug2 thresh1 thresh2 ... etc
#   where aug is the name of your desired augmentation, thresh1, and thresh2 are 
#   the upper and lower thresholds, typically a small value.

# ex. python3 augment.py brightness -10 10 noise -25 25 rotation -20 20

# Game Plan:
# - Group annotations by image
# - Grab matching image
# - Apply augmentation to iamge and annotation (if rotation)
# - Copy and save to ouput

import sys
import glob
import cv2 as cv 
import numpy
import random
from pathlib import Path
from enum import Enum

augmentations = 'rotate noise brightness saturation'

currentFolder = ''
inputFolderPath = ''
outputFolderPath = ''

def main():
    argc = len(sys.argv)
    assert argc == 4, printArgs()

def augment(aug, lowerThresh, upperThresh) -> bool:
    return True

# Take a list of commands and execute the next one
def checkAug(cmds: list[str]) -> str:
    return ''

def printAugs():
    for aug in augmentations.split(' '):
        print(aug)

def printArgs():
    print('Usage: python3 augment.py (aug thresh1 thresh2)+',
          '\nAugmentations:', augmentations,
          '\nThresholds: dependent on operation.')

if __name__ == '__main__':
    main()