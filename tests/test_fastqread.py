import unittest
from typing import Dict, Any
from statistics import mean
from fqfa.fastq.fastqread import FastqRead
from fqfa.util.nucleotide import reverse_complement


class TestFastqRead(unittest.TestCase):
    def setUp(self) -> None:
        self.test_kwargs: Dict[str, Any] = {
            "header": "@TEST:123:456 AAA",
            "sequence": "AAGNCT",
            "header2": "+",
            "quality_string": "!~ABCD",
            "quality_encoding_value": 33,
        }
        self.test_quality = [0, 93, 32, 33, 34, 35]

    def test_creation_no_errors(self) -> None:
        test_read = FastqRead(**self.test_kwargs)
        self.assertEqual(test_read.header, self.test_kwargs["header"])
        self.assertEqual(test_read.sequence, self.test_kwargs["sequence"])
        self.assertEqual(test_read.header2, self.test_kwargs["header2"])
        self.assertListEqual(test_read.quality, self.test_quality)
        self.assertEqual(
            test_read.quality_encoding_value, self.test_kwargs["quality_encoding_value"]
        )

    def test_creation_bad_header(self) -> None:
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["header"] = "TEST@:123:456 AAA"
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

    def test_creation_bad_header2(self) -> None:
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["header2"] = test_kwargs["header"]
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

    def test_creation_length_mismatch(self) -> None:
        # sequence longer than quality
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["sequence"] = test_kwargs["sequence"] + "A"
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

        # quality longer than sequence
        test_kwargs = self.test_kwargs.copy()
        test_kwargs["quality_string"] = test_kwargs["quality_string"] + "!"
        self.assertRaises(ValueError, FastqRead, **test_kwargs)

    def test_creation_bad_bases(self) -> None:
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

    def test_creation_bad_quality(self) -> None:
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

    def test_length(self) -> None:
        test_read = FastqRead(**self.test_kwargs)
        self.assertEqual(len(test_read), len(self.test_kwargs["sequence"]))

    def test_str(self) -> None:
        test_read = FastqRead(**self.test_kwargs)
        self.assertEqual(str(test_read), "\n".join(list(self.test_kwargs.values())[:4]))

    def test_average_quality(self) -> None:
        test_read = FastqRead(**self.test_kwargs)
        self.assertEqual(test_read.average_quality(), mean(self.test_quality))

    def test_min_quality(self) -> None:
        test_read = FastqRead(**self.test_kwargs)
        self.assertEqual(test_read.min_quality(), min(self.test_quality))

    def test_trim_defaults(self) -> None:
        test_read = FastqRead(**self.test_kwargs)
        test_read.trim()
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))

    def test_trim_start(self) -> None:
        test_read = FastqRead(**self.test_kwargs)
        test_read.trim(start=2)
        self.assertEqual(len(test_read), len(FastqRead(**self.test_kwargs)) - 1)
        self.assertEqual(len(test_read.sequence), len(test_read.quality))
        self.assertEqual(test_read.sequence, FastqRead(**self.test_kwargs).sequence[1:])

        test_read = FastqRead(**self.test_kwargs)
        test_read.trim(start=len(test_read))
        self.assertEqual(len(test_read), 1)
        self.assertEqual(len(test_read.sequence), len(test_read.quality))
        self.assertEqual(
            test_read.sequence, FastqRead(**self.test_kwargs).sequence[-1:]
        )

    def test_trim_end(self) -> None:
        test_read = FastqRead(**self.test_kwargs)
        test_read.trim(end=len(test_read))
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))

        test_read = FastqRead(**self.test_kwargs)
        test_read.trim(end=len(test_read) - 1)
        self.assertEqual(len(test_read), len(FastqRead(**self.test_kwargs)) - 1)
        self.assertEqual(len(test_read.sequence), len(test_read.quality))
        self.assertEqual(
            test_read.sequence, FastqRead(**self.test_kwargs).sequence[:-1]
        )

        test_read = FastqRead(**self.test_kwargs)
        test_read.trim(end=1)
        self.assertEqual(len(test_read), 1)
        self.assertEqual(len(test_read.sequence), len(test_read.quality))
        self.assertEqual(test_read.sequence, FastqRead(**self.test_kwargs).sequence[:1])

    def test_trim_both_ends(self) -> None:
        test_read = FastqRead(**self.test_kwargs)
        test_read.trim(start=2, end=2)
        self.assertEqual(len(test_read), 1)
        self.assertEqual(len(test_read.sequence), len(test_read.quality))
        self.assertEqual(
            test_read.sequence, FastqRead(**self.test_kwargs).sequence[1:2]
        )

        test_read = FastqRead(**self.test_kwargs)
        test_read.trim(start=2, end=4)
        self.assertEqual(len(test_read), 3)
        self.assertEqual(len(test_read.sequence), len(test_read.quality))
        self.assertEqual(
            test_read.sequence, FastqRead(**self.test_kwargs).sequence[1:4]
        )

    def test_trim_bad_parameters(self) -> None:
        test_read = FastqRead(**self.test_kwargs)

        # bad start parameters
        self.assertRaises(ValueError, test_read.trim, start=-1)
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))
        self.assertRaises(ValueError, test_read.trim, start=0)
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))
        self.assertRaises(ValueError, test_read.trim, start=len(test_read) + 1)
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))

        # bad end parameters
        self.assertRaises(ValueError, test_read.trim, end=-1)
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))
        self.assertRaises(ValueError, test_read.trim, end=0)
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))

        # bad parameter combinations
        self.assertRaises(ValueError, test_read.trim, start=-1, end=0)
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))
        self.assertRaises(ValueError, test_read.trim, start=4, end=3)
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))

    def test_trim_length(self) -> None:
        test_read = FastqRead(**self.test_kwargs)
        test_read.trim_length(length=len(test_read))
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))

        test_read = FastqRead(**self.test_kwargs)
        test_read.trim_length(length=1)
        self.assertEqual(len(test_read), 1)
        self.assertEqual(len(test_read.sequence), len(test_read.quality))
        self.assertEqual(test_read.sequence, FastqRead(**self.test_kwargs).sequence[:1])

        test_read = FastqRead(**self.test_kwargs)
        test_read.trim_length(length=2)
        self.assertEqual(len(test_read), 2)
        self.assertEqual(len(test_read.sequence), len(test_read.quality))
        self.assertEqual(test_read.sequence, FastqRead(**self.test_kwargs).sequence[:2])

        test_read = FastqRead(**self.test_kwargs)
        test_read.trim_length(start=2, length=4)
        self.assertEqual(len(test_read), 4)
        self.assertEqual(len(test_read.sequence), len(test_read.quality))
        self.assertEqual(
            test_read.sequence, FastqRead(**self.test_kwargs).sequence[1:5]
        )

    def test_trim_length_bad_parameters(self) -> None:
        test_read = FastqRead(**self.test_kwargs)

        # bad start parameters
        self.assertRaises(
            ValueError, test_read.trim_length, start=-1, length=len(test_read)
        )
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))
        self.assertRaises(
            ValueError, test_read.trim_length, start=0, length=len(test_read)
        )
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))
        self.assertRaises(
            ValueError,
            test_read.trim_length,
            start=len(test_read) + 1,
            length=len(test_read),
        )
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))

        # bad length parameters
        self.assertRaises(ValueError, test_read.trim_length, length=-1)
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))
        self.assertRaises(ValueError, test_read.trim_length, length=0)
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))
        self.assertRaises(ValueError, test_read.trim_length, length=len(test_read) + 1)
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))

        # bad parameter combinations
        self.assertRaises(ValueError, test_read.trim_length, start=-1, length=0)
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))
        self.assertRaises(
            ValueError, test_read.trim_length, start=2, length=len(test_read)
        )
        self.assertEqual(test_read, FastqRead(**self.test_kwargs))

    def test_reverse_complement(self) -> None:
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
