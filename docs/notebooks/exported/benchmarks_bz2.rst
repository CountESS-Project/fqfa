.. code:: ipython3

    import pyfastx
    from fqfa.fastq.fastq import parse_fastq_reads
    from fqfa.util.file import open_compressed

Benchmark 1: list of reads
==========================

This code creates a list containing all the reads in the file. Note that
the data structures for the reads are quite different, with two being
package-specific objects and one being a tuple.

Because pyfastx does not support bzip2, these results are most useful
for comparing with fqfa’s gzip benchmarks.

fqfa
----

Unlike pyfastx, fqfa takes an open file handle rather than a file name.
In these examples, this is addressed using a context created by a with
statement.

.. code:: ipython3

    with open_compressed("BRCA1_input_sample.fq.bz2") as handle:
        %time reads = [x for x in parse_fastq_reads(handle)]
    for x in reads[:5]:
        print(x)
    del reads


.. parsed-literal::

    CPU times: user 51.3 s, sys: 993 ms, total: 52.3 s
    Wall time: 52.3 s
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

fqfa
----

This code uses the ``average_quality()`` method implemented by the
FastqRead class.

.. code:: ipython3

    with open_compressed("BRCA1_input_sample.fq.bz2") as handle:
        %time read_quals = [x.average_quality() for x in parse_fastq_reads(handle)]
    print(f"Median average quality is {median(read_quals)}")
    del read_quals


.. parsed-literal::

    CPU times: user 1min 59s, sys: 174 ms, total: 1min 59s
    Wall time: 1min 59s
    Median average quality is 37.5


Benchmark 3: filtering reads on quality
=======================================

This code creates a list of reads for which all bases are at least Q20.
The performance and usage in this section is quite similar to Benchmark
2.

fqfa
----

This code uses the ``min_quality()`` method implemented by the FastqRead
class.

.. code:: ipython3

    with open_compressed("BRCA1_input_sample.fq.bz2") as handle:
        %time filt_reads = [x for x in parse_fastq_reads(handle) if x.min_quality() >= 20]
    print(f"Kept {len(filt_reads)} reads after applying filter.")
    del filt_reads


.. parsed-literal::

    CPU times: user 58.8 s, sys: 848 ms, total: 59.7 s
    Wall time: 59.7 s
    Kept 3641762 reads after applying filter.



