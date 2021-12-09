import shutil as st


def copy_file():
    st.copy('monster_01.png', '../png')


def copy_file_with_metadata():
    st.copy2('monster_02.png', '../png')


def copy_directory():
    st.copytree('images/', 'back-up-images/')


if __name__ == "__main__":
    # copy_file()
    # copy_file_with_metadata()
    copy_directory()
