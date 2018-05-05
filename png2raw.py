# -*- coding: utf-8 -*-

import os
import argparse
import numpy as np
import PIL.Image as Image

parser = argparse.ArgumentParser()
parser.add_argument("--input_dir", help="path to folder containing images")
parser.add_argument("--bit_depth", default="uint16", choices=["uint16", "uint8"], help="bit depth of the saving raw file")
parser.add_argument("--output", required=True, help="path to the output file")
a = parser.parse_args()

# get all png files
png_list = os.listdir(a.input_dir)
for index in range(len(png_list)):
    path = os.path.join(a.input_dir, str(index + 1) + ".png")
    if os.path.isfile(path):
        img = Image.open(path).convert('L')
        img_array = np.array(img)
        if a.bit_depth == 'uint16':
            img_array = img_array/255.0*65535
            img_array = img_array.astype(np.uint16)
        if index == 0:
            raw_array = np.zeros((len(png_list),img_array.shape[0],img_array.shape[1])).astype(img_array.dtype)
        raw_array[index,:,:] = img_array

# write the raw data
file_object = open(a.output,'wb')
file_object.write(raw_array.reshape((1,-1)))
file_object.close()
