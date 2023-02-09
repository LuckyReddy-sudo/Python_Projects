import pathlib

path = pathlib.Path("Ecommerce")
path1 = pathlib.Path("Emails")
print(path.absolute())
print(path.exists())
# print(path1.mkdir())
# path1.rmdir()

path2 = pathlib.Path()
for file in path2.glob("*.py"):
    print(file)