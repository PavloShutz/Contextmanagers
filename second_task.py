import os
from contextlib import contextmanager, suppress


class WhitespacesError(Exception):
    def __init__(self, filename, message="used whitespaces in file: "):
        self.filename = filename
        self.message = message
    
    def __str__(self):
        return f"{self.message} {self.filename}"


class OpenWriteFiles:
    """A small contextmanager to open folder and create 
    some files there.
    """
    def __init__(self, folder_name, *files):
        self.folder_name = folder_name
        self.files = list(files)

    def __enter__(self):
        # entering and trying to create files in folder
        with suppress(FileExistsError):
            os.mkdir(self.folder_name)
        os.chdir(self.folder_name)
        for file in self.files:
            if len(file.split()) > 1:
                raise WhitespacesError(file)
            open(file, "w").close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exiting from our folder
        pass


@contextmanager
def open_write_files(folder_name, *files):
    """Another context manager"""
    with suppress(FileExistsError):
        os.mkdir(folder_name)
    os.chdir(folder_name)
    for file in list(files):
        open(file, "w").close()
    yield
