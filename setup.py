import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fqfa",
    version="0.0.1",
    author="Alan F Rubin",
    author_email="alan.rubin@wehi.edu.au",
    description="A lightweight Python library for handling FASTQ and FASTA files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/varianteffect/fqfa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
