import unittest

from fqfa.util.util import reverse_complement, convert_rna_to_dna


class TestReverseComplement(unittest.TestCase):
    def test_single_nt(self):
        self.assertEqual("A", reverse_complement("T"))

    def test_non_dna_character(self):
        self.assertEqual("1", reverse_complement("1"))


class TestConvertRnaToDNA(unittest.TestCase):
    def test_single_nt(self):
        self.assertEqual("T", convert_rna_to_dna("U"))
        self.assertEqual("A", convert_rna_to_dna("A"))
