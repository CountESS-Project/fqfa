import unittest
from statistics import mean
from fqfa.fastq.fastqread import FastqRead
from fqfa.util.util import reverse_complement


class TestFastqRead(unittest.TestCase):
    def setUp(self) -> None:
        self.test_kwargs = {
            "header": "@TEST:123:456 AAA",
            "sequence": "AAGNCT",
            "header2": "+",
            "quality_string": "!~ABCD",
            "quality_encoding_value": 33,
        }
        self.test_quality = [0, 93, 32, 33, 34, 35]

    def test_creation_no_errors(self):
        test_read = FastqRead(**self.test_kwargs)
        self.assertEqual(test_read.header, self.test_kwargs["header"])
        self.assertEqual(test_read.sequence, self.test_kwargs["sequence"])
        self.assertEqual(test_read.header2, self.test_kwargs["header2"])
        self.assertListEqual(test_read.quality, self.test_quality)
        self.assertEqual(
            test_read.quality_encoding_value, self.test_kwargs["quality_encoding_value"]
        )

    def test_creation_bad_header(self):
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["header"] = "TEST@:123:456 AAA"
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

    def test_creation_bad_header2(self):
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["header2"] = test_kwargs["header"]
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

    def test_creation_length_mismatch(self):
        # sequence longer than quality
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["sequence"] = test_kwargs["sequence"] + "A"
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

        # quality longer than sequence
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["quality_string"] = test_kwargs["quality_string"] + "!"
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

    def test_creation_bad_bases(self):
        # bad first base/duplicate header
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["sequence"] = "@" + self.test_kwargs["sequence"][1:]
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

        # bad internal base/ambiguity character
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["sequence"] = (
            self.test_kwargs["sequence"][:1] + "W" + self.test_kwargs["sequence"][2:]
        )
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

        # bad last base/number
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["sequence"] = self.test_kwargs["sequence"][:-1] + "8"
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

    def test_creation_bad_quality(self):
        # bad first value/whitespace (too low)
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["quality_string"] = " " + self.test_kwargs["quality_string"][1:]
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

        # bad internal value/unicode character
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["quality_string"] = (
            self.test_kwargs["quality_string"][:1]
            + "µ"
            + self.test_kwargs["quality_string"][2:]
        )
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

        # bad last value/whitespace (too low)
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["sequence"] = self.test_kwargs["sequence"][:-1] + " "
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

    def test_length(self):
        test_read = FastqRead(**self.test_kwargs)
        self.assertEqual(len(test_read), len(self.test_kwargs["sequence"]))

    def test_str(self):
        test_read = FastqRead(**self.test_kwargs)
        self.assertEqual(str(test_read), "\n".join(list(self.test_kwargs.values())[:4]))

    def test_average_quality(self):
        test_read = FastqRead(**self.test_kwargs)
        self.assertEqual(test_read.average_quality(), mean(self.test_quality))

    def test_min_quality(self):
        test_read = FastqRead(**self.test_kwargs)
        self.assertEqual(test_read.min_quality(), min(self.test_quality))

    def test_trim(self):
        self.assertEqual(True, False)

    def test_trim_length(self):
        self.assertEqual(True, False)

    def test_reverse_complement(self):
        test_read = FastqRead(**self.test_kwargs)
        test_read.reverse_complement()

        self.assertEqual(test_read.header, self.test_kwargs["header"])
        self.assertEqual(
            test_read.sequence, reverse_complement(self.test_kwargs["sequence"])
        )
        self.assertEqual(test_read.header2, self.test_kwargs["header2"])
        self.assertListEqual(test_read.quality, self.test_quality[::-1])
        self.assertEqual(
            test_read.quality_encoding_value, self.test_kwargs["quality_encoding_value"]
        )


if __name__ == "__main__":
    unittest.main()
