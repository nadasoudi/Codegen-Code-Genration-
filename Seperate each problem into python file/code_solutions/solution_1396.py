"""

import os

def list_home_dir():
    """
    This function returns the list of absolute path of the home directory.
    """
    home_dir = os.path.expanduser("~")
    return [os.path.join(home_dir, d) for d in os.listdir(home_dir)]

print(list_home_dir())