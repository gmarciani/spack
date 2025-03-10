# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RBigalgebra(RPackage):
    """'BLAS' and 'LAPACK' Routines for Native R Matrices and 'big.matrix'
    Objects.

    Provides arithmetic functions for R matrix and 'big.matrix' objects as well
    as functions for QR factorization, Cholesky factorization, General
    eigenvalue, and Singular value decomposition (SVD). A method matrix
    multiplication and an arithmetic method -for matrix addition, matrix
    difference- allows for mixed type operation -a matrix class object and a
    big.matrix class object- and pure type operation for two big.matrix class
    objects."""

    cran = "bigalgebra"

    version('1.0.1', sha256='ff7e261d0aa0e0f498e926d923ac62fc5cb783fa1f74bb2ff76a09167388a9d2')
    version('1.0.0', sha256='f186b603bd660be0cc5b7a52c943e23e92fef264f0bc96a8858e38df6cfc4085')
    version('0.8.4.2', sha256='29962468cbfa6416f8628563d5ed8c9f76089190311ff1c618f099ee8d9eea75')

    depends_on('r-bigmemory@4.0.0:', type=('build', 'run'))
    depends_on('r-bh', type=('build', 'run'))
    depends_on('r-rcpp', type=('build', 'run'), when='@1.0.0:')
