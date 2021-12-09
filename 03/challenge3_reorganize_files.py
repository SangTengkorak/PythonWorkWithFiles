from os import stat_result
from pathlib import Path as pt
from datetime import datetime as dt


def generate_creation_date(path):
    # collect file status info
    stat_result = path.stat()
    # retrieve file creation date
    creation_date = stat_result.st_ctime
    # format retrieved date
    utc_timestamp = dt.utcfromtimestamp(creation_date)
    return utc_timestamp.strftime('%Y_%m_%d_')


def organize_images(image_folder):
    # save filetypes in list
    file_types = ['.png', '.svg']
    # find all entries in destined folder using Path iterdir
    for path in pt(image_folder).iterdir():
        # filter if entry is a file and suti filetypes list
        if path.is_file and path.suffix in file_types:
            # track what function do
            print(f"Renaming file {path.stem}")
            date = generate_creation_date(path)
            # using Path to organize new filename
            new_path = pt(image_folder + date + path.stem + path.suffix)
            # rename files that suit into category with intended format
            path.rename(new_path)


if __name__ == "__main__":
    organize_images('./')
