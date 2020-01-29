Sequence validation
*******************

fqfa implements regular expression-based sequence validators.
There are several commonly-used validators based on :ref:`IUPAC codes<IUPAC codes>`,
as well as a function for creating new callable validators from a string or list of characters.
This :py:func:`~fqfa.validator.create.create_validator` function can also be used to create case-insensitive versions
of the provided validators.

.. automodule:: fqfa.validator.validator
   :members:

.. automodule:: fqfa.validator.create
   :members:

IUPAC codes
===========

fqfa includes the International Union of Pure and Applied Chemistry (IUPAC) notation for degenerate bases.
A mapping between single- and three-letter amino acid codes is also included.
Validation based on single-letter amino acid codes can be accomplished by using the keys of the mapping.

DNA sequences
-------------

.. automodule:: fqfa.constants.iupac.dna
   :members:

RNA sequences
-------------

.. automodule:: fqfa.constants.iupac.rna
   :members:

Amino acid sequences
--------------------

.. automodule:: fqfa.constants.iupac.protein
   :members:
