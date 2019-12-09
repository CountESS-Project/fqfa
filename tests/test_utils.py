import unittest

from fqfa.util.util import reverse_complement, convert_rna_to_dna


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


class TestConvertRnaToDNA(unittest.TestCase):
    def test_single_nt(self):
        self.assertEqual("T", convert_rna_to_dna("U"))
        self.assertEqual("A", convert_rna_to_dna("A"))
