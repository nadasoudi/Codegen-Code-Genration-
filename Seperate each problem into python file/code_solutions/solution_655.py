import multiprocessing
import os

def start_new_process(process_name):
    print("Starting new process: ", process_name)
    os.system(f"python3 {process_name}.py")

if __name__ == "__main__":
    process_name = "python3 process.py"
    p = multiprocessing.Process(target=start_new_process, args=(process_name,))
    p.start()
    p.join