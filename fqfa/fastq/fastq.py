"""Functions for reading FASTQ files into FastqRead objects.

"""

from typing import TextIO, Generator, Tuple
from itertools import zip_longest
from fqfa.fastq.fastqread import FastqRead


def parse_fastq_reads(handle: TextIO) -> Generator[FastqRead, None, None]:
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


def parse_fastq_pe_reads(
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
        If the two file handles have a different number of reads.
    ValueError
        If the read header portion before the first whitespace doesn't match between read pairs.
        This usually contains the machine ID and read coordinates, and is therefore expected to match for PE data.

    """
    fwd_generator = parse_fastq_reads(handle_fwd)
    rev_generator = parse_fastq_reads(handle_rev)

    for fwd, rev in zip_longest(fwd_generator, rev_generator, fillvalue=None):
        if None in (fwd, rev):
            raise ValueError("mismatched FASTQ file lengths")
        elif fwd.header.split()[0] != rev.header.split()[0]:
            raise ValueError("forward and reverse read headers do not match")
        else:
            if revcomp:
                rev.reverse_complement()
            yield fwd, rev
