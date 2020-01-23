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


def yield_fastq_reads_pe(
    handle_fwd: TextIO, handle_rev: TextIO, revcomp: bool = False
) -> Generator[Tuple[FastqRead, FastqRead], None, None]:
    """Generator function that returns FASTQ read pairs as a tuple of objects.

    Parameters
    ----------
    handle_fwd : TextIO
        Open text file handle to parse for forward reads.

    handle_rev : TextIO
        Open text file handle to parse for reverse reads.

    revcomp : bool
        Whether to reverse-complement the reverse reads. Default False.

    Returns
    -------
    Tuple[FastqRead, FastqRead]
        Tuple of forward and reverse FastqRead objects.

    Raises
    ------
    ValueError
        If a record is incomplete.
    ValueError
        If the read header portion before the first whitespace doesn't match between read pairs.
        This usually contains the machine ID and read coordinates, and is therefore expected to match for PE data.

    """
    pass
