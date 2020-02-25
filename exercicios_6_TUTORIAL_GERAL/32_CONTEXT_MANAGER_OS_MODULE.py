import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir("exercicios_6_TUTORIAL_GERAL"):
    print(os.listdir())

with change_dir("exercicios_3"):
    print(os.listdir())
