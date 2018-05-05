# -*- coding: utf-8 -*-

import argparse
import numpy as np
import PIL.Image as Image
import SimpleITK as sitk

parser = argparse.ArgumentParser()
parser.add_argument("--mhd_file", help="path to the mhd file")
parser.add_argument("--png_dir", help="path to folder saving png files")
a = parser.parse_args()

image = sitk.ReadImage(a.mhd_file)
image_array = sitk.GetArrayFromImage(image)

if image_array.dtype == 'uint16':
    image_array = image_array/65535.0*255
    image_array = image_array.astype(np.uint8)

for index in range(image_array.shape[0]):
    img = Image.fromarray(image_array[index,:,:]).convert('L')
    img.save(a.png_dir + str(index+1) + ".png",'png')
    print a.png_dir + str(index+1) + ".png has been saved."
    
print a.mhd_file + " has been finished."
