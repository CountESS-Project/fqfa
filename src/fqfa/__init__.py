from fqfa.fasta.fasta import parse_fasta_records, write_fasta_record
from fqfa.fastq.fastq import parse_fastq_reads, parse_fastq_pe_reads
from fqfa.util.file import open_compressed, has_fasta_ext, has_fastq_ext
from fqfa.util.infer import infer_sequence_type, infer_all_sequence_types
from fqfa.util.nucleotide import (
    reverse_complement,
    convert_dna_to_rna,
    convert_rna_to_dna,
)
from fqfa.util.translate import translate_dna, ncbi_genetic_code_to_dict

__all__ = [
    "parse_fasta_records",
    "write_fasta_record",
    "parse_fastq_reads",
    "parse_fastq_pe_reads",
    "open_compressed",
    "has_fasta_ext",
    "has_fastq_ext",
    "infer_sequence_type",
    "infer_all_sequence_types",
    "reverse_complement",
    "convert_dna_to_rna",
    "convert_rna_to_dna",
    "translate_dna",
    "ncbi_genetic_code_to_dict",
]
