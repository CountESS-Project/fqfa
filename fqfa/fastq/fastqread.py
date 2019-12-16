"""Defintion for the FastqRead dataclass describing a single FASTQ record.

"""

import re
from dataclasses import dataclass, field, InitVar
from typing import List, Optional, ClassVar, Callable
from statistics import mean
from fqfa.util.util import reverse_complement


@dataclass
class FastqRead:
    """
    TODO
    """

    header: str
    sequence: str
    header2: str
    quality: List[int] = field(init=False)
    quality_string: InitVar[str]
    quality_encoding_value: int = 33
    sequence_pattern: ClassVar[Callable] = re.compile(r"[ACGTN]+").fullmatch

    def __post_init__(self, quality_string: str) -> None:
        """
        This function performs some basic checks on the input and converts the quality string into a list of integers.

        The quality string is converted to integers using the ``quality_encoding_value``, which defaults to Sanger-style
        quality values.

        Parameters
        ----------
        quality_string : str
            ASCII-encoded quality values.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the length of the sequence and quality strings are not equal.
        ValueError
            If the header string doesn't start with '@'.
        ValueError
            If the sequence contains characters other than A, C, G, T, or N.
        ValueError
            If the secondary header string doesn't start with '+'.
        ValueError
            If the quality values are outside the allowed range (0-93).

        """
        if len(self.sequence) != len(quality_string):
            raise ValueError("unequal number of quality values and bases")

        if not self.header.startswith("@"):
            raise ValueError("unexpected value for FASTQ header")
        if not self.header2.startswith("+"):
            raise ValueError("unexpected value for FASTQ header")

        if not self.sequence_pattern(self.sequence):
            raise ValueError("unexpected characters in sequence")

        self.quality = [ord(c) - self.quality_encoding_value for c in quality_string]
        if min(self.quality) < 0:
            raise ValueError("sequence quality value below 0")
        if max(self.quality) > 93:
            raise ValueError("sequence quality value above 93")

    def __len__(self) -> int:
        """
        The object's length is defined as the length of the sequence.

        Returns
        -------
        int
            The length of the read's sequence.

        """
        return len(self.sequence)

    def __str__(self) -> str:
        """
        Formats the object as a four-line FASTQ record.

        Returns
        -------
        str
            Reconstruction of the original FASTQ record.

        """
        quality_string = "".join(
            [chr(q + self.quality_encoding_value) for q in self.quality]
        )
        return "\n".join((self.header, self.sequence, self.header2, quality_string))

    def average_quality(self) -> float:
        """
        Calculates and returns the read's mean quality value.

        Returns
        -------
        float
            Mean quality value.

        """
        return mean(self.quality)

    def min_quality(self) -> int:
        """
        Calculates and returns the read's minimum quality value.

        Returns
        -------
        int
            The lowest quality value.

        """
        return min(self.quality)

    def trim(self, start: int = 1, end: Optional[int] = None) -> None:
        """
        Trim the read such that it contains bases between ``start`` and ``end`` (inclusive).
        Bases are numbered starting at 1.

        Parameters
        ----------
        start : int
            The first base to retain (1-indexed). Defaults to 1, which will not trim the start.
        end : Optional[int]
            The last base to retain (1-indexed). Defaults to ``None``, which will not trim the end.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the start is less than or equal to the end.
        ValueError
            If the start is less than 1.

        """
        if start < 1:
            raise ValueError("start must be at least 1")
        if start <= end:
            raise ValueError("invalid trimming parameters")
        self.sequence = self.sequence[start:end]
        self.quality = self.quality[start:end]

    def trim_length(self, length: int, start: int = 1) -> None:
        """
        Trim the read to a specific length, beginning at ``start``.
        Bases are numbered starting at 1.

        Parameters
        ----------
        length : int
            The length of the read after trimming.

        start : int
            The first base to retain (1-indexed). Defaults to 1, which will not trim the start.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the length is less than 1.
        ValueError
            If the start is less than 1.

        """
        if start < 1:
            raise ValueError("start must be at least 1")
        if length < 1:
            raise ValueError("length must be at least 1")
        self.trim(start=start, end=start + length)

    def reverse_complement(self) -> None:
        """
        Reverse-complements the sequence and reverse the order of quality values.

        Returns
        -------
        None

        """
        self.sequence = reverse_complement(self.sequence)
        self.quality = self.quality[::-1]
