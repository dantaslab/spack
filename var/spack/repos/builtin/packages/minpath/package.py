# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Minpath(Package):
    """MinPath (Minimal set of Pathways) is a parsimony approach for biological
    pathway reconstructions using protein family predictions, achieving a more
    conservative, yet more faithful, estimation of the biological pathways for a
    query dataset"""

    homepage = "https://omics.informatics.indiana.edu/MinPath/"
    git = "https://github.com/mgtools/MinPath.git"

    # versions 1.5+ are hosted on GitHub
    version("1.6", commit="46d3e81a4dca2310d558bea970bc002b15d44767")
    version("1.5", commit="8745150d61b4670876e2728800ca549fdd9e0747")

    depends_on("python")

#    def install(self, spec, prefix):
#        mkdirp(prefix.bin)
#        install("MinPath{0}.py".format(self.version), prefix.bin)
