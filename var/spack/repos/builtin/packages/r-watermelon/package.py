# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RWatermelon(RPackage):
    """Illumina 450 methylation array normalization and metrics.

    15 flavours of betas and three performance metrics, with methods for
    objects produced by methylumi and minfi packages."""

    bioc = "wateRmelon"

    version('2.0.0', commit='f6a331bdf50e0e5c94009fb67be873d996348ade')
    version('1.34.0', commit='3fa2745535c22068a438747b41b9d793196098d4')
    version('1.30.0', commit='66d7579fe49206d965832288df7937c3d43ed578')

    depends_on('r@2.10:', type=('build', 'run'))
    depends_on('r@3.5.0:', type=('build', 'run'), when='@2.0.0:')
    depends_on('r-biobase', type=('build', 'run'))
    depends_on('r-limma', type=('build', 'run'))
    depends_on('r-matrixstats', type=('build', 'run'))
    depends_on('r-methylumi', type=('build', 'run'))
    depends_on('r-lumi', type=('build', 'run'))
    depends_on('r-roc', type=('build', 'run'))
    depends_on('r-illuminahumanmethylation450kanno-ilmn12-hg19', type=('build', 'run'))
    depends_on('r-illuminaio', type=('build', 'run'))
