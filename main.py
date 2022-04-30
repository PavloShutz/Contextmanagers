from contextlib import contextmanager


class OpenFile:
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def __enter__(self):
        self.file = open(self.filename, "w")
        self.file.write(self.data)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


@contextmanager
def open_and_write_in_file(filename, data):
    file = open(filename, "w")
    file.write(data)
    yield
    file.close()

