import re
from typing import Union, List, Callable, Match, Optional
from fqfa.constants.iupac.dna import DNA_BASES, DNA_CHARACTERS
from fqfa.constants.iupac.rna import RNA_BASES
from fqfa.constants.iupac.protein import AA_CODES


def create_validator(
    valid_characters: Union[str, List[str]], case_sensitive: bool = True
) -> Callable[[str, int, int], Optional[Match[str]]]:
    """
    Function that generates a callable, regular-expression based validator. When called on a given string, the
    validator will return a Match object if every character is one of the valid_characters, else None.

    Parameters
    ----------
    valid_characters : Union[str, List[str]]
        A string or list of single-character strings defining the set of valid characters.
    case_sensitive : bool
        False if both upper- and lower-case characters in valid_characters are valid. Default True.

    Returns
    -------
    Callable[[str, int, int], Optional[Match[str]]]
        Callable validator that uses re.fullmatch.

    """
    if isinstance(valid_characters, list):
        if not all(len(c) == 1 for c in valid_characters):
            raise ValueError("expected a list of single characters")

    if case_sensitive:
        charset = set(valid_characters)
    else:
        charset = set(c.upper() for c in valid_characters)
        charset.update(c.lower() for c in valid_characters)

    pattern_string = f"[{''.join(charset)}]+"
    return re.compile(pattern_string).fullmatch


dna_bases_validator = create_validator(DNA_BASES)
dna_characters_validator = create_validator(DNA_CHARACTERS)
rna_bases_validator = create_validator(RNA_BASES)
amino_acids_validator = create_validator(list(AA_CODES.keys()))
