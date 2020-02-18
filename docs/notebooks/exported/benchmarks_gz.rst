.. code:: ipython3

    import pyfastx
    from fqfa.fastq.fastq import parse_fastq_reads
    from fqfa.util.file import open_compressed

Benchmark 1: list of reads
==========================

This code creates a list containing all the reads in the file. Note that
the data structures for the reads are quite different, with two being
package-specific objects and one being a tuple.

pyfastx with index
------------------

Much of the time spent in the first example is likely spent building the
``.fxi`` index file. This file enables direct access into the FASTQ
file, which we are not using here. The index is quite large, much larger
than the reads in this case:

::

   334M    BRCA1_input_sample.fq
   48M     BRCA1_input_sample.fq.bz2
   520M    BRCA1_input_sample.fq.fxi
   68M     BRCA1_input_sample.fq.gz
   522M    BRCA1_input_sample.fq.gz.fxi

.. code:: ipython3

    %time reads = [x for x in pyfastx.Fastq("BRCA1_input_sample.fq.gz")]
    for x in reads[:5]:
        print(repr(x))
    del reads


.. parsed-literal::

    CPU times: user 32.1 s, sys: 18.6 s, total: 50.7 s
    Wall time: 50.8 s
    <Read> 140313_SN743_0432_AC3TTHACXX:4:1101:5633:2224:1#0/1 with length of 16
    <Read> 140313_SN743_0432_AC3TTHACXX:4:1101:6580:2239:1#0/1 with length of 16
    <Read> 140313_SN743_0432_AC3TTHACXX:4:1101:6929:2242:1#0/1 with length of 16
    <Read> 140313_SN743_0432_AC3TTHACXX:4:1101:13004:2221:1#0/1 with length of 16
    <Read> 140313_SN743_0432_AC3TTHACXX:4:1101:14034:2219:1#0/1 with length of 16


pyfastx without index
---------------------

This is by far the fastest for just reading data from the file, but it
doesn’t perform any extra computation or quality value conversion.

.. code:: ipython3

    %time reads = [x for x in pyfastx.Fastq("BRCA1_input_sample.fq.gz", build_index=False)]
    for x in reads[:5]:
        print(x)
    del reads


.. parsed-literal::

    CPU times: user 3.34 s, sys: 452 ms, total: 3.79 s
    Wall time: 3.79 s
    ('140313_SN743_0432_AC3TTHACXX:4:1101:5633:2224:1#0/1', 'CCCGTGGCCTTTTCCA', 'B@CFFFFFHHHHHJJJ')
    ('140313_SN743_0432_AC3TTHACXX:4:1101:6580:2239:1#0/1', 'TTTGGTAAAGGGTAAC', 'BBCFFDFFHHHHDHIJ')
    ('140313_SN743_0432_AC3TTHACXX:4:1101:6929:2242:1#0/1', 'AATAATGTATGTACCT', 'BC@FFFFEFHHHHJJJ')
    ('140313_SN743_0432_AC3TTHACXX:4:1101:13004:2221:1#0/1', 'CTATTGCGTGTGATCT', 'BCCFFFFFHHHHHJJJ')
    ('140313_SN743_0432_AC3TTHACXX:4:1101:14034:2219:1#0/1', 'ACCCCTACCCTCTGCC', 'BBBFFFFFHHHHHJJJ')


fqfa
----

Unlike pyfastx, fqfa takes an open file handle rather than a file name.
In these examples, this is addressed using a context created by a with
statement.

.. code:: ipython3

    with open_compressed("BRCA1_input_sample.fq.gz") as handle:
        %time reads = [x for x in parse_fastq_reads(handle)]
    for x in reads[:5]:
        print(x)
    del reads


