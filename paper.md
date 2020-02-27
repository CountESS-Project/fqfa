---
title: 'fqfa: A pure Python package for genomic sequence files'
tags:
  - Python
  - genomics
  - bioinformatics
authors:
  - name: Alan F. Rubin
    orcid: 0000-0003-1474-605X
    affiliation: "1, 2"
affiliations:
 - name: The Walter and Eliza Hall Institute of Medical Research
   index: 1
 - name: The University of Melbourne
   index: 2
date: 20 February 2020
bibliography: paper.bib

---

# Summary

Modern bioinformatics requires the use of many field-specific file formats.
Two of the most prevalent formats for representing biological sequences are FASTA [@pearson_improved_1988] and FASTQ [@cock_sanger_2010].
While multiple feature-rich Python bioinformatics libraries exist that can process biological sequence files [@cock_biopython_2009; @noauthor_biocorescikit-bio_2013], they require complex compiled dependencies that may limit their use in non-Unix environments.
Other FASTA or FASTQ specific Python libraries [@pedersen_brentppyfasta_2010; @hunt_sanger-pathogensfastaq_2013; @shirley_efficient_2015; @du_lmdupyfastx_2019] are outdated, require runtime dependencies, or make heavy use of C extensions that prioritize speed over readability and portability. 

fqfa is a pure Python package that aims to fill the needs of bioinformatics and computational biology researchers who want a simple and efficient solution for working with files in FASTA and FASTQ formats.
It has no dependencies outside of the Python standard library (with the exception of backported dataclasses [@smith_ericvsmithdataclasses_2020] for Python 3.6 users) and makes use of newer language features such as type hinting and f-strings to improve readability.
These implementation details make fqfa highly suitable for use in notebooks and projects that have simple requirements, with underlying code that is easy for novice bioinformaticians and students to understand and explore.

Although fqfa is written in pure Python, its performance is comparable to modules using C extensions like pyfastx [@du_lmdupyfastx_2019] for tasks such as processing a FASTQ file sequentially and collecting or filtering on quality statistics from the high-throughput sequencing reads.
Detailed benchmarking results and usage examples comparing fqfa and pyfastx [@du_lmdupyfastx_2019] are available as part of the fqfa documentation in static format as well as in Jupyter notebooks [@Kluyver:2016aa].

fqfa is released under the BSD 3-Clause License and is available from GitHub and PyPI.

# Acknowledgements

Thank you to Matthew Wakefield for helpful discussion and code review.
The research benefited by support from the Victorian State Government Operational Infrastructure Support and Australian Government NHMRC Independent Research Institute Infrastructure Support.
AFR was supported by the National Human Genome Research Institute of the NIH under award number RM1HG010461.

# References
