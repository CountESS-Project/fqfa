.. code:: ipython3

    import pyfastx
    from fqfa.fastq.fastq import parse_fastq_reads

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

    %time reads = [x for x in pyfastx.Fastq("BRCA1_input_sample.fq")]
    for x in reads[:5]:
        print(repr(x))
    del reads


.. parsed-literal::

    CPU times: user 29.5 s, sys: 17 s, total: 46.5 s
    Wall time: 46.5 s
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

    %time reads = [x for x in pyfastx.Fastq("BRCA1_input_sample.fq", build_index=False)]
    for x in reads[:5]:
        print(x)
    del reads


.. parsed-literal::

    CPU times: user 1.68 s, sys: 384 ms, total: 2.07 s
    Wall time: 2.07 s
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

    with open("BRCA1_input_sample.fq") as handle:
        %time reads = [x for x in parse_fastq_reads(handle)]
    for x in reads[:5]:
        print(x)
    del reads


.. parsed-literal::

    CPU times: user 33.2 s, sys: 934 ms, total: 34.1 s
    Wall time: 34 s
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

.. code:: ipython3

    %time read_quals = [mean(x.quali) for x in pyfastx.Fastq("BRCA1_input_sample.fq")]
    print(f"Median average quality is {median(read_quals)}")
    del read_quals


.. parsed-literal::

    CPU times: user 2min 6s, sys: 30.4 s, total: 2min 37s
    Wall time: 2min 37s
    Median average quality is 37.5


pyfastx without index
---------------------

The timing here is quite a bit closer to the others, since the
conversion and calculation has not already been performed as part of
processing the input file.

.. code:: ipython3

    %time read_quals = [mean([ord(c) - 33 for c in x[2]]) for x in pyfastx.Fastq("BRCA1_input_sample.fq", build_index=False)]
    print(f"Median average quality is {median(read_quals)}")
    del read_quals


.. parsed-literal::

    CPU times: user 1min 10s, sys: 87.3 ms, total: 1min 10s
    Wall time: 1min 10s
    Median average quality is 37.5


fqfa
----

This code uses the ``average_quality()`` method implemented by the
FastqRead class.

.. code:: ipython3

    with open("BRCA1_input_sample.fq") as handle:
        %time read_quals = [x.average_quality() for x in parse_fastq_reads(handle)]
    print(f"Median average quality is {median(read_quals)}")
    del read_quals


.. parsed-literal::

    CPU times: user 1min 27s, sys: 214 ms, total: 1min 27s
    Wall time: 1min 27s
    Median average quality is 37.5


Benchmark 3: filtering reads on quality
=======================================

This code creates a list of reads for which all bases are at least Q20.
The performance and usage in this section is quite similar to Benchmark
2.

pyfastx with index
------------------

.. code:: ipython3

    %time filt_reads = [x for x in pyfastx.Fastq("BRCA1_input_sample.fq") if min(x.quali) >= 20]
    print(f"Kept {len(filt_reads)} reads after applying filter.")
    del filt_reads


.. parsed-literal::

    CPU times: user 41.1 s, sys: 24.7 s, total: 1min 5s
    Wall time: 1min 5s
    Kept 3641762 reads after applying filter.


pyfastx without index
---------------------

.. code:: ipython3

    %time filt_reads = [x for x in pyfastx.Fastq("BRCA1_input_sample.fq", build_index=False) if min([ord(c) - 33 for c in x[2]]) >= 20]
    print(f"Kept {len(filt_reads)} reads after applying filter.")
    del filt_reads


.. parsed-literal::

    CPU times: user 7.63 s, sys: 314 ms, total: 7.94 s
    Wall time: 7.94 s
    Kept 3641762 reads after applying filter.


fqfa
----

This code uses the ``min_quality()`` method implemented by the FastqRead
class.

.. code:: ipython3

    with open("BRCA1_input_sample.fq") as handle:
        %time filt_reads = [x for x in parse_fastq_reads(handle) if x.min_quality() >= 20]
    print(f"Kept {len(filt_reads)} reads after applying filter.")
    del filt_reads


.. parsed-literal::

    CPU times: user 37.2 s, sys: 863 ms, total: 38.1 s
    Wall time: 38 s
    Kept 3641762 reads after applying filter.