.. parsed-literal::

    CPU times: user 39.7 s, sys: 757 ms, total: 40.5 s
    Wall time: 40.5 s
    @140313_SN743_0432_AC3TTHACXX:4:1101:5633:2224:1#0/1
    CCCGTGGCCTTTTCCA
    +
    B@CFFFFFHHHHHJJJ
    @140313_SN743_0432_AC3TTHACXX:4:1101:6580:2239:1#0/1
    TTTGGTAAAGGGTAAC
    +
    BBCFFDFFHHHHDHIJ
    @140313_SN743_0432_AC3TTHACXX:4:1101:6929:2242:1#0/1
    AATAATGTATGTACCT
    +
    BC@FFFFEFHHHHJJJ
    @140313_SN743_0432_AC3TTHACXX:4:1101:13004:2221:1#0/1
    CTATTGCGTGTGATCT
    +
    BCCFFFFFHHHHHJJJ
    @140313_SN743_0432_AC3TTHACXX:4:1101:14034:2219:1#0/1
    ACCCCTACCCTCTGCC
    +
    BBBFFFFFHHHHHJJJ


Benchmark 2: summarized quality statistics
==========================================

This code calculates the median average read quality for all reads in
the file.

.. code:: ipython3

    from statistics import mean, median

pyfastx with index
------------------

pyfastx provides integer quality values as part of its FASTQ read data
structure.

Note: this step ran for over an hour without completing, so timing
information is not provided.

.. code:: ipython3

    %time read_quals = [mean(x.quali) for x in pyfastx.Fastq("BRCA1_input_sample.fq.gz")]
    print(f"Median average quality is {median(read_quals)}")
    del read_quals

pyfastx without index
---------------------

The timing here is quite a bit closer to the others, since the
conversion and calculation has not already been performed as part of
processing the input file.

.. code:: ipython3

    %time read_quals = [mean([ord(c) - 33 for c in x[2]]) for x in pyfastx.Fastq("BRCA1_input_sample.fq.gz", build_index=False)]
    print(f"Median average quality is {median(read_quals)}")
    del read_quals


.. parsed-literal::

    CPU times: user 1min 12s, sys: 95.6 ms, total: 1min 12s
    Wall time: 1min 12s
    Median average quality is 37.5


fqfa
----

This code uses the ``average_quality()`` method implemented by the
FastqRead class.

.. code:: ipython3

    with open_compressed("BRCA1_input_sample.fq.gz") as handle:
        %time read_quals = [x.average_quality() for x in parse_fastq_reads(handle)]
    print(f"Median average quality is {median(read_quals)}")
    del read_quals


.. parsed-literal::

    CPU times: user 1min 42s, sys: 119 ms, total: 1min 42s
    Wall time: 1min 42s
    Median average quality is 37.5


Benchmark 3: filtering reads on quality
=======================================

This code creates a list of reads for which all bases are at least Q20.
The performance and usage in this section is quite similar to Benchmark
2.

pyfastx with index
------------------

Note: this step ran for over an hour without completing, so timing
information is not provided.

.. code:: ipython3

    %time filt_reads = [x for x in pyfastx.Fastq("BRCA1_input_sample.fq.gz") if min(x.quali) >= 20]
    print(f"Kept {len(filt_reads)} reads after applying filter.")
    del filt_reads

pyfastx without index
---------------------

.. code:: ipython3

    %time filt_reads = [x for x in pyfastx.Fastq("BRCA1_input_sample.fq.gz", build_index=False) if min([ord(c) - 33 for c in x[2]]) >= 20]
    print(f"Kept {len(filt_reads)} reads after applying filter.")
    del filt_reads


.. parsed-literal::

    CPU times: user 9.29 s, sys: 356 ms, total: 9.65 s
    Wall time: 9.65 s
    Kept 3641762 reads after applying filter.


fqfa
----

This code uses the ``min_quality()`` method implemented by the FastqRead
class.

.. code:: ipython3

    with open_compressed("BRCA1_input_sample.fq.gz") as handle:
        %time filt_reads = [x for x in parse_fastq_reads(handle) if x.min_quality() >= 20]
    print(f"Kept {len(filt_reads)} reads after applying filter.")
    del filt_reads


.. parsed-literal::

    CPU times: user 39.9 s, sys: 884 ms, total: 40.8 s
    Wall time: 40.8 s
    Kept 3641762 reads after applying filter.



