# hello-world
mycode(Authors: Yuhui Ma)

## Implementations
### Requirements
* python 2.7
* SimpleITK
* Pillow

### Getting Started

```sh
# Install the dependency
pip install Pillow SimpleITK
# convert the text file to the json file
python txt2json.py \
  --txt_path /path/to/your/txt \
  --num_cls ${class_count} \
  --json_path /path/to/your/json
# convert the mhd file to the png file
python mhd2png.py \
  --mhd_file /path/to/your/mhd \
  --png_dir /dir/to/save/png
```

### End
