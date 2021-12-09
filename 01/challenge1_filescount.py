from pathlib import Path as pt


def file_counts():
    total_files = 0
    for path in pt("/home/osboxes/Documents/Python/Lab").glob("**/*"):
        if path.is_file():
            total_files += 1
    return total_files


if __name__ == "__main__":
    file_amount = file_counts()
    print(f"Number of Files found: {file_amount}")
