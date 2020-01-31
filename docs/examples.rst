Usage examples
********************

This page contains some example use cases for fqfa.
They are formatted as :py:mod:`doctest` tests.

Basic sequence validation
=========================

.. testsetup:: validators

   from fqfa.validator.validator import dna_bases_validator, dna_characters_validator
   from fqfa.validator.create import create_validator
   from fqfa.constants.iupac.dna import DNA_BASES

The validators in :py:mod:`fqfa.validator.validator` return a match object if the sequence validates or None if the
sequence doesn't validate. This means that they can be used in simple if statements.

This validator only accepts the standard DNA bases, so the input sequence is invalid.

.. doctest:: validators
   :pyversion: >= 3.6

   >>> if dna_bases_validator("ACGTNW"):
   ...     print("valid!")
   ... else:
   ...     print("invalid!")
   invalid!

This validator accepts all IUPAC bases, so the input sequence is valid.

.. doctest:: validators
   :pyversion: >= 3.6

   >>> if dna_characters_validator("ACGTNW"):
   ...     print("valid!")
   ... else:
   ...     print("invalid!")
   valid!

The validators only accept strings (or bytes), as they are based on regular expressions.
Attempting to validate anything else results in a :py:class:`TypeError`.

.. doctest:: validators
   :pyversion: >= 3.6

   >>> if dna_characters_validator(42):
   ...     print("valid!")
   ... else:
   ...     print("invalid!")
   Traceback (most recent call last):
       ...
   TypeError: expected string or bytes-like object

Default validators only accept uppercase characters, so mixed-case or lowercase input is invalid.

.. doctest:: validators
   :pyversion: >= 3.6

   >>> if dna_bases_validator("ACgT"):
   ...     print("valid!")
   ... else:
   ...     print("invalid!")
   invalid!

Case-insensitive validators can be created using :py:func:`~fqfa.validator.create.create_validator`.

.. doctest:: validators
   :pyversion: >= 3.6

   >>> case_insensitive_validator = create_validator(DNA_BASES, case_sensitive=False)
   >>> if case_insensitive_validator("ACgT"):
   ...     print("valid!")
   ... else:
   ...     print("invalid!")
   valid!


Translating FASTA sequences
===========================

.. testsetup:: fasta

   from io import StringIO
   from fqfa.validator.validator import dna_bases_validator
   from fqfa.fasta.fasta import parse_fasta_records, write_fasta_record
   from fqfa.util.translate import translate_dna

fqfa implements a function to parse individual records from FASTA_ files.

.. doctest:: fasta
   :pyversion: >= 3.6

   >>> fasta_string = """
   ... >test record
   ... ACGAAA
   ... TAA
   ...
   ... >another record here
   ... ACANaa
   ... """
   >>> for header, seq in parse_fasta_records(StringIO(fasta_string)):
   ...     print(header)
   ...     print(seq)
   test record
   ACGAAATAA
   another record here
   ACANaa

These sequences can be validated and/or transformed using utility functions in the library and rewritten as FASTA_
output.

.. doctest:: fasta
   :pyversion: >= 3.6

   >>> fasta_string = """
   ... >test record
   ... ACGAAA
   ... TAA
   ... """
   >>> output_file = StringIO()
   >>> for header, dna_seq in parse_fasta_records(StringIO(fasta_string)):
   ...     if dna_bases_validator(dna_seq):
   ...         protein_seq, _ = translate_dna(dna_seq)
   ...         write_fasta_record(output_file, header, protein_seq)
   >>> output_file.seek(0)
   0
   >>> print(output_file.read())
   >test record
   TK*
   <BLANKLINE>

Filtering paired-end FASTQ reads on sequence quality
====================================================

