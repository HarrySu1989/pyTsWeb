
import os
def get_path(file):
    current_file_dir = os.path.dirname(file)
    res = f'{current_file_dir}/cache'
    if not os.path.exists(res):
        os.makedirs(res)
    return res