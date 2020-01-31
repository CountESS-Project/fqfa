File handling
*************

fqfa implements several functions to help open FASTA_ and FASTQ_ data files.
This includes functions for validating file names as well as for opening compressed file handles.
Currently fqfa supports opening files compressed with bzip2 or gzip.
Generally speaking, gzip is faster and more widely-supported by other bioinformatics software,
but bzip2 offers slightly better compression that may be relevant for large FASTQ_ files that are not frequently
accessed.

The generator functions for FASTA_ and FASTQ_ files take open file handles as their arguments,
supporting the use of :py:func:`~fqfa.util.file.open_compressed`.

.. automodule:: fqfa.util.file
   :members:

FASTA files
========================

fqfa has basic support for FASTA_ files.
This is designed for small FASTA_ files such as those containing gene or plasmid sequences.
fqfa does not use or create FASTA_ index (``.fai``) files.

The generator function below that parses FASTA_ files is slightly more flexible than the FASTA specification.
Specifically, it ignores any lines before the first FASTA_ record, allowing for comments or other metadata at the
start of the file, and allows any amount of leading or trailing whitespace in the sequence
(including blank lines within a record).

No validation is performed on the sequences, but fqfa implements a set of
:ref:`callable validators<Sequence validation>` that can be used.

.. automodule:: fqfa.fasta.fasta
   :members:

FASTQ files
========================

fqfa supports reading FASTQ files either singly or as a pair (for paired-end data).
Reads are returned as :py:class:`~fqfa.fastq.fastqread.FastqRead` objects.
These objects support several basic operations, such as in-place read trimming and calculating quality-based values.
The sequence and headers are stored as strings, and the quality values are stored as a list of integers.

.. automodule:: fqfa.fastq.fastq
   :members:

.. automodule:: fqfa.fastq.fastqread
   :members:
   :special-members:
