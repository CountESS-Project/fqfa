import unittest
from fqfa.util.infer import infer_sequence_type, infer_all_sequence_types


class TestInferSequenceType(unittest.TestCase):
    def test_dna(self):
        self.assertEqual(infer_sequence_type("ACG"), "dna")
        self.assertEqual(infer_sequence_type("ACGT"), "dna")
        self.assertEqual(infer_sequence_type("TTTTT"), "dna")

    def test_dna_iupac(self):
        self.assertEqual(infer_sequence_type("AWGT", report_iupac=True), "dna-iupac")
        self.assertEqual(infer_sequence_type("AWGT", report_iupac=False), "dna")

    def test_rna(self):
        self.assertEqual(infer_sequence_type("ACGU"), "rna")
        self.assertEqual(infer_sequence_type("UUUAAAA"), "rna")

    def test_protein(self):
        self.assertEqual(infer_sequence_type("LIVW"), "protein")
        self.assertEqual(infer_sequence_type("MDLSALRVEE"), "protein")

    def test_protein_iupac(self):
        self.assertEqual(
            infer_sequence_type("LIVWZ", report_iupac=True), "protein-iupac"
        )
        self.assertEqual(infer_sequence_type("LIVWZ", report_iupac=False), "protein")

    def test_lowercase(self):
        self.assertIsNone(infer_sequence_type("acgt"))

    def test_invalid(self):
        self.assertIsNone(infer_sequence_type("ACGTU"))
        self.assertIsNone(infer_sequence_type("LITVO"))
        self.assertIsNone(infer_sequence_type("AC.GT"))
        self.assertIsNone(infer_sequence_type("TTT88AG"))


class TestInferAllSequenceTypes(unittest.TestCase):
    def test_dna(self):
        self.assertListEqual(
            infer_all_sequence_types("ACG", report_iupac=True),
            ["dna", "dna-iupac", "rna", "protein", "protein-iupac"],
        )
        self.assertListEqual(
            infer_all_sequence_types("ACG", report_iupac=False),
            ["dna", "rna", "protein"],
        )
        self.assertListEqual(
            infer_all_sequence_types("ACGT", report_iupac=True),
            ["dna", "dna-iupac", "protein", "protein-iupac"],
        )
        self.assertListEqual(
            infer_all_sequence_types("ACGT", report_iupac=False), ["dna", "protein"]
        )
        self.assertListEqual(
            infer_all_sequence_types("TTTTT", report_iupac=True),
            ["dna", "dna-iupac", "protein", "protein-iupac"],
        )
        self.assertListEqual(
            infer_all_sequence_types("TTTTT", report_iupac=False), ["dna", "protein"]
        )

    def test_dna_iupac(self):
        self.assertListEqual(
            infer_all_sequence_types("AWGT", report_iupac=True),
            ["dna-iupac", "protein", "protein-iupac"],
        )
        self.assertListEqual(
            infer_all_sequence_types("AWGT", report_iupac=False), ["dna", "protein"]
        )

    def test_rna(self):
        self.assertListEqual(infer_all_sequence_types("ACGU"), ["rna"])
        self.assertListEqual(infer_all_sequence_types("UUUAAAA"), ["rna"])

    def test_protein(self):
        self.assertListEqual(
            infer_all_sequence_types("LIVW", report_iupac=True),
            ["protein", "protein-iupac"],
        )
        self.assertListEqual(
            infer_all_sequence_types("MDLSALRVEE", report_iupac=False), ["protein"]
        )

    def test_protein_iupac(self):
        self.assertListEqual(
            infer_all_sequence_types("LIVWZ", report_iupac=True), ["protein-iupac"]
        )
        self.assertListEqual(
            infer_all_sequence_types("LIVWZ", report_iupac=False), ["protein"]
        )

    def test_lowercase(self):
        self.assertIsNone(infer_all_sequence_types("acgt"))

    def test_invalid(self):
        self.assertIsNone(infer_all_sequence_types("ACGTU"))
        self.assertIsNone(infer_all_sequence_types("LITVO"))
        self.assertIsNone(infer_all_sequence_types("AC.GT"))
        self.assertIsNone(infer_all_sequence_types("TTT88AG"))


if __name__ == "__main__":
    unittest.main()
