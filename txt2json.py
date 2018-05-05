# -*- coding: utf-8 -*-

import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser() # 创建命令行参数解析对象
parser.add_argument("--txt_path", required=True, help="path to the txt file.") # txt文件所在路径
parser.add_argument("--num_cls",  type=int, help="number of classes (except background).") # 类别数目
parser.add_argument("--json_path", required=True, help="path to the json file.") # json文件保存路径
a = parser.parse_args() # 解析命令行参数

def get_data(filename): # 得到图片信息和标注信息列表
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
			Sample_String = line.strip() # 去除字符串首尾空格
			if Sample_String != '': # 去除txt文件空行
				Id += 1
				Sample_List = Sample_String.split()
				if os.path.exists(Sample_List[0]): # 判断图片是否存在
					if Sample_List[0] not in ImgPath_List: # 写图片信息列表
						ImgPath_List.append(Sample_List[0])
						img = Image.open(Sample_List[0]) # 打开图片
						Images_List.append({"file_name":Sample_List[0],"height":img.shape[0],"width":img.shape[1],"id":ImgPath_List.index(Sample_List[0]) + 1})
					x1 = Sample_List[2]
					y1 = Sample_List[3]
					w = Sample_List[4] - Sample_List[2]
					h = Sample_List[5] - Sample_List[3]
					Annotations_List.append({"segmentation":Segmentation_List,"area":Area,"iscrowd":Iscrowd,"image_id":ImgPath_List.index(Sample_List[0]) + 1,"category_id":Sample_List[1],"bbox":[x1,y1,w,h],"id":Id,"ignore":Ignore}) # 写标注信息列表
	print("reading finished.")
	return Images_List, Annotations_List

Images_List, Annotations_List = get_data(a.txt_path) # 得到图片信息和标注信息列表
Categories_List = []
for idx_cls in range(a.num_cls): # 得到类别信息列表
	Categories_List.append({"supercategory":"none","id":idx_cls + 1,"name":idx_cls + 1})

# 得到数据集完整信息
JSON_Dict = {}
JSON_Dict["images"] = Images_List
JSON_Dict["type"] = "instances"
JSON_Dict["annotations"] = Annotations_List
JSON_Dict["categories"] = Categories_List

with open(a.json_path, 'w', encoding='utf-8') as output: # 以覆盖写方式打开json文件
	print(JSON_Dict, file = output) # 写json文件
output.close() # 关闭json文件
