"""Simple utility functions for sequence manipulation.

"""

import itertools

from typing import Dict, Tuple, Optional

from fqfa.constants.iupac.dna import DNA_COMPLEMENTS
from fqfa.constants.translation.table import CODON_TABLE

_DNA_COMPLEMENTS_TRANS = str.maketrans(DNA_COMPLEMENTS)
"""Mapping[int, str]: translation table for complementing DNA bases, including IUPAC ambiguity characters.

"""

_RNA_DNA_TRANS = str.maketrans("U", "T")
"""Mapping[int, str]: translation table for converting U bases to T bases in RNA sequences.

"""

_DNA_RNA_TRANS = str.maketrans("T", "U")
"""Mapping[int, str]: translation table for converting T bases to U bases in DNA sequences.

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


def convert_dna_to_rna(seq: str) -> str:
    """
    Convert a DNA sequence into a RNA sequence by changing "T" to "U".

    Parameters
    ----------
    seq : str
        String containing DNA bases.

    Returns
    -------
    str
        The equivalent RNA sequence.

    """
    rna_seq = seq.translate(_DNA_RNA_TRANS)
    return rna_seq


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


def ncbi_genetic_code_to_dict(ncbi_string: str) -> Dict[str, str]:
    """
    Parse a translation table from NCBI in the five-line table format into a dictionary representation suitable for
    :py:func:`fqfa.util.util.translate_dna`.

    NCBI translation tables can be found
    `here <https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=cgencodes>`_.

    The default translation table is encoded by::

        AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
      Starts = ---M------**--*----M---------------M----------------------------
      Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
      Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
      Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG


    Information from the `Starts` line is not retained in the dictionary representation.

    Blank lines or whitespace-only lines are automatically skipped, as are lines beginning with `#`.

    Parameters
    ----------
    ncbi_string : str
        Multi-line string containing a `transl_table` from NCBI.

    Returns
    -------
    Dict[str, str]
        Dictionary mapping codons to single-letter amino acid codes.

    Raises
    ------
    TODO

    """
    lines = [
        s.strip()
        for s in ncbi_string.split("\n")
        if len(s) > 0 and not s.startswith("#") and not s.isspace()
    ]
    if len(lines) != 5:
        raise ValueError("transl_table string must have 5 lines")

    transl_table = dict()
    for s in lines:
        try:
            a, b = s.split("=")
        except ValueError:
            raise ValueError("transl_table line did not contain '=' separator")
        transl_table[a.strip()] = b.strip()

    if list(transl_table.keys()) != ["AAs", "Starts", "Base1", "Base2", "Base3"]:
        raise ValueError("unmatched transl_table row labels")
    if [len(s) for s in transl_table.values()] != [64] * 5:
        raise ValueError("all transl_table rows must contain 64 characters")

    codon_dict = dict()
    for aa, codon in zip(
        transl_table["AAs"],
        (
            "".join(nts)
            for nts in zip(
                transl_table["Base1"], transl_table["Base2"], transl_table["Base3"]
            )
        ),
    ):
        if codon not in codon_dict:
            codon_dict[codon] = aa
        else:
            raise ValueError("all transl_table codons must be unique")

    if sorted(codon_dict.keys()) != sorted(
        "".join(nts) for nts in itertools.product("ACGT", repeat=3)
    ):
        raise ValueError("incomplete set of codons from transl_table")

    return codon_dict