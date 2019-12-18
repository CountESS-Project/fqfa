from fqfa.validator.create import create_validator
from fqfa.constants.iupac.dna import DNA_BASES, DNA_CHARACTERS
from fqfa.constants.iupac.rna import RNA_BASES
from fqfa.constants.iupac.protein import AA_CODES

dna_bases_validator = create_validator(DNA_BASES)
"""Callable[[str, int, int], Optional[Match[str]]]: validator for DNA bases.

Returns a match object if all characters in the string are found in :py:data:`~fqfa.constants.iupac.dna.DNA_BASES`.

"""

dna_characters_validator = create_validator(DNA_CHARACTERS)
"""Callable[[str, int, int], Optional[Match[str]]]: validator for DNA bases and ambiguity characters.

Returns a match object if all characters in the string are found in :py:data:`~fqfa.constants.iupac.dna.DNA_CHARACTERS`.

"""

rna_bases_validator = create_validator(RNA_BASES)
"""Callable[[str, int, int], Optional[Match[str]]]: validator for RNA bases.

Returns a match object if all characters in the string are found in :py:data:`~fqfa.constants.iupac.rna.RNA_BASES`.

"""

amino_acids_validator = create_validator(list(AA_CODES.keys()))
"""Callable[[str, int, int], Optional[Match[str]]]: validator for amino acids.

Returns a match object if all characters in the string are single-letter amino acid codes found in
:py:data:`~fqfa.constants.iupac.protein.AA_CODES`.

"""
