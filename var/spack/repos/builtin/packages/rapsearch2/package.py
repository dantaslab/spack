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
#     spack install rapsearch2
#
# You can edit this file again by typing:
#
#     spack edit rapsearch2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Rapsearch2(AutotoolsPackage, SourceforgePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://rapsearch2.sourceforge.net"
    sourceforge_mirror_path = "rapsearch2/RAPSearch2.24_64bits.tar.gz"

    version("2.24", sha256="85db4573f4c768b6c3c73bb44ff2611ba48dc6c8d188feb40f44bf7c55de36ce")

    def url_for_version(self, version):
        url = (
            "https://sourceforge.net/projects/rapsearch2/files/RAPSearch{0}_64bits.tar.gz"
        )
        return url.format(version)

    depends_on("autoconf", type="build", when="build_system=autotools")
    depends_on("automake", type="build", when="build_system=autotools")
    depends_on("libtool", type="build", when="build_system=autotools")

