import os

def get_data(file_name, data_dir = "Data", newline=True):
    work_dir = os.getcwd()
    f_path = os.path.join(work_dir, data_dir, file_name)
    print("Working directory: ", work_dir)
    print(f"Getting data from {f_path}", end="\n")
    
    f = open(f_path, "r")
    
    if newline:
        f = f.read().splitlines()
    return f