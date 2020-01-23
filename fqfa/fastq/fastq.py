"""Functions for reading FASTQ files into FastqRead objects.

"""

from typing import TextIO, Generator
from fqfa.fastq.fastqread import FastqRead


def yield_fastq_reads(handle: TextIO) -> Generator[FastqRead, None, None]:
    """Generator function that returns FASTQ reads as objects.

    Parameters
    ----------
    handle : TextIO
        Open text file handle to parse.

    Yields
    -------
    FastqRead
        FastqRead object for the read.

    Raises
    ------
    ValueError
        If a record is incomplete.

    """
    empty = False
    while not empty:
        lines = [handle.readline() for _ in range(4)]
        if all(len(x) == 0 for x in lines):
            empty = True
        elif any(len(x) == 0 for x in lines):
            raise ValueError("incomplete FASTQ record")
        else:
            lines = [x.rstrip() for x in lines]  # remove trailing newlines
            yield FastqRead(*lines)
