# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyDeepsigBiocomp(PythonPackage):
    """DeepSig - Predictor of signal peptides
    in proteins based on deep learning"""

    homepage = "https://deepsig.biocomp.unibo.it"

    url = "https://github.com/BolognaBiocomp/deepsig/archive/refs/tags/v1.2.5.tar.gz"

    version("1.2.5", sha256="e954b815d63c221c564c7d3fe27123d7cd2c39b191d6107369ab095d506496e0")

    depends_on("python@3.8", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-biopython@1.78:", type=("build", "run"))
    depends_on("py-tensorflow@2.2.0", type=("build", "run"))
