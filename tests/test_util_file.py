import unittest


class TestOpenCompressed(unittest.TestCase):
    @unittest.expectedFailure
    def test_something(self) -> None:
        self.assertEqual(True, False)


class TestHasFastqExt(unittest.TestCase):
    @unittest.expectedFailure
    def test_something(self) -> None:
        self.assertEqual(True, False)


class TestHasFastaExt(unittest.TestCase):
    @unittest.expectedFailure
    def test_something(self) -> None:
        self.assertEqual(True, False)


if __name__ == "__main__":
    unittest.main()
