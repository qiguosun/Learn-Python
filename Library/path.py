from pathlib import Path
# window
Path("C:\\Program Files\\Microsoft")
Path(r"C:\Program Files\Microsoft")
path = Path(r"Library\ecommerce\__init__.py")
p = Path(".")
[x for x in p.iterdir() if x.is_dir()]
print(path.exists())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
# create a new path only different with the last name
path.with_name("file.txt")
# absolute value of the path
print(path.absolute())


############## working with directories ######################

path = Path("Library\\ecommerce")
# print(path.exists())
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# iterdir return a generator
for p in path.iterdir():
    print(p)

# list
paths = [p for p in path.iterdir()]
print(paths)
# apply filter: if you only want directories
paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("*.py")]
# to search recursively, use rglob(*.*)
recursive_files = [p for p in path.rglob("*.py")]
print("paths: ", paths)
print("files: ", py_files)
print("allFiles: ", recursive_files)
