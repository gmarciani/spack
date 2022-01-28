# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyBiomFormat(PythonPackage):
    """The BIOM file format (canonically pronounced biome) is designed to be
    a general-use format for representing biological sample by observation
    contingency tables."""

    pypi = "biom-format/biom-format-2.1.6.tar.gz"

    version("2.1.10", sha256="f5a277a8144f0b114606852c42f657b9cfde44b3cefa0b2638ab1c1d5e1d0488")
    version("2.1.9", sha256="18a6e4d4b4b2a6bf2d5544fa357ad168bedeac93f0837015ef9c72f41fa89491")
    version("2.1.7", sha256="b47e54282ef13cddffdb00aea9183a87175a2372c91a915259086a3f444c42f4")
    version("2.1.6", sha256="8eefc275a85cc937f6d6f408d91b7b45eae854cd5d1cbda411a3af51f5b49b0d")

    depends_on("python@2.7:", type=("build", "run"))
    depends_on("python@3:", type=("build", "run"), when="@2.1.9:")
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-cython@0.29:", type="build")
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-click", type=("build", "run"), when="@2.1.5:")
    depends_on("py-numpy@1.9.2:", type=("build", "run"))
    depends_on("py-future@0.16.0:", type=("build", "run"))
    depends_on("py-scipy@1.3.1:", type=("build", "run"))
    depends_on("py-pandas@0.20.0:", type=("build", "run"))
    depends_on("py-six@1.10.0:", type=("build", "run"))
    depends_on("py-pyqi", type=("build", "run"), when="^python@:2")
