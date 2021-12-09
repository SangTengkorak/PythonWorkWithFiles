from pathlib import Path as pt


def print_directory_contents():
    entries = pt.cwd()

    # entris = pt.('Absolute Path')
    # entries = pt.home()

    for entry in entries.iterdir():
        print(entry.name)
        print(entry.parent)
        print(entry.parent.parent)
        print(entry.stem)
        print(entry.suffix)
        print(entry.stat())
        print()


if __name__ == "__main__":
    print_directory_contents()
