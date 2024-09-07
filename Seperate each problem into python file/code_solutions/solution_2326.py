import os
import sys

def kill_process(process_name):
    # Open a pipe to the process
    os.system('kill'+ process_name)

if __name__ == '__main__':
    # Process name
    process_name = sys.argv[1]
    # Kill process
    kill_process(process_name)