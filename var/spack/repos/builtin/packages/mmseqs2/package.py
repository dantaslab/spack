# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Mmseqs2(CMakePackage):
    """MMseqs2 (Many-against-Many sequence searching) is a software suite to
    search and cluster huge protein and nucleotide sequence sets"""

    homepage = "https://github.com/soedinglab/MMseqs2"
    url = "https://github.com/soedinglab/MMseqs2/archive/refs/tags/14-7e284.tar.gz"

    version("14-7e284", sha256="a15fd59b121073fdcc8b259fc703e5ce4c671d2c56eb5c027749f4bd4c28dfe1")

    variant("openmp", default=True, description="build with OpenMP support")
    variant("mpi", default=False, description="build with MPI support")

    depends_on("zstd")
    depends_on("llvm-openmp", when="+openmp")
    depends_on("mpi", when="+mpi")

    def cmake_args(self):
        spec = self.spec
        args = []
        # use spack-installed zstd
        args.append("-DUSE_SYSTEM_ZSTD=1")
        if "~openmp" in spec:
            args.append("-DREQUIRE_OPENMP=0")
        if "~mpi" in spec:
            args.append("-DHAVE_MPI=0")
        return args
