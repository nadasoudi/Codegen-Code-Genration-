import os
import sys

def get_pid(process_name):
    pid = os.getpid()
    if process_name == "python":
        pid = os.getppid()
    return pid

def change_user_id(process_name, user_id):
    pid = get_pid(process_name)
    os.setpgrp(pid, user_id)

if __name__ == "__