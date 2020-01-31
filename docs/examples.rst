Usage examples
********************

This page contains some example use cases for fqfa.
They are formatted as :py:mod:`doctest` tests.

Basic sequence validation
=========================

The validators in :py:mod:`fqfa.validator.validator` return a match object if the sequence validates or None if the
sequence doesn't validate. This means that they can be used in simple if statements.

.. testsetup:: validators

   from fqfa.validator.validator import dna_bases_validator, dna_characters_validator
   from fqfa.validator.create import create_validator
   from fqfa.constants.iupac.dna import DNA_BASES

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

Filtering paired-end FASTQ reads on sequence quality
====================================================

