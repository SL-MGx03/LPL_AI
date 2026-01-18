import glob
import os

def get_all_json_files(folder_path):
    pattern = os.path.join(folder_path, "*.json")
    
    file_list = glob.glob(pattern)
    
    return file_list

def get_all_names(paths):
    return [os.path.basename(p).replace(".json", "") for p in paths]

my_folder = "lpldata"
json_files = get_all_json_files(my_folder)
json_id = get_all_names(json_files)
