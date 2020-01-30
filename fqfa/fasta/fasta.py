"""Functions for working with FASTA files and FASTA records.

"""

from typing import TextIO, Generator, Tuple


def parse_fasta_records(handle: TextIO) -> Generator[Tuple[str, str], None, None]:
    """Generator function that returns tuples of FASTA headers and their associated sequences.

    Lines before the start of the first record are ignored.
    Any leading and trailing whitespace is removed before the sequence lines are concatenated together.
    No validation of the characters in the FASTA record is performed.

    Parameters
    ----------
    handle : TextIO
        Open text file handle to parse.

    Yields
    -------
    Tuple[str, str]
        Tuple containing the header line (with leading '>' removed) and the sequence.

    """
    header = None
    for line in handle:
        if line.startswith(">"):
            if header is not None:  # not the first record
                yield header, "".join(seq_lines)
            seq_lines = list()
            header = line[1:].rstrip()
        else:
            if header is not None:  # not the first record
                seq_lines.append(line.strip())

    if header is not None:
        yield header, "".join(seq_lines)
    else:  # no FASTA records in file
        return
