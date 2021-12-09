import glob


def display_pngs():
    png_files = glob.glob('*.py')
    print(png_files)


def find_first_py():
    filtered_items = glob.glob('*1-2*')
    print(filtered_items)


def find_py_in_subdirs():
    for file in glob.iglob('**/*.py', recursive=True):
        print(file)


if __name__ == "__main__":
    display_pngs()
    find_first_py()
    find_py_in_subdirs()
