import unittest

from fqfa.util.util import reverse_complement


class TestReverseComplement(unittest.TestCase):
    def test_single_nt(self):
        self.assertEqual("A", reverse_complement("T"))

    def test_non_dna_character(self):
        self.assertEqual("1", reverse_complement("1"))
