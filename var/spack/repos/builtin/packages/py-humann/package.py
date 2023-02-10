# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyHumann(PythonPackage):
    """HUMAnN 3.0 is the next iteration of HUMAnN, the HMP Unified Metabolic
    Analysis Network. HUMAnN is a method for efficiently and accurately
    profiling the abundance of microbial metabolic pathways and other molecular
    functions from metagenomic or metatranscriptomic sequencing data"""

    homepage = "http://huttenhower.sph.harvard.edu/humann"
    pypi = "humann/humann-3.6.tar.gz"

    version("3.6", sha256="addce81db58bacfdd5465423455d25e385aa8dd14349253c3a7054bf7d3747dc")

    variant("rapsearch2", default=False, description="required for translated search using RAPSearch2")
    variant("usearch", default=False, description="required for translated search using Usearch")
    variant("samtools", default=False, description="required for using BAM files as input")
    variant("py-biom-format", default=False, description="required if input or output files are in biom format")

    # https://github.com/biobakery/humann#requirements
    depends_on("py-metaphlan@3.0:", type=("build", "run"))
    # let spack handle bowtie, diamond, and minpath installs
    depends_on("bowtie2@2.2:", type=("build", "run"))
    depends_on("diamond@0.9.24:", type=("build", "run"))
    depends_on("py-minpath@1.2", type=("build", "run"))
    # optional dependencies
    depends_on("rapsearch2@2.21:", when="+rapsearch2")
    depends_on("usearch@7.0:", when="+usearch")
    depends_on("samtools", when="+samtools")
    depends_on("py-biom-format", when="+py-biom-format")
