# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Coin3d(AutotoolsPackage):
    """Coin is an OpenGL-based, 3D graphics library that has its roots in the
    Open Inventor 2.1 API, which Coin still is compatible with."""

    homepage = "https://github.com/coin3d/coin"
    url = "https://github.com/coin3d/coin/archive/Coin-4.0.0.tar.gz"

    version("3.1.0", sha256="70dd5ef39406e1d9e05eeadd54a5b51884a143e127530876a97744ca54173dc3")
    version("3.0.0", sha256="d5c2eb0ecaa5c83d93daf0e9e275e58a6a8dfadc74c873d51b0c939011f81bfa")
    version("2.0.0", sha256="6d26435aa962d085b7accd306a0b478069a7de1bc5ca24e22344971852dd097c")

    depends_on("boost@1.45.0:", type="build")
    depends_on("doxygen", when="+html", type="build")
    depends_on("perl", when="+html", type="build")
    depends_on("glu", type="link")
    depends_on("gl", type="link")
    depends_on("libsm", type="link")
    depends_on("libxext", type="link")
    depends_on("libice", type="link")
    depends_on("uuid", type="link")
    depends_on("libxcb", type="link")
    depends_on("libxau", type="link")

    variant("html", default=False, description="Build and install Coin HTML documentation")
    variant("man", default=False, description="Build and install Coin man pages")

    variant("framework", default=False, description="Do 'UNIX-style' installation on Mac OS X")
    variant("shared", default=True, description="Build shared library (off: build static library)")
    variant("debug", default=False, description="Make debug build")
    variant("symbols", default=False, description="Enable debug symbols")

    def configure_args(self):
        args = []
        args += self.enable_or_disable("framework")
        args += self.enable_or_disable("shared")
        args += self.enable_or_disable("html")
        args += self.enable_or_disable("man")
        args += self.enable_or_disable("symbols")
        args += self.enable_or_disable("debug")
        args.append("--with-boost=" + self.spec["boost"].prefix)
        args.append("--with-boost-libdir=" + self.spec["boost"].prefix.lib)

        return args
