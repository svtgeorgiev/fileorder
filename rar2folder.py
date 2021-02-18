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
month_list_vrt = 1
for (dirpath, dirnames, filenames) in walk(root):
    root_file_list.extend(filenames)
    break
print (f"list of fienames in the directory {root_file_list}")

for year_string in root_file_list:
    year_list.append(year_string[0:4])
    # take the characters from 0 to 4th and put it in list
year_list = list(dict.fromkeys(year_list))
# cheks for duplicates and remove them

print(f"list with years {year_list}")

for item in year_list:
    os.mkdir(os.path.join(fpath, item))
# creates directories based on the year list
for item in year_list:
    for element in root_file_list:
        if item == element[0:4]:
            file_source_path = pathlib.Path(f"{root}\{element}")
            file_dest_path = pathlib.Path(f"{root}\{item}\{element}")
            shutil.move(file_source_path, file_dest_path)
# checks if the name of the year directory is equal to the charachters in position from 0 to 4th and if it is move the file in the corresponding directory
for item in year_list:
    year_folder_path = pathlib.Path(f"{root}\{item}")
    print(f"the path to every year directory {year_folder_path}")
    for (dirpath, dirnames, filenames) in walk(f"{year_folder_path}"):
        # walks within yeard directories and creates a list
        year_file_list.extend(filenames)
        for month_string in year_file_list:
            month_list.append(month_string[4:6])
        month_list = list(dict.fromkeys(month_list))
        # elements of the month list are the charachters in position from 4 to 6th in the filenames
        print(f"list with month directories {month_list}")

