# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetapod(RPackage):
    """Meta-Analyses on P-Values of Differential Analyses.

    Implements a variety of methods for combining p-values in differential
    analyses of genome-scale datasets. Functions can combine p-values across
    different tests in the same analysis (e.g., genomic windows in ChIP-seq,
    exons in RNA-seq) or for corresponding tests across separate analyses
    (e.g., replicated comparisons, effect of different treatment conditions).
    Support is provided for handling log-transformed input p-values, missing
    values and weighting where appropriate."""

    bioc = "metapod"

    version("1.4.0", commit="e71c2072e5b39f74599e279b28f4da7923b515fb")

    depends_on("r-rcpp", type=("build", "run"))
