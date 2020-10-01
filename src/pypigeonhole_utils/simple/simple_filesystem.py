import os
import gzip
import shutil
import glob


def unzip_file(in_file: str, out_file: str):
    with gzip.open(in_file, 'rb') as f_in, open(out_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


def zip_file(in_file: str, out_file: str):
    with open(in_file, 'rb') as f_in, gzip.open(out_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


def latest_file_in(folder: str, pattern='*'):
    files = glob.glob(folder + '/' + pattern)
    latest = max(files, key=os.path.getmtime)  # we use modify time as marker
    return latest


def latest_folder_in(folder: str, pattern='*/'):
    files = glob.glob(folder + '/' + pattern)
    latest = max(files, key=os.path.getctime)  # we use creation time as marker
    return latest
