import os
from pathlib import Path as pt
import shutil as st


def delete_files_os():
    os.remove('screenshots/screenshot1.png')
    # os.unlink('screenshots/screenshot1.png')


def delete_file_pathlib():
    file = pt('screenshots/screenshot2.png')
    file.unlink()


def delete_directory_os():
    os.rmdir('screenshots/')


def delete_directory_pathlib():
    directory = pt("other-screenshots/")
    directory.rmdir


def delete_directory_including_subdir():
    st.rmtree('other-screenshots/')


if __name__ == "__main__":
    # delete_files_os()
    # delete_file_pathlib()
    # delete_directory_pathlib()
    # delete_directory_os()
    delete_directory_including_subdir()
