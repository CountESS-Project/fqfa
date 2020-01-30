import unittest
from io import StringIO
from fqfa.fastq.fastqread import FastqRead
from fqfa.fastq.fastq import parse_fastq_reads, parse_fastq_pe_reads


class TestYieldFastqReads(unittest.TestCase):
    def test_empty(self) -> None:
        data = StringIO("")

        iterator = parse_fastq_reads(data)

        # should return an empty generator
        self.assertRaises(StopIteration, next, iterator)

    def test_single(self) -> None:
        test_read = FastqRead(
            header="@TEST:123:456 AAA",
            sequence="AAGNCT",
            header2="+",
            quality_string="!~ABCD",
        )
        data = StringIO(str(test_read))

        iterator = parse_fastq_reads(data)

        self.assertEqual(next(iterator), test_read)

    def test_truncated(self) -> None:
        data = StringIO("@TEST:123:456 AAA\nAAGN")

        iterator = parse_fastq_reads(data)

        self.assertRaises(ValueError, next, iterator)


class TestYieldFastqReadsPe(unittest.TestCase):
    def test_empty(self) -> None:
        fwd_data = StringIO("")
        rev_data = StringIO("")

        iterator = parse_fastq_pe_reads(fwd_data, rev_data)

        # should return an empty generator
        self.assertRaises(StopIteration, next, iterator)

    def test_one_empty(self) -> None:
        test_fwd_read = FastqRead(
            header="@TEST:123:456 AAA",
            sequence="AAGNCT",
            header2="+",
            quality_string="!~ABCD",
        )
        fwd_data = StringIO(str(test_fwd_read))
        rev_data = StringIO("")

        iterator = parse_fastq_pe_reads(fwd_data, rev_data)

        self.assertRaises(ValueError, next, iterator)

    def test_single_pair(self) -> None:
        test_fwd_read = FastqRead(
            header="@TEST:123:456 AAA",
            sequence="AAGNCT",
            header2="+",
            quality_string="!~ABCD",
        )
        fwd_data = StringIO(str(test_fwd_read))
        test_rev_read = FastqRead(
            header="@TEST:123:456 BBB",
            sequence="ACGTAA",
            header2="+",
            quality_string="AAA!CD",
        )
        rev_data = StringIO(str(test_rev_read))

        iterator = parse_fastq_pe_reads(fwd_data, rev_data)

        self.assertTupleEqual(next(iterator), (test_fwd_read, test_rev_read))

    def test_single_pair_rc(self) -> None:
        test_fwd_read = FastqRead(
            header="@TEST:123:456 AAA",
            sequence="AAGNCT",
            header2="+",
            quality_string="!~ABCD",
        )
        fwd_data = StringIO(str(test_fwd_read))
        test_rev_read = FastqRead(
            header="@TEST:123:456 BBB",
            sequence="ACGTAA",
            header2="+",
            quality_string="AAA!CD",
        )
        rev_data = StringIO(str(test_rev_read))

        iterator = parse_fastq_pe_reads(fwd_data, rev_data, revcomp=True)

        test_rev_read.reverse_complement()  # take reverse complement for comparison after creating the test data
        self.assertTupleEqual(next(iterator), (test_fwd_read, test_rev_read))

    def test_truncated(self) -> None:
        fwd_data = StringIO("@TEST:123:456 AAA\nAAGN")
        test_rev_read = FastqRead(
            header="@TEST:123:456 BBB",
            sequence="ACGTAA",
            header2="+",
            quality_string="AAA!CD",
        )
        rev_data = StringIO(str(test_rev_read))

        iterator = parse_fastq_pe_reads(fwd_data, rev_data)

        self.assertRaises(ValueError, next, iterator)

    def test_header_mismatch(self) -> None:
        test_fwd_read = FastqRead(
            header="@TEST:123:456 AAA",
            sequence="AAGNCT",
            header2="+",
            quality_string="!~ABCD",
        )
        fwd_data = StringIO(str(test_fwd_read))
        test_rev_read = FastqRead(
            header="@TEST:123:789 BBB",
            sequence="ACGTAA",
            header2="+",
            quality_string="AAA!CD",
        )
        rev_data = StringIO(str(test_rev_read))

        iterator = parse_fastq_pe_reads(fwd_data, rev_data)

        self.assertRaises(ValueError, next, iterator)


if __name__ == "__main__":
    unittest.main()
