# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Slirp4netns(AutotoolsPackage):
    """User-mode networking for unprivileged network namespaces"""

    homepage = "https://github.com/rootless-containers/slirp4netns"
    url = "https://github.com/rootless-containers/slirp4netns/archive/v1.1.12.tar.gz"
    maintainers = ["bernhardkaindl"]

    version("1.1.12", sha256="279dfe58a61b9d769f620b6c0552edd93daba75d7761f7c3742ec4d26aaa2962")

    depends_on("autoconf", type="build", when="@1.1.12")
    depends_on("automake", type="build", when="@1.1.12")
    depends_on("libtool", type="build", when="@1.1.12")
    depends_on("pkgconfig", type="build")
    depends_on("glib")
    depends_on("libcap")
    depends_on("libseccomp")
    depends_on("libslirp")
