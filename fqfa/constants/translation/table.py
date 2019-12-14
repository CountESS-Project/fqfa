"""Constants defining a standard amino acid translation table.

"""

from typing import Dict

CODON_TABLE: Dict[str, str] = {
    "AAA": "K",  # Lysine
    "AAC": "N",  # Asparagine
    "AAG": "K",  # Lysine
    "AAT": "N",  # Asparagine
    "ACA": "T",  # Threonine
    "ACC": "T",  # Threonine
    "ACG": "T",  # Threonine
    "ACT": "T",  # Threonine
    "AGA": "R",  # Arginine
    "AGC": "S",  # Serine
    "AGG": "R",  # Arginine
    "AGT": "S",  # Serine
    "ATA": "I",  # Isoleucine
    "ATC": "I",  # Isoleucine
    "ATG": "M",  # Methionine
    "ATT": "I",  # Isoleucine
    "CAA": "Q",  # Glutamine
    "CAC": "H",  # Histidine
    "CAG": "Q",  # Glutamine
    "CAT": "H",  # Histidine
    "CCA": "P",  # Proline
    "CCC": "P",  # Proline
    "CCG": "P",  # Proline
    "CCT": "P",  # Proline
    "CGA": "R",  # Arginine
    "CGC": "R",  # Arginine
    "CGG": "R",  # Arginine
    "CGT": "R",  # Arginine
    "CTA": "L",  # Leucine
    "CTC": "L",  # Leucine
    "CTG": "L",  # Leucine
    "CTT": "L",  # Leucine
    "GAA": "E",  # Glutamic acid
    "GAC": "D",  # Aspartic acid
    "GAG": "E",  # Glutamic acid
    "GAT": "D",  # Aspartic acid
    "GCA": "A",  # Alanine
    "GCC": "A",  # Alanine
    "GCG": "A",  # Alanine
    "GCT": "A",  # Alanine
    "GGA": "G",  # Glycine
    "GGC": "G",  # Glycine
    "GGG": "G",  # Glycine
    "GGT": "G",  # Glycine
    "GTA": "V",  # Valine
    "GTC": "V",  # Valine
    "GTG": "V",  # Valine
    "GTT": "V",  # Valine
    "TAA": "*",  # termination codon
    "TAC": "Y",  # Tyrosine
    "TAG": "*",  # termination codon
    "TAT": "Y",  # Tyrosine
    "TCA": "S",  # Serine
    "TCC": "S",  # Serine
    "TCG": "S",  # Serine
    "TCT": "S",  # Serine
    "TGA": "*",  # termination codon
    "TGC": "C",  # Cysteine
    "TGG": "W",  # Tryptophan
    "TGT": "C",  # Cysteine
    "TTA": "L",  # Leucine
    "TTC": "F",  # Phenylalanine
    "TTG": "L",  # Leucine
    "TTT": "F",  # Phenylalanine
}
"""Dict[str, str]: Map from codons to single-letter amino acid codes according to the standard code. Sorted by codon.

.. csv-table:: 
   :header: "Codon", "Symbol", "Amino Acid"
   :widths: 5, 5, 10

   "AAA", "K", "Lysine"
   "AAC", "N", "Asparagine"
   "AAG", "K", "Lysine"
   "AAT", "N", "Asparagine"
   "ACA", "T", "Threonine"
   "ACC", "T", "Threonine"
   "ACG", "T", "Threonine"
   "ACT", "T", "Threonine"
   "AGA", "R", "Arginine"
   "AGC", "S", "Serine"
   "AGG", "R", "Arginine"
   "AGT", "S", "Serine"
   "ATA", "I", "Isoleucine"
   "ATC", "I", "Isoleucine"
   "ATG", "M", "Methionine"
   "ATT", "I", "Isoleucine"
   "CAA", "Q", "Glutamine"
   "CAC", "H", "Histidine"
   "CAG", "Q", "Glutamine"
   "CAT", "H", "Histidine"
   "CCA", "P", "Proline"
   "CCC", "P", "Proline"
   "CCG", "P", "Proline"
   "CCT", "P", "Proline"
   "CGA", "R", "Arginine"
   "CGC", "R", "Arginine"
   "CGG", "R", "Arginine"
   "CGT", "R", "Arginine"
   "CTA", "L", "Leucine"
   "CTC", "L", "Leucine"
   "CTG", "L", "Leucine"
   "CTT", "L", "Leucine"
   "GAA", "E", "Glutamic acid"
   "GAC", "D", "Aspartic acid"
   "GAG", "E", "Glutamic acid"
   "GAT", "D", "Aspartic acid"
   "GCA", "A", "Alanine"
   "GCC", "A", "Alanine"
   "GCG", "A", "Alanine"
   "GCT", "A", "Alanine"
   "GGA", "G", "Glycine"
   "GGC", "G", "Glycine"
   "GGG", "G", "Glycine"
   "GGT", "G", "Glycine"
   "GTA", "V", "Valine"
   "GTC", "V", "Valine"
   "GTG", "V", "Valine"
   "GTT", "V", "Valine"
   "TAA", "\*", "termination codon"
   "TAC", "Y", "Tyrosine"
   "TAG", "\*", "termination codon"
   "TAT", "Y", "Tyrosine"
   "TCA", "S", "Serine"
   "TCC", "S", "Serine"
   "TCG", "S", "Serine"
   "TCT", "S", "Serine"
   "TGA", "\*", "termination codon"
   "TGC", "C", "Cysteine"
   "TGG", "W", "Tryptophan"
   "TGT", "C", "Cysteine"
   "TTA", "L", "Leucine"
   "TTC", "F", "Phenylalanine"
   "TTG", "L", "Leucine"
   "TTT", "F", "Phenylalanine"

"""
