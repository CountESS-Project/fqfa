import unittest

from fqfa.validator.create import create_validator


class TestCreateValidator(unittest.TestCase):
    def test_create_from_string(self) -> None:
        # case sensitive
        validator = create_validator("ACGT")

        # test valid strings
        self.assertIsNotNone(validator("ACGT"))
        self.assertIsNotNone(validator("AAAAAAA"))

        # test invalid strings
        self.assertIsNone(validator("acgt"))
        self.assertIsNone(validator("AAAAAAa"))
        self.assertIsNone(validator(""))
        self.assertIsNone(validator("123"))
        self.assertIsNone(validator("AAAA AAA"))

        # case insensitive
        validator = create_validator("ACGT", case_sensitive=False)

        # test valid strings
        self.assertIsNotNone(validator("ACGT"))
        self.assertIsNotNone(validator("AAAAAAA"))
        self.assertIsNotNone(validator("acgt"))
        self.assertIsNotNone(validator("AAAAAAa"))

        # test invalid strings
        self.assertIsNone(validator(""))
        self.assertIsNone(validator("123"))
        self.assertIsNone(validator("AAAA AAA"))

    def test_create_from_list(self) -> None:
        # case sensitive
        validator = create_validator(list("ACGT"))

        # test valid strings
        self.assertIsNotNone(validator("ACGT"))
        self.assertIsNotNone(validator("AAAAAAA"))

        # test invalid strings
        self.assertIsNone(validator("acgt"))
        self.assertIsNone(validator("AAAAAAa"))
        self.assertIsNone(validator(""))
        self.assertIsNone(validator("123"))
        self.assertIsNone(validator("AAAA AAA"))

        # case insensitive
        validator = create_validator(list("ACGT"), case_sensitive=False)

        # test valid strings
        self.assertIsNotNone(validator("ACGT"))
        self.assertIsNotNone(validator("AAAAAAA"))
        self.assertIsNotNone(validator("acgt"))
        self.assertIsNotNone(validator("AAAAAAa"))

        # test invalid strings
        self.assertIsNone(validator(""))
        self.assertIsNone(validator("123"))
        self.assertIsNone(validator("AAAA AAA"))

        # invalid list arguments
        self.assertRaises(ValueError, create_validator, ["A", "C", "GT"])
        self.assertRaises(
            ValueError, create_validator, ["A", "C", "GT"], case_sensitive=False
        )
        self.assertRaises(ValueError, create_validator, ["A", "C", ""])
        self.assertRaises(
            ValueError, create_validator, ["A", "C", ""], case_sensitive=False
        )


if __name__ == "__main__":
    unittest.main()
