# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Rapsearch2(Package, SourceforgePackage):
    """RAPSearch2 is a tool for fast protein similarity searches"""

    homepage = "https://rapsearch2.sourceforge.net"
    sourceforge_mirror_path = "rapsearch2/RAPSearch2.24_64bits.tar.gz"

    version("2.24", sha256="85db4573f4c768b6c3c73bb44ff2611ba48dc6c8d188feb40f44bf7c55de36ce")

    # the "64bits" messes with spack's url parsing
    def url_for_version(self, version):
        url = (
            "https://sourceforge.net/projects/rapsearch2/files/RAPSearch{0}_64bits.tar.gz"
        )
        return url.format(version)

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install_tree("bin", prefix.bin)
