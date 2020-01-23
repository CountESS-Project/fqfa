import unittest
from io import StringIO
from fqfa.fastq.fastq import yield_fastq_reads


class TestYieldFastqReads(unittest.TestCase):
    def test_empty(self) -> None:
        data = StringIO("")

        iterator = yield_fastq_reads(data)

        # should return an empty generator
        self.assertRaises(StopIteration, next, iterator)

    def test_single(self) -> None:
        data = StringIO("@TEST:123:456 AAA\nAAGNCT\n+\n!~ABCD\n")

        iterator = yield_fastq_reads(data)

        read = next(iterator)

        self.assertEqual(read.header, "@TEST:123:456 AAA")
        self.assertEqual(read.sequence, "AAGNCT")
        self.assertEqual(read.header2, "+")
        self.assertListEqual(read.quality, [0, 93, 32, 33, 34, 35])

    def test_truncated(self) -> None:
        data = StringIO("@TEST:123:456 AAA\nAAGN")

        iterator = yield_fastq_reads(data)

        self.assertRaises(ValueError, next, iterator)


if __name__ == "__main__":
    unittest.main()
