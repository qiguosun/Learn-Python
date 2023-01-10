import shutil
from pathlib import Path
from time import ctime


path = Path("Library\\ecommerce\\__init__.py")
# print(path.exists())
# path.rename("init.txt")
# path.unlink()
print(path.stat())
print(ctime(path.stat().st_atime))


# print(path.read_text())
# path.write_text("..")

########################### shutil ###################
source = Path("Library\\ecommerce\\__init__.py")
target = Path("Library\\ecommerce\\shopping") / "__init__.txt"
shutil.copy(source, target)
