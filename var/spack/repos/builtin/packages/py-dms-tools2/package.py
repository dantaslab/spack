# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyDmsTools2(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    pypi = "dms_tools2/dms_tools2-2.6.12.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    version("2.6.12", sha256="1300cdfae6856674039dc36bfa05a17c962a187d5d0e8f37ba63087e373e9a86")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-attrs@17.4.0:", type=("build","run"))
    depends_on("py-biopython@1.68:", type=("build","run"))
    depends_on("py-pysam@0.13:", type=("build","run"))
    depends_on("py-pandas@0.23:0.25.3", type=("build","run"))
    depends_on("py-numpy@1.16:1.19.5", type=("build","run"))
    depends_on("py-ipython@5.1:", type=("build","run"))
    depends_on("py-jupyter@1.0.0:", type=("build","run"))
    depends_on("py-matplotlib@2.1.1:3.2.2", type=("build","run"))
    depends_on("py-plotnine@0.3:0.6", type=("build","run"))
    depends_on("py-mizani@:0.6", type=("build","run"))
    depends_on("py-natsort@5.0.3:", type=("build","run"))
    depends_on("py-pystan@2.19", type=("build","run"))
    depends_on("py-scipy@1.0:", type=("build","run"))
    depends_on("py-seaborn@0.8:", type=("build","run"))
    depends_on("py-phydms@2.4.1:", type=("build","run"))
    depends_on("py-statsmodels@0.8:", type=("build","run"))
    depends_on("py-regex@2.4.153:", type=("build","run"))
    depends_on("py-packaging", type=("build","run"))
    depends_on("py-umi-tools@1.0.0:", type=("build","run"))
