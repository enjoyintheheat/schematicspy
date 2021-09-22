from tree.interface import IFileEntry


class FileEntry(IFileEntry):
    def __init__(self, path: str):
        self.path = path

    def __repr__(self):
        pass
