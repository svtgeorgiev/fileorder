import os
from os import walk
import pathlib
import shutil

root = r'C:\Users\zare\Desktop\work\rar2file'
fpath = pathlib.Path(f"{root}")
root_file_list = []
year_list = []
year_file_list = []
month_list = []
month_file_list = []
temp_dir_list = []

for (dirpath, dirnames, filenames) in walk(root):
    root_file_list.extend(filenames)
    break

for year_string in root_file_list:
    year_list.append(year_string[0:4])
year_list = list(set(year_list))

for item in year_list:
    os.mkdir(os.path.join(fpath, item))

for item in year_list:
    for element in root_file_list:
        if item == element[0:4]:
            file_source_path = pathlib.Path(f"{root}\{element}")
            file_dest_path = pathlib.Path(f"{root}\{item}\{element}")
            shutil.move(file_source_path, file_dest_path)

for item in year_list:
    year_folder_path = pathlib.Path(f"{root}\{item}")
    for (dirpath, dirnames, filenames) in walk(f"{year_folder_path}"):
        year_file_list.extend(filenames)
        for month_string in year_file_list:
            month_list.append(month_string[4:6])
        month_list = list(set(month_list))
        year_file_list.clear()
    for month in month_list:
        os.mkdir(os.path.join(f"{year_folder_path}\{month}"))
    month_list.clear()
