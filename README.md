# file-formats-converter
Code for convert the file formats(Authors: Yuhui Ma)

## Implementations
### Requirements
* python 2.7
* numpy
* Pillow
* SimpleITK

### Getting Started

```sh
# Install the dependency
pip install numpy Pillow SimpleITK
# convert the mhd file to the png file
python mhd2png.py \
  --mhd_file /path/to/your/mhd \
  --png_dir /dir/to/save/png
# convert the png file to the raw file(bit_depth can be chosen between "uint16" and "uint8")
python png2raw.py \
  --input_dir /dir/to/your/png \
  --bit_depth [bit_depth] \
  --output /path/to/your/raw
# convert the text file to the json file
python txt2json.py \
  --txt_path /path/to/your/txt \
  --num_cls [class_count] \
  --json_path /path/to/your/json
```
