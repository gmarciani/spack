# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Maq(AutotoolsPackage):
    """Maq is a software that builds mapping assemblies from short reads
    generated by the next-generation sequencing machines."""

    homepage = "http://maq.sourceforge.net/"
    url = "https://downloads.sourceforge.net/project/maq/maq/0.7.1/maq-0.7.1.tar.bz2"
    list_url = "https://sourceforge.net/projects/maq/files/maq/"

    version("0.7.1", sha256="e1671e0408b0895f5ab943839ee8f28747cf5f55dc64032c7469b133202b6de2")
    version("0.5.0", sha256="c292c19baf291b2415b460d687d43a71ece00a7d178cc5984bc8fc30cfce2dfb")

    conflicts("%gcc@4.7.0:", when="@0.7.1")
