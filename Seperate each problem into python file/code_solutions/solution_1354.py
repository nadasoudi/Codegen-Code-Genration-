import os

def iterate_dirs_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            print(os.path.join(root, file))
        for directory in dirs:
            print(os.path.join(root, directory))

if __name__ == '__main__':
    dir_path