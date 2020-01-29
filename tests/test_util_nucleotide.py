import unittest
from fqfa.util.nucleotide import (
    reverse_complement,
    convert_rna_to_dna,
    convert_dna_to_rna,
)


class TestReverseComplement(unittest.TestCase):
    def test_single_nt(self) -> None:
        self.assertEqual("A", reverse_complement("T"))

    def test_multiple_nt(self) -> None:
        self.assertEqual("TTCC", reverse_complement("GGAA"))
        self.assertEqual("ACGT", reverse_complement("ACGT"))

    def test_non_dna_characters(self) -> None:
        self.assertEqual("1", reverse_complement("1"))
        self.assertEqual("4321", reverse_complement("1234"))
        self.assertEqual("GT4321", reverse_complement("1234AC"))


class TestConvertRnaToDna(unittest.TestCase):
    def test_single_nt(self) -> None:
        self.assertEqual("T", convert_rna_to_dna("U"))
        self.assertEqual("A", convert_rna_to_dna("A"))

    def test_multiple_nt(self) -> None:
        self.assertEqual("ACGT", convert_rna_to_dna("ACGU"))
        self.assertEqual("AATT", convert_rna_to_dna("AAUU"))
        self.assertEqual("GGAA", convert_rna_to_dna("GGAA"))


class TestConvertDnaToRna(unittest.TestCase):
    def test_single_nt(self) -> None:
        self.assertEqual("U", convert_dna_to_rna("T"))
        self.assertEqual("A", convert_dna_to_rna("A"))

    def test_multiple_nt(self) -> None:
        self.assertEqual("ACGU", convert_dna_to_rna("ACGT"))
        self.assertEqual("AAUU", convert_dna_to_rna("AATT"))
        self.assertEqual("GGAA", convert_dna_to_rna("GGAA"))


if __name__ == "__main__":
    unittest.main()
