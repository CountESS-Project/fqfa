import unittest
from io import StringIO
from fqfa.fasta.fasta import parse_fasta_records, write_fasta_record


class TestYieldFastaRecords(unittest.TestCase):
    def test_empty(self) -> None:
        data = StringIO("")

        iterator = parse_fasta_records(data)

        # should return an empty generator
        self.assertRaises(StopIteration, next, iterator)

    def test_noheader(self) -> None:
        data = StringIO("ACGT\n")

        iterator = parse_fasta_records(data)

        # should return an empty generator
        self.assertRaises(StopIteration, next, iterator)

    def test_single(self) -> None:
        data = StringIO(">seq1\nACGT\n")

        iterator = parse_fasta_records(data)

        self.assertTupleEqual(next(iterator), ("seq1", "ACGT"))
        self.assertRaises(StopIteration, next, iterator)

    def test_multiple(self) -> None:
        data = StringIO(">seq1\nACGT\n>seq2\nTGCA\n\n>seq3\nTTTT")

        iterator = parse_fasta_records(data)

        self.assertTupleEqual(next(iterator), ("seq1", "ACGT"))
        self.assertTupleEqual(next(iterator), ("seq2", "TGCA"))
        self.assertTupleEqual(next(iterator), ("seq3", "TTTT"))
        self.assertRaises(StopIteration, next, iterator)

    def test_multiline(self) -> None:
        data = StringIO(">seq1\nACGT\nTGCA")

        iterator = parse_fasta_records(data)

        self.assertTupleEqual(next(iterator), ("seq1", "ACGTTGCA"))
        self.assertRaises(StopIteration, next, iterator)


class TestWriteFastaRecord(unittest.TestCase):
    def test_single_line_write(self) -> None:
        outfile = StringIO()
        header = "test"
        seq = "ACGT"

        write_fasta_record(outfile, header, seq)
        outfile.seek(0)

        self.assertEqual(outfile.read(), ">test\nACGT\n")

        # test header with internal whitespace
        outfile = StringIO()
        header = "test details-some metadata"
        seq = "ACGT"

        write_fasta_record(outfile, header, seq)
        outfile.seek(0)

        self.assertEqual(outfile.read(), ">test details-some metadata\nACGT\n")

    def test_strip_seq_whitespace(self) -> None:
        outfile = StringIO()
        header = "test"
        seq = "AC\nGT"

        write_fasta_record(outfile, header, seq)
        outfile.seek(0)

        self.assertEqual(outfile.read(), ">test\nACGT\n")

    def test_strip_header_whitespace(self) -> None:
        outfile = StringIO()
        header = " test  "
        seq = "ACGT"

        write_fasta_record(outfile, header, seq)
        outfile.seek(0)

        self.assertEqual(outfile.read(), ">test\nACGT\n")

    def test_multi_line_write(self) -> None:
        outfile = StringIO()
        header = "test"
        seq = "ACGTAAAA"

        write_fasta_record(outfile, header, seq, width=4)
        outfile.seek(0)

        self.assertEqual(outfile.read(), ">test\nACGT\nAAAA\n")

        outfile = StringIO()
        header = "test"
        seq = "ACGTAA"

        write_fasta_record(outfile, header, seq, width=4)
        outfile.seek(0)

        self.assertEqual(outfile.read(), ">test\nACGT\nAA\n")

    def test_empty_header(self) -> None:
        # empty string
        outfile = StringIO()
        header = ""
        seq = "ACGT"

        self.assertRaises(ValueError, write_fasta_record, outfile, header, seq)

        # whitespace only
        outfile = StringIO()
        header = "  "
        seq = "ACGT"

        self.assertRaises(ValueError, write_fasta_record, outfile, header, seq)

    def test_empty_sequence(self) -> None:
        # empty string
        outfile = StringIO()
        header = "test"
        seq = ""

        self.assertRaises(ValueError, write_fasta_record, outfile, header, seq)

        # whitespace only
        outfile = StringIO()
        header = "test"
        seq = "  "

        self.assertRaises(ValueError, write_fasta_record, outfile, header, seq)


if __name__ == "__main__":
    unittest.main()
