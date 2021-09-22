from __future__ import annotations
from abc import ABCMeta
from io import TextIOWrapper
from pathlib import Path
from typing import List, Union


class IFileEntry(meta=ABCMeta):
    path: Path
    content: TextIOWrapper


class IDirectoryEntry(meta=ABCMeta):
    path: Path
    struct: Union[List[IDirectoryEntry], List[IFileEntry]]

    def visit(
        directory: IDirectoryEntry,
    ) -> Union[List[IDirectoryEntry], List[IFileEntry]]:
        """
        Iterate over directories
        """
