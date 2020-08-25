Performance comparison
*****************************

This page contains some performance and usage comparisons for processing FASTQ_ files with
fqfa and `pyfastx <https://github.com/lmdu/pyfastx>`_.

In these benchmarks, fqfa is comparable to `pyfastx <https://github.com/lmdu/pyfastx>`_,
although `pyfastx <https://github.com/lmdu/pyfastx>`_ has made substantial performance
improvements since fqfa was written, particularly when reading gzip-compressed input files.

The results are derived from `Jupyter notebooks <https://jupyter.org/>`_.
If you'd like to run this code yourself, the notebooks are available with the fqfa
documentation in ``fqfa/docs/notebooks``.
The file used in the benchmark is from the
`Enrich2 example dataset <https://github.com/FowlerLab/Enrich2-Example>`_.
To run the benchmarks as written, you will have to decompress the bz2 file and also
create a gzipped version.

This section includes examples of usage that are common in my work, primarily in
processing files of barcode reads for high-throughput functional genomic assays.
`pyfastx <https://github.com/lmdu/pyfastx>`_ includes many other functions that are not
demonstrated here.

Benchmarking for raw FASTQ files
#####################################

.. include:: notebooks/exported/benchmarks_raw.rst

Benchmarking for gzip-compressed FASTQ files
##################################################

.. include:: notebooks/exported/benchmarks_gz.rst

Benchmarking for bzip2-compressed FASTQ files
##################################################

.. include:: notebooks/exported/benchmarks_bz2.rst
