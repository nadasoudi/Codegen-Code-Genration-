def get_list_of_empty_directories(path):
    list_of_empty_directories = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.isfile(os.path.join(root, file)):
                if os.stat(os.path.join(root, file)).st_size == 0:
                    list_of_empty_directories.append(os.path.join(root, file))