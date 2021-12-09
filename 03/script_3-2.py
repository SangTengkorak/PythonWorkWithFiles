import os
from pathlib import Path as pt
import shutil as st


def rename_os():
    os.rename('images/monster01.png', 'images/monster_01.png')


def rename_pathlib():
    file = pt('images/monster02.png')
    file.rename('images/monster_02.png')


def move_files():
    os.mkdir('png')
    st.move('images/', 'png/')


def move_file():
    # os.mkdir('svg')
    os.chdir('png/images')
    st.move('monster03.svg', '../../svg/')


if __name__ == "__main__":
    # rename_os()
    # rename_pathlib()
    # move_files()
    move_file()
