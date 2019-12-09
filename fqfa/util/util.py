"""Simple utility functions for sequence manipulation.

"""

from fqfa.iupac.dna import DNA_COMPLEMENTS


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
