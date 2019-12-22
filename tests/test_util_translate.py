import unittest
from fqfa.util.translate import translate_dna, ncbi_genetic_code_to_dict
from fqfa.constants.translation.table import CODON_TABLE


class TestTranslateDna(unittest.TestCase):
    def test_single_codon(self) -> None:
        self.assertTupleEqual(("K", None), translate_dna("AAA"))
        self.assertTupleEqual(("*", None), translate_dna("TGA"))

    def test_multi_codon(self) -> None:
        # Note: this is the codon-optimized WW domain sequence from Fowler et al. 2010
        self.assertTupleEqual(
            ("DVPLPAGWEMAKTSSGQRYFLNHIDQTTTWQDPR", None),
            translate_dna(
                "GACGTTCCACTGCCGGCTGGTTGGGAAATGGCTAAAACTAGTTCTGGTCAGCGTTACTTCCTGAACCACATCGACCAGACCACCACGTGGCAGGACCCGCGT"
            ),
        )

    def test_bad_codon(self) -> None:
        self.assertRaises(KeyError, translate_dna, "atg")
        self.assertRaises(KeyError, translate_dna, "NGA")
        self.assertRaises(KeyError, translate_dna, "A.A")
        self.assertRaises(KeyError, translate_dna, "CT ")

    def test_partial_codon(self) -> None:
        self.assertTupleEqual(("", "AA"), translate_dna("AA"))
        self.assertTupleEqual(("K", "AA"), translate_dna("AAAAA"))
        self.assertTupleEqual(("DVPLPA", "G"), translate_dna("GACGTTCCACTGCCGGCTG"))


class TestNcbiGeneticCodeToDict(unittest.TestCase):
    def test_parsing_default_table(self) -> None:
        transl_table = """
          AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Starts = ---M------**--*----M---------------M----------------------------
          Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
          Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
        """
        self.assertDictEqual(ncbi_genetic_code_to_dict(transl_table), CODON_TABLE)

    def test_missing_line(self) -> None:
        transl_table = """
          AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
          Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
        """
        self.assertRaises(ValueError, ncbi_genetic_code_to_dict, transl_table)

    def test_missing_separator(self) -> None:
        transl_table = """
          AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Starts  ---M------**--*----M---------------M----------------------------
          Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
          Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
        """
        self.assertRaises(ValueError, ncbi_genetic_code_to_dict, transl_table)

        transl_table = """
          AAs\tFFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Starts\t---M------**--*----M---------------M----------------------------
          Base1\tTTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
          Base2\tTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base3\tTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
        """
        self.assertRaises(ValueError, ncbi_genetic_code_to_dict, transl_table)

    def test_wrong_order(self) -> None:
        transl_table = """
          AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Starts = ---M------**--*----M---------------M----------------------------
          Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
          Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
        """
        self.assertRaises(ValueError, ncbi_genetic_code_to_dict, transl_table)

    def test_wrong_length(self) -> None:
        # missing value in one row
        transl_table = """
          AAs  = FLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Starts = ---M------**--*----M---------------M----------------------------
          Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
          Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
        """
        self.assertRaises(ValueError, ncbi_genetic_code_to_dict, transl_table)

        # missing value in all rows
        transl_table = """
          AAs  = LLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Starts = --M------**--*----M---------------M----------------------------
          Base1  = TTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
          Base2  = TTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base3  = CAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
        """
        self.assertRaises(ValueError, ncbi_genetic_code_to_dict, transl_table)

        # extra value in one row
        transl_table = """
          AAs  = FFFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Starts = ---M------**--*----M---------------M----------------------------
          Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
          Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
        """
        self.assertRaises(ValueError, ncbi_genetic_code_to_dict, transl_table)

        # extra value in one row
        transl_table = """
          AAs  = FFFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Starts = ----M------**--*----M---------------M----------------------------
          Base1  = TTTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
          Base2  = TTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base3  = TTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
        """
        self.assertRaises(ValueError, ncbi_genetic_code_to_dict, transl_table)

    def test_nonunique_codons(self) -> None:
        transl_table = """
          AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Starts = ---M------**--*----M---------------M----------------------------
          Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
          Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base3  = TTAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
        """
        self.assertRaises(ValueError, ncbi_genetic_code_to_dict, transl_table)

    def test_invalid_bases(self) -> None:
        transl_table = """
          AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Starts = ---M------**--*----M---------------M----------------------------
          Base1  = WTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
          Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
        """
        self.assertRaises(ValueError, ncbi_genetic_code_to_dict, transl_table)

    def test_invalid_aas(self) -> None:
        transl_table = """
          AAs  = BFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
          Starts = ---M------**--*----M---------------M----------------------------
          Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
          Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
          Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
        """
        self.assertRaises(ValueError, ncbi_genetic_code_to_dict, transl_table)


if __name__ == "__main__":
    unittest.main()
