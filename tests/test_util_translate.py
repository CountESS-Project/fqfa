import unittest
from fqfa.util.translate import translate_dna, ncbi_genetic_code_to_dict
from fqfa.constants.translation.table import CODON_TABLE


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
    def test_parsing_default_table(self):
        transl_table = """
          AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Starts = ---M------**--*----M---------------M----------------------------
          Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
          Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
        """
        self.assertDictEqual(ncbi_genetic_code_to_dict(transl_table), CODON_TABLE)


if __name__ == "__main__":
    unittest.main()
