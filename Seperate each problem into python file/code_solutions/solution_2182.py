import multiprocessing
import os

def get_process_info(process_name):
    process_info = os.popen('ps -A -o pid,ppid,args').read()
    process_info = process_info.split('\n')
    process_info = process_info[process_info.index(process_name) + 1:]
    process_info = [x.split() for x in process_info]
    process_info = [x for x in process_info if x