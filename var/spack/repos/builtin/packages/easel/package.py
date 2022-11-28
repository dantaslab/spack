# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Easel(AutotoolsPackage):
    """Easel is an ANSI C code library developed
    by the Eddy/Rivas laboratory at Harvard"""

    homepage = "https://github.com/EddyRivasLab/easel"
    url = "https://github.com/EddyRivasLab/easel/archive/refs/tags/easel-0.48.tar.gz"

    version("0.48", sha256="c5d055acbe88fa834e81424a15fc5fa54ac787e35f2ea72d4ffd9ea2c1aa29cf")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
