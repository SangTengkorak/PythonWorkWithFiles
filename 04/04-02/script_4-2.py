# Read from and extract ZIP archives

import zipfile as zf


def read_zip():
    with zf.ZipFile('archive.zip', 'r') as archive:
        print(archive.namelist())


def retrieve_file_info_zip():
    with zf.ZipFile('archive.zip', 'r') as archive:
        file_info = archive.getinfo('png/monster01.png')
        print(file_info)


def read_file_zip():
    with zf.ZipFile('archive.zip', 'r') as archive:
        with archive.open('png/monster01.png') as file:
            print(file.read)
# Read certain file content of compressed files


def extract_file(archive, file_to_extract):
    with zf.ZipFile(archive, 'r') as my_archive:
        my_archive.extract(file_to_extract)


def extract_all():
    with zf.ZipFile('archive.zip', 'r') as archive:
        archive.extractall("extracted_files")


if __name__ == "__main__":
    # read_zip()
    # retrieve_file_info_zip()
    # read_file_zip()
    # extract_file('archive.zip', 'png/monster01.png')
    extract_all()
