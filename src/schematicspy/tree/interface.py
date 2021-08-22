from abc import ABCMeta
from io import TextIOWrapper
from pathlib import Path


class IFileEntry(meta=ABCMeta):
    path: Path
    content: TextIOWrapper


class IDirectoryEntry(meta=ABCMeta):
    path: Path
