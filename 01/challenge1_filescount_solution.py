import os


def count_file_with_os_walk(path):
    total = 0
    for base, subdirs, files in os.walk(path):
        for file in files:
            total += 1
    return total


def count_files_with_scandir(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += 1
        else:
            total += count_files_with_scandir(entry)
    return total


if __name__ == "__main__":
    print(count_files_with_scandir('.'))
