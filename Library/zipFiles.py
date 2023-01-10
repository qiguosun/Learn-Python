from pathlib import Path
from zipfile import ZipFile
# to write all the files into the zip

# the following code may meet some error
# zip = ZipFile("Library\\files.zip", "w")

# for path in Path(r"Library\ecommerce").rglob("*.*"):
#     zip.write(path)
# zip.close()

# use with:
with ZipFile("Library\\files.zip", "w") as zip:
    for path in Path(r"Library\ecommerce").rglob("*.*"):
        zip.write(path)

with ZipFile(r"Library\files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("Library/ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("Library\\extract")
