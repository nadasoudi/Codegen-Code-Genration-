import os

def skip_dir(dir_name):
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            if file.endswith(".py"):
                os.remove(os.path.join(root, file))

skip_dir("C:\\Users\\srin\\OneDrive\\Desktop\\Python\\Python_Projects\\Python_Projects\\Python_Projects\\Python_Projects\\Python_Projects