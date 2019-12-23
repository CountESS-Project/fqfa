"""Utility functions for file handling.

"""

import os
import bz2
import gzip
from typing import Optional, IO, Any

_COMPRESSION_EXTENSIONS = [".bz2", ".gz"]
"""List[str]: list of recognized compression extensions.

"""


def open_compressed(path: str, encoding: Optional[str] = None) -> IO[Any]:
    """Open the file handle for reading using the correct (optional) decompression method.

    Compression status is determined by the file extension.
    Recognized file extensions are ``.bz2`` for bzip2 compression and ``.gz`` for gzip compression.
    If there is any other file extension (or no extension), the file is opened normally.
    The file is opened in text mode.

    Parameters
    ----------
    path : str
        File path to be opened.
    encoding : Optional[str]
        Text file encoding as described for :py:class:`io.TextIOWrapper`.

    Returns
    -------
    IO[Any]
        Open text file handle.

    Raises
    ------
    FileNotFoundError
        If path does not correspond to a file.
    NotImplementedError
        If a recognized compression extension lacks an implementation.

    """
    if not os.path.isfile(path):
        raise FileNotFoundError("could not find file to open")
    _, ext = os.path.splitext(path)
    if ext.lower() in _COMPRESSION_EXTENSIONS:
        if ext.lower() == ".bz2":
            return bz2.open(path, mode="rt", encoding=encoding)
        elif ext.lower() == ".gz":
            return gzip.open(path, mode="rt", encoding=encoding)
        else:  # pragma no cover
            raise NotImplementedError("unsupported compression type")
    else:
        return open(path, mode="rt", encoding=encoding)


def has_fastq_ext(path: str) -> bool:
    """Checks whether the file path has the expected file extension for FASTQ format.

    Recognized file extensions are ``.fq`` and ``.fastq`` optionally in combination with a compression file extension
    supported by :py:func:`~fqfa.util.file.open_compressed`.

    Parameters
    ----------
    path : str
        File path to be checked.

    Returns
    -------
    bool
        True if the file has a recognized extension, else False.

    """
    root, ext = os.path.splitext(path)
    if ext.lower() in _COMPRESSION_EXTENSIONS:
        _, ext = os.path.splitext(root)
    if ext.lower() in (".fq", ".fastq"):
        return True
    else:
        return False


def has_fasta_ext(path: str) -> bool:
    """Checks whether the file path has the expected file extension for FASTA format.

    Recognized file extensions are ``.fa`` and ``.fasta`` optionally in combination with a compression file extension
    supported by :py:func:`~fqfa.util.file.open_compressed`.

    Parameters
    ----------
    path : str
        File path to be checked.

    Returns
    -------
    bool
        True if the file has a recognized extension, else False.

    """
    root, ext = os.path.splitext(path)
    if ext.lower() in _COMPRESSION_EXTENSIONS:
        _, ext = os.path.splitext(root)
    if ext.lower() in (".fa", ".fasta"):
        return True
    else:
        return False
