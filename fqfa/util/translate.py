"""Simple utility functions for translating DNA sequences.

"""

from typing import Dict, Tuple, Optional
from fqfa.constants.translation.table import CODON_TABLE
from fqfa.validator.validator import dna_bases_validator, amino_acids_validator


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
    """Parse a translation table from NCBI into a dictionary.

    The five-line table input is parsed into a dictionary representation suitable for
    :py:func:`~fqfa.util.util.translate_dna`.
    As an example, the standard genetic code (transl_table=1) is defined in
    :py:data:`~fqfa.constants.translation.table.CODON_TABLE`.

    NCBI translation tables can be found
    `here <https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=cgencodes>`_.

    The standard genetic code is encoded by::

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
    ValueError
        If any of the rows is missing.
    ValueError
        If the row labels do not match the expected format.
    ValueError
        If any row does not have the expected format (``<label> = <data>``).
    ValueError
        If any of the rows fails to contain the expected number of characters (64).
    ValueError
        If there are duplicate codons in the table.
    ValueError
        If any of the BaseN rows contains a character other than ACGT.
    ValueError
        If the AAs row contains a character other than an amino acid.

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

    if not all(
        dna_bases_validator(bases)
        for bases in (
            transl_table["Base1"],
            transl_table["Base2"],
            transl_table["Base3"],
        )
    ):
        raise ValueError("transl_table row contains non-DNA base characters")
    if not amino_acids_validator(transl_table["AAs"]):
        raise ValueError("transl_table row contains non-amino acid characters")

    codon_dict: Dict[str, str] = dict()
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

    return codon_dict
