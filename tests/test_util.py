import unittest

from fqfa.util.util import (
    reverse_complement,
    convert_rna_to_dna,
    convert_dna_to_rna,
    translate_dna,
)


class TestReverseComplement(unittest.TestCase):
    def test_single_nt(self):
        self.assertEqual("A", reverse_complement("T"))

    def test_multiple_nt(self):
        self.assertEqual("TTCC", reverse_complement("GGAA"))
        self.assertEqual("ACGT", reverse_complement("ACGT"))

    def test_non_dna_characters(self):
        self.assertEqual("1", reverse_complement("1"))
        self.assertEqual("4321", reverse_complement("1234"))
        self.assertEqual("GT4321", reverse_complement("1234AC"))


class TestConvertRnaToDna(unittest.TestCase):
    def test_single_nt(self):
        self.assertEqual("T", convert_rna_to_dna("U"))
        self.assertEqual("A", convert_rna_to_dna("A"))

    def test_multiple_nt(self):
        self.assertEqual("ACGT", convert_rna_to_dna("ACGU"))
        self.assertEqual("AATT", convert_rna_to_dna("AAUU"))
        self.assertEqual("GGAA", convert_rna_to_dna("GGAA"))


class TestConvertDnaToRna(unittest.TestCase):
    def test_single_nt(self):
        self.assertEqual("U", convert_dna_to_rna("T"))
        self.assertEqual("A", convert_dna_to_rna("A"))

    def test_multiple_nt(self):
        self.assertEqual("ACGU", convert_dna_to_rna("ACGT"))
        self.assertEqual("AAUU", convert_dna_to_rna("AATT"))
        self.assertEqual("GGAA", convert_dna_to_rna("GGAA"))


class TestTranslateDna(unittest.TestCase):
    def test_single_codon(self):
        self.assertTupleEqual(("K", None), translate_dna("AAA"))
        self.assertTupleEqual(("*", None), translate_dna("TGA"))

    def test_multi_codon(self):
        # Note: this is the codon-optimized WW domain sequence from Fowler et al. 2010
        self.assertTupleEqual(
            ("DVPLPAGWEMAKTSSGQRYFLNHIDQTTTWQDPR", None),
            translate_dna(
                "GACGTTCCACTGCCGGCTGGTTGGGAAATGGCTAAAACTAGTTCTGGTCAGCGTTACTTCCTGAACCACATCGACCAGACCACCACGTGGCAGGACCCGCGT"
            ),
        )

    def test_partial_codon(self):
        self.assertTupleEqual(("", "AA"), translate_dna("AA"))
        self.assertTupleEqual(("K", "AA"), translate_dna("AAAAA"))
        self.assertTupleEqual(("DVPLPA", "G"), translate_dna("GACGTTCCACTGCCGGCTG"))


if __name__ == "__main__":
    unittest.main()
