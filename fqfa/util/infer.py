"""Functions for sequence type inference.

"""

from typing import Optional, List
from fqfa.validator.validator import (
    dna_bases_validator,
    dna_characters_validator,
    rna_bases_validator,
    amino_acids_validator,
    amino_acids_all_validator,
)

__all__ = ["infer_sequence_type", "infer_all_sequence_types"]


def infer_sequence_type(seq: str, report_iupac: bool = True) -> Optional[str]:
    """Infer the type of the given sequence.

    Returns the first sequence type that validates given the following priority order:
        * "dna"
        * "dna-iupac" (DNA sequence that contains ambiguity characters)
        * "rna"
        * "protein"
        * "protein-iupac" (protein sequence that contains ambiguity characters)

    Parameters
    ----------
    seq : str
        The string to infer the type of.
    report_iupac : bool
        If True, report sequence types with extended characters as "<type>-iupac";
        else report only the sequence type.

    Returns
    -------
    Optional[str]
        String containing the inferred sequence type if a type was inferred.
        None if the sequence didn't match any sequence types.

    """
    if dna_bases_validator(seq):
        return "dna"
    elif dna_characters_validator(seq):
        if report_iupac:
            return "dna-iupac"
        else:
            return "dna"
    elif rna_bases_validator(seq):
        return "rna"
    elif amino_acids_validator(seq):
        return "protein"
    elif amino_acids_all_validator(seq):
        if report_iupac:
            return "protein-iupac"
        else:
            return "protein"
    else:
        return None


def infer_all_sequence_types(
    seq: str, report_iupac: bool = True
) -> Optional[List[str]]:
    """Return all inferred types for the given sequence.

    Sequence types include:
        * "dna"
        * "dna-iupac" (DNA sequence that contains ambiguity characters)
        * "rna"
        * "protein"
        * "protein-iupac" (protein sequence that contains ambiguity characters)

    Parameters
    ----------
    seq : str
        The string to infer the type of.
    report_iupac : bool
        If True, report sequence types with extended characters as "<type>-iupac";
        else report only the sequence type.

    Returns
    -------
    Optional[List[str]]
        List of strings containing the inferred sequence types if any type was inferred.
        None if the sequence didn't match any sequence types.

    """
    valid = list()

    if dna_bases_validator(seq):
        valid.append("dna")
        if report_iupac:
            valid.append("dna-iupac")
    elif dna_characters_validator(seq):
        if report_iupac:
            valid.append("dna-iupac")
        else:
            valid.append("dna")

    if rna_bases_validator(seq):
        valid.append("rna")

    if amino_acids_validator(seq):
        valid.append("protein")
        if report_iupac:
            valid.append("protein-iupac")
    elif amino_acids_all_validator(seq):
        if report_iupac:
            valid.append("protein-iupac")
        else:
            valid.append("protein")

    if len(valid) > 0:
        return valid
    else:
        return None
