# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack.build_environment import MakeExecutable, determine_number_of_jobs
from spack.package import *


class Rosetta(Package):
    """The Rosetta software suite includes algorithms for computational modeling
    and analysis of protein structures. It has enabled notable scientific
    advances in computational biology, including de novo protein design, enzyme
    design, ligand docking, and structure prediction of biological
    macromolecules and macromolecular complexes."""

    homepage = "https://www.rosettacommons.org/"
    url = "file://{0}/rosetta_src_{1}_bundle.tgz".format(os.getcwd(), version)
    manual_download = True

    version("3.13", "00b8ee6dfafcefc1b9502bd41f952d59")
    version("3.12", "d20a9e5c97f2759723e517cdaa85fb7c")

    depends_on("python", type="build")
    depends_on("scons", type="build")

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            self.python("scons.py", "-j {0}".format(jobs), "mode=release", "bin")
