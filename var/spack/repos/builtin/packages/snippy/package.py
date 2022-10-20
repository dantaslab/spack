# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Snippy(Package):
    """Rapid haploid variant calling and core genome alignment"""

    homepage = "https://github.com/tseemann/snippy"
    url = "https://github.com/tseemann/snippy/archive/refs/tags/v4.6.0.tar.gz"

    version("4.6.0", sha256="7264e3819e249387effd3eba170ff49404b1cf7347dfa25944866f5aeb6b11c3")

    depends_on("perl@5.18:", type="run")
    depends_on("perl-bioperl@1.7:", type="run")
    depends_on("bwa@0.7.12:", type="run")
    depends_on("minimap2@2.0:", type="run")
    depends_on("samtools@1.7:", type="run")
    depends_on("bcftools@1.7:", type="run")
    depends_on("bedtools2@2.0:", type="run")
    depends_on("parallel", type="run")
    depends_on("freebayes@1.1.0:", type="run")
    depends_on("vcflib@1.0.0:", type="run")
    depends_on("vt@0.577:", type="run")
    depends_on("snpEff@2016-07-04:", type="run")
    depends_on("samclip@0.2:", type="run")
    depends_on("seqtk@1.2:", type="run")
    depends_on("snp-sites@2.0:", type="run")
    depends_on("any2fasta@0.4:", type="run")

    def install(self, spec, prefix):
        install_tree("bin", prefix.bin)
