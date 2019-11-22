"""Constants containing IUPAC codes for DNA sequences.

"""

from typing import List, Dict

DNA_BASES: List[str] = [
    "A",  # Adenine
    "C",  # Cytosine
    "G",  # Guanine
    "T",  # Thymine
]
"""List[str]: The four DNA bases.

.. csv-table:: 
   :header: "Symbol", "Description"
   :widths: 5, 10
   
    "A",  "Adenine"
    "C",  "Cytosine"
    "G",  "Guanine"
    "T",  "Thymine"

"""

DNA_AMBIGUITY: List[str] = [
    "W",  # Weak, AT
    "S",  # Strong, GC
    "M",  # aMino, AC
    "K",  # Keto, GT
    "R",  # puRine, AG
    "Y",  # pYrimidine, CT
    "B",  # not A, CGT
    "D",  # not C, AGT
    "H",  # not G, ACT
    "V",  # not T, ACG
    "N",  # any Nucleotide, ACGT
]
"""List[str]: IUPAC ambiguity characters for DNA sequence.

.. csv-table:: 
   :header: "Symbol", "Description", "Bases"
   :widths: 5, 10, 5
   
    "W",  "Weak", "AT"
    "S",  "Strong", "GC"
    "M",  "aMino", "AC"
    "K",  "Keto", "GT"
    "R",  "puRine", "AG"
    "Y",  "pYrimidine", "CT"
    "B",  "not A", "CGT"
    "D",  "not C", "AGT"
    "H",  "not G", "ACT"
    "V",  "not T", "ACG"
    "N",  "any Nucleotide", "ACGT"

"""

DNA_CHARACTERS: List[str] = DNA_BASES + DNA_AMBIGUITY
"""List[str]: Bases and IUPAC ambiguity characters for DNA sequence.

.. csv-table:: 
   :header: "Symbol", "Description", "Bases"
   :widths: 5, 10, 5
   
    "A",  "Adenine", "A"
    "C",  "Cytosine", "C"
    "G",  "Guanine", "G"
    "T",  "Thymine", "T"
    "W",  "Weak", "AT"
    "S",  "Strong", "GC"
    "M",  "aMino", "AC"
    "K",  "Keto", "GT"
    "R",  "puRine", "AG"
    "Y",  "pYrimidine", "CT"
    "B",  "not A", "CGT"
    "D",  "not C", "AGT"
    "H",  "not G", "ACT"
    "V",  "not T", "ACG"
    "N",  "any Nucleotide", "ACGT"

"""

DNA_COMPLEMENTS: Dict[str, str] = {
    "A": "T",
    "C": "G",
    "G": "C",
    "T": "A",
    "W": "W",
    "S": "S",
    "M": "K",
    "K": "M",
    "R": "Y",
    "Y": "R",
    "B": "V",
    "D": "H",
    "H": "D",
    "V": "B",
    "N": "N",
}
"""Dict[str, str]: Map for complementing DNA sequences.

.. csv-table:: 
   :header: "Symbol", "Complement", "Bases", "Comp. Bases"
   :widths: 5, 5, 5, 5

    "A", "T", "A", "T"
    "C", "G", "C", "G"
    "G", "C", "G", "C"
    "T", "A", "T", "A"
    "W", "W", "AT", "AT"
    "S", "S", "GC", "GC"
    "M", "K", "AC", "GT"
    "K", "M", "GT", "AC"
    "R", "Y", "AG", "CT"
    "Y", "R", "CT", "AG"
    "B", "V", "CGT", "ACG"
    "D", "H", "AGT", "ACT"
    "H", "D", "ACT", "AGT"
    "V", "B", "ACG", "CGT"
    "N", "N", "ACGT", "ACGT"

"""
