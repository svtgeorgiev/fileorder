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
print (f"lista s failovete w osnownata direktoria {root_file_list}")

for year_string in root_file_list:
    year_list.append(year_string[0:4])
year_list = list(dict.fromkeys(year_list))

print(f"lista s poddirektorii-godini {year_list}")

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
    print(f"putia do vsiaka poddirektoria-godina {year_folder_path}")
    for (dirpath, dirnames, filenames) in walk(f"{year_folder_path}"):
        year_file_list.extend(filenames)
        for month_string in year_file_list:
            month_list.append(month_string[4:6])
        month_list = list(dict.fromkeys(month_list))
        print(f"list s imenata na mesechnite direktorii {month_list}")


# month_list.append(year_files[4:6])
# month_list = list(dict.fromkeys(year_files))
# print(f"direktorii po meseci {month_list}")

# for files in walk(f"{year_root}\{files}"):

# print(f"direktorii po meseci {month_dir}")

# for month in month_dir:
# month_root = pathlib.Path(f"{year_root}\{month}")
# print(month_root)


# month_list = []
# for item in year_list:
# for filenames in walk(f"{root}\{item}"):
# file_list.extend(filenames)
# for element in file_list:
# month_dir_list.append(element[4:6])
# break

# month_dir_list = list(dict.fromkeys(month_dir_list))
# month_list = ["January" if element == "01" else "February" if element == "02" else "March" if element == "03" else "April" if element == "04" else "May" if element == "05" else "June" if element == "06" else "July" if element == "07" else "August" if element == "08" else "September" if element == "09" else "October" if element == "10" else "November" if element == "11" else "December" if element == "12" else element for element in month_dir_list]
# for month in month_list:
# month_path = pathlib.Path(f"{root}\{item}")
# os.mkdir(os.path.join(month_path,month))


# year_list = list(dict(from keys(year_list)))
# for element in file_list:
# new_dir_list.append(element[4:6])
# new_dir_list = list(dict.fromkeys(new_dir_list))
# month_list = ["January" if element == "01" else "February" if element == "02" else
# "March" if element == "03" else "April" if element == "04" else "May" if element == "05" else
# "June" if element == "06" else "July" if element == "07" else
# "August" if element == "08" else "September" if element == "09" else
# "October" if element == "10" else "November" if element == "11" else
# "December" if element == "12" else element for element in new_dir_list]

# for item in month_list:
# os.mkdir(os.path.join(fpath, item))
