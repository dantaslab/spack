# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-minpath
#
# You can edit this file again by typing:
#
#     spack edit py-minpath
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Minpath(Package):
    """MinPath (Minimal set of Pathways) is a parsimony approach for biological
    pathway reconstructions using protein family predictions, achieving a more
    conservative, yet more faithful, estimation of the biological pathways for a
    query dataset"""

    homepage = "https://omics.informatics.indiana.edu/MinPath/"
    url = "https://omics.informatics.indiana.edu/mg/get.php?justdoit=yes&software=minpath1.4.tar.gz"

    version("1.4", sha256="665e90b5ee7fa5837d13b1145cdf3eafa691d25c1ce4bb76847dfa771ff24551")
    version("1.2", sha256="f57a7c6a83d5ae366e08069d4b12a7c12fae8aa25d35fea5cfbe75cacbcd04de")

    depends_on("python")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("MinPath{0}.py".format(self.version), prefix.bin)
