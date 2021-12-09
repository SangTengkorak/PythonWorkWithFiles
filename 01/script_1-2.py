import os


def display_cwd():
    cwd = os.getcwd()
    print(f"Current Working Directory is : {cwd}")


def up_one_dirlevel():
    os.chdir("../")


def display_entries_in_directory(directory):
    # os.listdir()
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name)


if __name__ == "__main__":
    display_cwd()
    up_one_dirlevel()
    display_cwd()
    display_entries_in_directory("/home/osboxes")
