from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file("sample.txt", "w") as f:
    f.write("Just testing some contexts managers files.")

print(f.closed)
