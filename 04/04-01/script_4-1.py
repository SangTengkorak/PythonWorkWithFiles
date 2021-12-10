# Create .zip files using Python3

import zipfile as zf
import shutil as st


def create_zip(files):
    with zf.ZipFile('archive.zip', 'w') as archive:
        for file in files:
            archive.write(file)


def append_zip(files):
    with zf.ZipFile('archive.zip', 'a') as archive:
        for file in files:
            archive.write(file)


def create_zip_nested_dir(directory_path):
    st.make_archive('directory_path', 'zip', directory_path)


if __name__ == "__main__":
    # files = ["png/monster01.png", "png/monster02.png", "png/monster03.png"]
    # create_zip(files)
    create_zip_nested_dir("svg")
