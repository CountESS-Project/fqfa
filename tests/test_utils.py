import unittest

from fqfa.util.util import reverse_complement, convert_rna_to_dna, translate_dna


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


class TestTranslateDna(unittest.TestCase):
    def test_single_codon(self):
        self.assertTupleEqual(("K", None), translate_dna("AAA"))

    def test_partial_codon(self):
        self.assertTupleEqual(("", "AA"), translate_dna("AA"))
        self.assertTupleEqual(("K", "AA"), translate_dna("AAAAA"))
