import os
import shutil
import pathlib
from pathlib import Path

source_path = r"C:\Users\zare\Desktop\work\rar2file\source"
fsoruce_path = pathlib.Path(f"{source_path}")
source_files = os.listdir(fsoruce_path)

dest_path = r"C:\Users\zare\Desktop\work\rar2file\dest"
fdest_path = f"{dest_path}"

for filename in source_files:
    Path(f"{fdest_path}\{filename[0:4]}\{filename[4:6]}").mkdir(parents=True, exist_ok=True)
    shutil.move(f"{fsoruce_path}\{filename}", f"{fdest_path}\{filename[0:4]}\{filename[4:6]}\{filename}")
