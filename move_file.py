import os
import shutil 
source = r'C:\Users\Noona\Downloads'
destination = r'C:\Users\Noona\Desktop\PYTHON\P - 111\Document_files'


list_of_files = os.listdir(source)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)