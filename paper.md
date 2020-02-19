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
date: 3 February 2020
bibliography: paper.bib

---

# Summary

Modern bioinformatics requires the use of many field-specific file formats.
Two of the most prevalent for representing biological sequences are FASTA [@pearson_improved_1988] and FASTQ [@cock_sanger_2010].
While multiple feature-rich Python bioinformatics libraries exist [@cock_biopython_2009; @noauthor_biocorescikit-bio_2013], they require complex compiled dependencies that can limit their use in non-Unix environments.
Other FASTA/FASTQ specific Python libraries [@pedersen_brentppyfasta_2010; @shirley_efficient_2015; @du_lmdupyfastx_2019] are either outdated or make heavy use of C extensions that prioritize speed over readability and portability. 

fqfa is a pure Python package for working with files in FASTA and FASTQ formats.
It has no dependencies outside of the Python standard library and makes use of newer language features such as type hinting to improve readability.
This makes it more suitable for use in notebooks or projects with simple requirements, as well as easier to understand by novice bioinformaticians and students.

Although it is written in pure Python, fqfa's performance is comparable to modules using C extensions like pyfastx [@du_lmdupyfastx_2019] for tasks such as processing a FASTQ file sequentially.
Timing results and example usage are available as part of the fqfa documentation.

fqfa is released under the BSD 3-Clause License and is available from GitHub and PyPI.

# Acknowledgements

Thank you to Matthew Wakefield for helpful discussion and code review.
The research benefited by support from the Victorian State Government Operational Infrastructure Support and Australian Government NHMRC Independent Research Institute Infrastructure Support.
AFR was supported by the National Human Genome Research Institute of the NIH under award number RM1HG010461.

# References
