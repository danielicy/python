from time import ctime
from pathlib import Path

import shutil

path = Path("modules/ecomerce.__init__.py")
# print(path.exists())
print(path.is_dir())

print(path.name)

print("sufix: ", path.suffix)

print(path.stem)

print(path.parent)
print(path.is_dir())

path.is_file()
# print(path.name)

ecommercedir = Path(r"helloworld/modules/ecomerce")
# print(ecommercedir)

paths = [p for p in ecommercedir.iterdir() if p.is_dir()]
print("all items:", paths)

py_files = [p for p in Path().glob("*.py")]
print("all py_files:", py_files)

# recoursive:
py_files = [p for p in Path().rglob("*.py")]
print("all py_files:", py_files)


# home directory:
print(Path.home())


# files:

file = Path("helloworld/modules/ecomerce/__init__.py")
file.exists()
file.rename("init.txt")
# to delete:
file.unlink()
print(ctime(file.stat()))

file.read_bytes()
file.read_text()
file.write_text("hello world")


# to copy a file to another file
source = Path("ecomerce/__init__.py")
target = Path()/"__init_.py"
shutil.copy(source, target)
