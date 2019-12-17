import unittest
from fqfa.util.translate import translate_dna, ncbi_genetic_code_to_dict


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

    def test_bad_codon(self):
        self.assertRaises(KeyError, translate_dna, "atg")
        self.assertRaises(KeyError, translate_dna, "NGA")
        self.assertRaises(KeyError, translate_dna, "A.A")
        self.assertRaises(KeyError, translate_dna, "CT ")

    def test_partial_codon(self):
        self.assertTupleEqual(("", "AA"), translate_dna("AA"))
        self.assertTupleEqual(("K", "AA"), translate_dna("AAAAA"))
        self.assertTupleEqual(("DVPLPA", "G"), translate_dna("GACGTTCCACTGCCGGCTG"))


class TestNcbiGeneticCodeToDict(unittest.TestCase):
    @unittest.expectedFailure
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == "__main__":
    unittest.main()
