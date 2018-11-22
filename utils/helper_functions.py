from os import listdir
from os.path import isfile, join, isdir

def get_all_files(path):
    """
    List all files in target folder given by path
    """
    check_if_directory_exists(path)

    all_files_list = [f for f in listdir(path) if isfile(join(path, f))]
    return all_files_list

def write_to_file(file_path, data):
    """
    Write data to the file given by file_path
    """

    target_file = open(file_path, "w")
    target_file.write(data)
    target_file.close()

def check_if_directory_exists(path):
    """
    Checks if the file on the given path is directory, If it's
    not it displays a proper message and exits the program.
    """

    if not isdir(path):
        print("Sites directory not found please make one in the same folder where is your main.py")
        print("Aborting...")
        exit()

def check_if_file_exists(path):
    """
    Checks if the file on the given path is regular file, If it's
    not it displays a proper message and exits the program.
    """

    if not isfile(path):
        print("urls file not found, please make one in the same folder where is your main.py")
        print("Aborting...")
        exit()