import os
import shutil

path = "./files"

for file in os.listdir(path):
    filename, extension = os.path.splitext(file)

    extension = extension[1:]

    if extension == "":
        continue

    folder_path = os.path.join(path, extension)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(os.path.join(path, file), os.path.join(folder_path, file))
