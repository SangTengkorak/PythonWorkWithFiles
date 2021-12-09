from datetime import datetime as dt
import os


def format_datetime(timestamp):
    utc_timestamp = dt.utcfromtimestamp(timestamp)
    formated_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formated_date


def display_entries_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            print(f"Name : {entry.name}")
            info = entry.stat()
            print("Creation Time : ", format_datetime(info.st_ctime))
            print("Last Access Time : ", format_datetime(info.st_atime))
            print("Size : ", info.st_size)


def display_directories(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                print("Directory Name : ", entry.name)


def display_files(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print("File_Name : ", entry.name)


if __name__ == "__main__":
    # display_entries_in_directory(".")
    display_directories("/home/osboxes")
    display_files("/home/osboxes")
