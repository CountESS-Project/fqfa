Utility functions
********************

fqfa provides basic utility functions for working with biological sequences as strings.
For efficiency, these functions assume that any required validation
(such as making sure all the characters string are valid bases) has already been performed.

fqfa has a copy of the :ref:`standard translation table<translation table>` and alternative translation tables can be imported using
:py:func:`~fqfa.util.translate.ncbi_genetic_code_to_dict`.

Nucleotide sequence utility functions
=====================================

.. automodule:: fqfa.util.nucleotide
   :members:

Coding sequence translation
===========================

.. automodule:: fqfa.util.translate
   :members:

.. _translation table:

.. automodule:: fqfa.constants.translation.table
   :members:
