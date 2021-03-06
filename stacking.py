import cv2
import numpy as np
import os
import argparse


parser = argparse.ArgumentParser(description='''Takes in a path to a  directory
of images and stacks them into a star trail image.''')
parser.add_argument('path',
    help='Path to a directory containing images of stars')

parser.add_argument('--name',
    help='Name of output file')

args = parser.parse_args()
path = args.path
name = args.name

if name == None:
    name = 'out.jpg'

im, prev = None, None
for file in os.listdir(path):
    if os.path.splitext(file)[1] == '.jpg':
        curr = cv2.imread(path + file)
        if im is None:
            im = curr 
        else:
            im = np.maximum(im, curr)
        
    cv2.imwrite(name, im)
