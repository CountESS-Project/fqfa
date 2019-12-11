"""Simple utility functions for sequence manipulation.

"""

from typing import Dict, Tuple, Optional

from fqfa.constants.iupac.dna import DNA_COMPLEMENTS
from fqfa.constants.translation.table import CODON_TABLE

_DNA_COMPLEMENTS_TRANS = str.maketrans(DNA_COMPLEMENTS)
"""Mapping[int, str]: translation table for complementing DNA bases, including IUPAC ambiguity characters.

"""

_RNA_DNA_TRANS = str.maketrans("U", "T")
"""Mapping[int, str]: translation table for converting U bases to T bases in RNA sequences.

"""


def reverse_complement(seq: str) -> str:
    """
    Reverse-complement a DNA sequence string and return it.

    If a character not in fqfa.iupac.dna.DNA_CHARACTERS is encountered, it is retained.

    Parameters
    ----------
    seq : str
        String containing DNA bases.

    Returns
    -------
    str
        The reverse complement DNA sequence.

    """
    rev_seq = seq[::-1].translate(_DNA_COMPLEMENTS_TRANS)
    return rev_seq


def convert_rna_to_dna(seq: str) -> str:
    """
    Convert an RNA sequence into a DNA sequence by changing "U" to "T".

    Parameters
    ----------
    seq : str
        String containing RNA bases.

    Returns
    -------
    str
        The equivalent DNA sequence.

    """
    dna_seq = seq.translate(_RNA_DNA_TRANS)
    return dna_seq


def translate_dna(
    seq: str, table: Optional[Dict[str, str]] = None, frame: int = 0
) -> Tuple[str, Optional[str]]:
    """
    Translate a DNA sequence into the corresponding amino acid sequence.

    Parameters
    ----------
    seq : str
        String containing DNA bases to translate.
    table : Optional(Dict[str, str])
        Map from codon strings to single-letter amino acid codes or `None` to use the default translation table.
    frame : int
        Integer with value in (0, 1, 2) defining the position in the sequence to start at.

    Returns
    -------
    Tuple[str, Optional[str]]
        Returns a Tuple where the first string consists of the single-letter amino acid codes and the second string
        contains any remaining bases in a trailing partial codon (or `None` if there was no remainder).

    Raises
    ------
    KeyError
        If a full-length codon was not present in the translation table.

    """
    if table is None:
        table = CODON_TABLE

    remainder_length = (len(seq) - frame) % 3
    if remainder_length == 0:
        remainder = None
    else:
        remainder = seq[-remainder_length:]

    aa_seq = list()
    for i in range(frame, len(seq) - remainder_length, 3):
        codon = seq[i : i + 3]
        try:
            aa_seq.append(table[codon])
        except KeyError:
            raise KeyError(f"unrecognized codon '{codon}' at nt position {i + 1}")

    return "".join(aa_seq), remainder
