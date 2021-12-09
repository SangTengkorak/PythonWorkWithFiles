import os
from pathlib import Path as pt


def make_logs_dir():
    try:
        os.mkdir("logs/")
    except FileExistsError as ex:
        print("Log directory already exists.")


def make_output_dir():
    dir_path = pt("output/")
    dir_path.mkdir(exist_ok=True)


if __name__ == "__main__":
    make_logs_dir()
    make_output_dir()
