"""Utility functions for file handling.

"""

from typing import TextIO


_COMPRESSION_EXTENSIONS = [".bz2", ".gz"]
"""List[str]: list of recognized compression extensions.

"""


def open_compressed(path: str) -> TextIO:
    """
    Open the file handle for reading using the correct (optional) decompression method.
    Compression status is determined by the file extension.
    Recognized file extensions are ``.bz2`` for bzip2 compression and ``.gz`` for gzip compression.
    The file is opened in text mode.

    Parameters
    ----------
    path : str
        File path to be opened.

    Returns
    -------
    TextIO
        Open file handle.

    """
    pass


def has_fastq_ext(path: str) -> bool:
    """
    Checks whether the file has the expected file extension for FASTQ format.
    Recognized file extensions are ``.fq`` and ``.fastq`` optionally in combination with a compression file extension
    supported by :py:func:`~fqfq.util.file.open_compressed`.

    Parameters
    ----------
    path : str
        File path to be checked.

    Returns
    -------
    bool
        True if the file has a recognized extension, else False.

    Raises
    ------
    FileNotFoundError
        If path does not correspond to a file.

    """
    pass


def has_fasta_ext(path: str) -> bool:
    """
    Checks whether the file has the expected file extension for FASTA format.
    Recognized file extensions are ``.fa`` and ``.fasta`` optionally in combination with a compression file extension
    supported by :py:func:`~fqfq.util.file.open_compressed`.

    Parameters
    ----------
    path : str
        File path to be checked.

    Returns
    -------
    bool
        True if the file has a recognized extension, else False.

    Raises
    ------
    FileNotFoundError
        If path does not correspond to a file.

    """
    pass
