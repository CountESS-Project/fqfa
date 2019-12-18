"""Constants containing IUPAC codes for protein sequences.

"""

from typing import Dict

AA_CODES: Dict[str, str] = {
    "A": "Ala",  # Alanine
    "R": "Arg",  # Arginine
    "N": "Asn",  # Asparagine
    "D": "Asp",  # Aspartic acid
    "C": "Cys",  # Cysteine
    "Q": "Gln",  # Glutamine
    "E": "Glu",  # Glutamic acid
    "G": "Gly",  # Glycine
    "H": "His",  # Histidine
    "I": "Ile",  # Isoleucine
    "L": "Leu",  # Leucine
    "K": "Lys",  # Lysine
    "M": "Met",  # Methionine
    "F": "Phe",  # Phenylalanine
    "P": "Pro",  # Proline
    "S": "Ser",  # Serine
    "T": "Thr",  # Threonine
    "W": "Trp",  # Tryptophan
    "Y": "Tyr",  # Tyrosine
    "V": "Val",  # Valine
    "*": "Ter",  # termination codon
}
"""Dict[str, str]: Map from single-letter amino acid codes to three-letter codes. Sorted by three-letter code.

.. csv-table:: 
   :header: "Single-letter", "Three-letter", "Amino Acid"
   :widths: 5, 5, 10

    "A", "Ala", "Alanine"
    "R", "Arg", "Arginine"
    "N", "Asn", "Asparagine"
    "D", "Asp", "Aspartic acid"
    "C", "Cys", "Cysteine"
    "Q", "Gln", "Glutamine"
    "E", "Glu", "Glutamic acid"
    "G", "Gly", "Glycine"
    "H", "His", "Histidine"
    "I", "Ile", "Isoleucine"
    "L", "Leu", "Leucine"
    "K", "Lys", "Lysine"
    "M", "Met", "Methionine"
    "F", "Phe", "Phenylalanine"
    "P", "Pro", "Proline"
    "S", "Ser", "Serine"
    "T", "Thr", "Threonine"
    "W", "Trp", "Tryptophan"
    "Y", "Tyr", "Tyrosine"
    "V", "Val", "Valine"
    "\*", "Ter",  "termination codon"

"""
