# -*- coding: utf-8 -*-

import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("--txt_path", required=True, help="path to the txt file.")
parser.add_argument("--num_cls",  type=int, help="number of classes (except background).")
parser.add_argument("--json_path", required=True, help="path to the json file.")
a = parser.parse_args()

def get_data(filename): # get data info
	ImgPath_List = []
	Images_List = []
	Annotations_List = []
	Segmentation_List = [[360,24,360,78,383,78,383,24]]
	Area = 1242
	Iscrowd = 0
	Ignore = 0
	Id = 0
	
	# open the LabelRes.txt
	with open(filename, "r", encoding="utf-8") as lines:
		print("file has been open.")
		for line in lines:
			Sample_String = line.strip()
			if Sample_String != '':
				Id += 1
				Sample_List = Sample_String.split()
				if os.path.exists(Sample_List[0]):
					if Sample_List[0] not in ImgPath_List:
						ImgPath_List.append(Sample_List[0])
						img = Image.open(Sample_List[0])
						Images_List.append({"file_name":Sample_List[0],"height":img.shape[0],"width":img.shape[1],"id":ImgPath_List.index(Sample_List[0]) + 1})
					x1 = Sample_List[2]
					y1 = Sample_List[3]
					w = Sample_List[4] - Sample_List[2]
					h = Sample_List[5] - Sample_List[3]
					Annotations_List.append({"segmentation":Segmentation_List,"area":Area,"iscrowd":Iscrowd,"image_id":ImgPath_List.index(Sample_List[0]) + 1,"category_id":Sample_List[1],"bbox":[x1,y1,w,h],"id":Id,"ignore":Ignore})
	print("Reading finished.")
	return Images_List, Annotations_List

Images_List, Annotations_List = get_data(a.txt_path)
Categories_List = []
for idx_cls in range(a.num_cls): # get labels info
	Categories_List.append({"supercategory":"none","id":idx_cls + 1,"name":idx_cls + 1})

# get whole info
JSON_Dict = {}
JSON_Dict["images"] = Images_List
JSON_Dict["type"] = "instances"
JSON_Dict["annotations"] = Annotations_List
JSON_Dict["categories"] = Categories_List

with open(a.json_path, 'w', encoding='utf-8') as output: # write the json file
	print(JSON_Dict, file = output)
output.close() # close the json file
