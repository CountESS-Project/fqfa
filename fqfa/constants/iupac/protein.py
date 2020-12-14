"""Constants containing IUPAC codes for protein sequences.

"""

from typing import Dict

__all__ = ["AA_CODES", "AA_CODES_AMBIGUITY", "AA_CODES_ALL"]

AA_CODES: Dict[str, str] = {
    "A": "Ala",  # Alanine
    "R": "Arg",  # Arginine
    "N": "Asn",  # Asparagine
    "D": "Asp",  # Aspartic acid (Aspartate)
    "C": "Cys",  # Cysteine
    "Q": "Gln",  # Glutamine
    "E": "Glu",  # Glutamic acid (Glutamate)
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
   :widths: 5, 5, 20

    "A", "Ala", "Alanine"
    "R", "Arg", "Arginine"
    "N", "Asn", "Asparagine"
    "D", "Asp", "Aspartic acid (Aspartate)"
    "C", "Cys", "Cysteine"
    "Q", "Gln", "Glutamine"
    "E", "Glu", "Glutamic acid (Glutamate)"
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

AA_CODES_AMBIGUITY: Dict[str, str] = {
    "B": "Asx",  # Aspartic acid or Asparagine
    "Z": "Glx",  # Glutamine or Glutamic acid
    "X": "Xaa",  # Any amino acid
}
"""Dict[str, str]: Map from ambiguous single-letter amino acid codes to three-letter codes. Sorted by three-letter code.

.. csv-table:: 
   :header: "Single-letter", "Three-letter", "Amino Acid"
   :widths: 5, 5, 20

    "B", "Asx", "Aspartic acid or Asparagine"
    "Z", "Glx", "Glutamine or Glutamic acid"
    "X", "Xaa", "Any amino acid"

"""

AA_CODES_ALL: Dict[str, str] = {**AA_CODES, **AA_CODES_AMBIGUITY}
"""Dict[str, str]: Map from all single-letter amino acid codes to three-letter codes. Sorted by three-letter code.

.. csv-table:: 
   :header: "Single-letter", "Three-letter", "Amino Acid"
   :widths: 5, 5, 20

    "A", "Ala", "Alanine"
    "R", "Arg", "Arginine"
    "N", "Asn", "Asparagine"
    "D", "Asp", "Aspartic acid (Aspartate)"
    "C", "Cys", "Cysteine"
    "Q", "Gln", "Glutamine"
    "E", "Glu", "Glutamic acid (Glutamate)"
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
    "B", "Asx", "Aspartic acid or Asparagine"
    "Z", "Glx", "Glutamine or Glutamic acid"
    "X", "Xaa", "Any amino acid"

"""
