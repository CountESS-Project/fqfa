"""Functions for working with FASTA files and FASTA records.

"""

import textwrap
import string
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


def write_fasta_record(handle: TextIO, header: str, seq: str, width: int = 60) -> None:
    """Writes a FASTA record to an open file handle.

    Leading and trailing whitespace will be removed from the header and all whitespace will be removed from the
    sequence before generating output.

    Parameters
    ----------
    handle : TextIO
        Open text file handle to write to.
    header : str
        Header string for the FASTA record, without the leading '>'
    seq : str
        Sequence for the FASTA record.
    width : int
        Width to use when hard-wrapping the sequence. Default 60.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the header is empty.
    ValueError
        If the sequence is empty.

    """
    header = header.strip()
    seq = seq.translate(str.maketrans("", "", string.whitespace))

    if len(header) == 0:
        raise ValueError("empty FASTA header")
    if len(seq) == 0:
        raise ValueError("empty FASTA sequence")

    print(f">{header}\n{textwrap.fill(seq, width=width)}", file=handle)
