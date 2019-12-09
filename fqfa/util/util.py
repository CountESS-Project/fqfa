"""Simple utility functions for sequence manipulation.

"""

from fqfa.iupac.dna import DNA_COMPLEMENTS


_DNA_COMPLEMENTS_TRANS = str.maketrans(DNA_COMPLEMENTS)


def reverse_complement(seq: str) -> str:
    """
    Reverse-complement a DNA sequence string and return it.

    If a character not in fqfa.iupac.dna.DNA_CHARACTERS is encountered, it is retained.

    Parameters
    ----------
    seq : str
        String containing only DNA bases.

    Returns
    -------
    str
        The reverse complement DNA sequence.

    """
    rev_seq = seq.translate(_DNA_COMPLEMENTS_TRANS)
    return rev_seq
