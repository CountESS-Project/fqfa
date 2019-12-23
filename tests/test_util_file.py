import unittest
import unittest.mock as mock

from fqfa.util.file import open_compressed, has_fastq_ext, has_fasta_ext


class TestOpenCompressed(unittest.TestCase):
    @mock.patch("fqfa.util.file.gzip.open")
    @mock.patch("fqfa.util.file.os.path.isfile")
    def test_open_gzip(self, mock_isfile, mock_gzip_open) -> None:
        mock_isfile.return_value = False
        self.assertRaises(FileNotFoundError, open_compressed, "file.fq.gz")

        mock_isfile.return_value = True
        mock_gzip_open.return_value = "opened gz"
        self.assertEqual("opened gz", open_compressed("file.fq.gz"))

    @mock.patch("fqfa.util.file.bz2.open")
    @mock.patch("fqfa.util.file.os.path.isfile")
    def test_open_bzip2(self, mock_isfile, mock_bz2_open) -> None:
        mock_isfile.return_value = False
        self.assertRaises(FileNotFoundError, open_compressed, "file.fq.bz2")

        mock_isfile.return_value = True
        mock_bz2_open.return_value = "opened bz2"
        self.assertEqual("opened bz2", open_compressed("file.fq.bz2"))

    @mock.patch("fqfa.util.file.open")
    @mock.patch("fqfa.util.file.os.path.isfile")
    def test_open_uncompressed(self, mock_isfile, mock_default_open) -> None:
        mock_isfile.return_value = False
        self.assertRaises(FileNotFoundError, open_compressed, "file.fq")

        mock_isfile.return_value = True
        mock_default_open.return_value = "opened uncompressed"
        self.assertEqual("opened uncompressed", open_compressed("file.fq"))


class TestHasFastqExt(unittest.TestCase):
    def test_uncompressed(self) -> None:
        self.assertTrue(has_fastq_ext("file.fq"))
        self.assertTrue(has_fastq_ext("file.fastq"))

        self.assertFalse(has_fastq_ext("file"))
        self.assertFalse(has_fastq_ext(".dotfile"))
        self.assertFalse(has_fastq_ext("file.txt"))

        self.assertTrue(has_fastq_ext("file.fq".upper()))
        self.assertTrue(has_fastq_ext("file.fastq".upper()))

        self.assertTrue(has_fastq_ext("rel/path/to/file.fq"))
        self.assertTrue(has_fastq_ext("rel/path/to/file.fastq"))

        self.assertTrue(has_fastq_ext("/abs/path/to/file.fq"))
        self.assertTrue(has_fastq_ext("/abs/path/to/file.fastq"))

    def test_compressed_bzip2(self) -> None:
        self.assertTrue(has_fastq_ext("file.fq.bz2"))
        self.assertTrue(has_fastq_ext("file.fastq.bz2"))

        self.assertFalse(has_fastq_ext("file.bz2"))
        self.assertFalse(has_fastq_ext(".dotfile.bz2"))
        self.assertFalse(has_fastq_ext("file.txt.bz2"))

        self.assertTrue(has_fastq_ext("file.fq.bz2".upper()))
        self.assertTrue(has_fastq_ext("file.fastq.bz2".upper()))

        self.assertTrue(has_fastq_ext("rel/path/to/file.fq.bz2"))
        self.assertTrue(has_fastq_ext("rel/path/to/file.fastq.bz2"))

        self.assertTrue(has_fastq_ext("/abs/path/to/file.fq.bz2"))
        self.assertTrue(has_fastq_ext("/abs/path/to/file.fastq.bz2"))

    def test_compressed_gzip(self) -> None:
        self.assertTrue(has_fastq_ext("file.fq.gz"))
        self.assertTrue(has_fastq_ext("file.fastq.gz"))

        self.assertFalse(has_fastq_ext("file.gz"))
        self.assertFalse(has_fastq_ext(".dotfile.gz"))
        self.assertFalse(has_fastq_ext("file.txt.gz"))

        self.assertTrue(has_fastq_ext("file.fq.gz".upper()))
        self.assertTrue(has_fastq_ext("file.fastq.gz".upper()))

        self.assertTrue(has_fastq_ext("rel/path/to/file.fq.gz"))
        self.assertTrue(has_fastq_ext("rel/path/to/file.fastq.gz"))

        self.assertTrue(has_fastq_ext("/abs/path/to/file.fq.gz"))
        self.assertTrue(has_fastq_ext("/abs/path/to/file.fastq.gz"))


class TestHasFastaExt(unittest.TestCase):
    def test_uncompressed(self) -> None:
        self.assertTrue(has_fasta_ext("file.fa"))
        self.assertTrue(has_fasta_ext("file.fasta"))

        self.assertFalse(has_fasta_ext("file"))
        self.assertFalse(has_fasta_ext(".dotfile"))
        self.assertFalse(has_fasta_ext("file.txt"))

        self.assertTrue(has_fasta_ext("file.fa".upper()))
        self.assertTrue(has_fasta_ext("file.fasta".upper()))

        self.assertTrue(has_fasta_ext("rel/path/to/file.fa"))
        self.assertTrue(has_fasta_ext("rel/path/to/file.fasta"))

        self.assertTrue(has_fasta_ext("/abs/path/to/file.fa"))
        self.assertTrue(has_fasta_ext("/abs/path/to/file.fasta"))

    def test_compressed_bzip2(self) -> None:
        self.assertTrue(has_fasta_ext("file.fa.bz2"))
        self.assertTrue(has_fasta_ext("file.fasta.bz2"))

        self.assertFalse(has_fasta_ext("file.bz2"))
        self.assertFalse(has_fasta_ext(".dotfile.bz2"))
        self.assertFalse(has_fasta_ext("file.txt.bz2"))

        self.assertTrue(has_fasta_ext("file.fa.bz2".upper()))
        self.assertTrue(has_fasta_ext("file.fasta.bz2".upper()))

        self.assertTrue(has_fasta_ext("rel/path/to/file.fa.bz2"))
        self.assertTrue(has_fasta_ext("rel/path/to/file.fasta.bz2"))

        self.assertTrue(has_fasta_ext("/abs/path/to/file.fa.bz2"))
        self.assertTrue(has_fasta_ext("/abs/path/to/file.fasta.bz2"))

    def test_compressed_gzip(self) -> None:
        self.assertTrue(has_fasta_ext("file.fa.gz"))
        self.assertTrue(has_fasta_ext("file.fasta.gz"))

        self.assertFalse(has_fasta_ext("file.gz"))
        self.assertFalse(has_fasta_ext(".dotfile.gz"))
        self.assertFalse(has_fasta_ext("file.txt.gz"))

        self.assertTrue(has_fasta_ext("file.fa.gz".upper()))
        self.assertTrue(has_fasta_ext("file.fasta.gz".upper()))

        self.assertTrue(has_fasta_ext("rel/path/to/file.fa.gz"))
        self.assertTrue(has_fasta_ext("rel/path/to/file.fasta.gz"))

        self.assertTrue(has_fasta_ext("/abs/path/to/file.fa.gz"))
        self.assertTrue(has_fasta_ext("/abs/path/to/file.fasta.gz"))


if __name__ == "__main__":
    unittest.main()
