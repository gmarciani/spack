# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack import *


class PyTorch(PythonPackage, CudaPackage):
    """Tensors and Dynamic neural networks in Python
    with strong GPU acceleration."""

    homepage = "https://pytorch.org/"
    git      = "https://github.com/pytorch/pytorch.git"

    maintainers = ['adamjstewart']

    # Exact set of modules is version- and variant-specific, just attempt to import the
    # core libraries to ensure that the package was successfully installed.
    import_modules = ['torch', 'torch.autograd', 'torch.nn', 'torch.utils']

    version('master', branch='master', submodules=True)
    version('1.11.0', tag='v1.11.0', submodules=True)
    version('1.10.2', tag='v1.10.2', submodules=True)
    version('1.10.1', tag='v1.10.1', submodules=True)
    version('1.10.0', tag='v1.10.0', submodules=True)
    version('1.9.1', tag='v1.9.1', submodules=True)
    version('1.9.0', tag='v1.9.0', submodules=True)
    version('1.8.2', tag='v1.8.2', submodules=True)
    version('1.8.1', tag='v1.8.1', submodules=True)
    version('1.8.0', tag='v1.8.0', submodules=True)
    version('1.7.1', tag='v1.7.1', submodules=True)
    version('1.7.0', tag='v1.7.0', submodules=True)
    version('1.6.0', tag='v1.6.0', submodules=True)
    version('1.5.1', tag='v1.5.1', submodules=True)
    version('1.5.0', tag='v1.5.0', submodules=True)
    version('1.4.1', tag='v1.4.1', submodules=True)
    version('1.3.1', tag='v1.3.1', submodules=True)
    version('1.3.0', tag='v1.3.0', submodules=True)
    version('1.2.0', tag='v1.2.0', submodules=True)
    version('1.1.0', tag='v1.1.0', submodules=True)
    version('1.0.1', tag='v1.0.1', submodules=True, deprecated=True)
    version('1.0.0', tag='v1.0.0', submodules=True, deprecated=True)

    is_darwin = sys.platform == 'darwin'

    # All options are defined in CMakeLists.txt.
    # Some are listed in setup.py, but not all.
    variant('caffe2', default=True, description='Build Caffe2', when='@1.7:')
    variant('test', default=False, description='Build C++ test binaries')
    variant('cuda', default=not is_darwin, description='Use CUDA')
    variant('rocm', default=False, description='Use ROCm')
    variant('cudnn', default=not is_darwin, description='Use cuDNN', when='+cuda')
    variant('fbgemm', default=True, description='Use FBGEMM (quantized 8-bit server operators)')
    variant('kineto', default=True, description='Use Kineto profiling library', when='@1.8:')
    variant('magma', default=not is_darwin, description='Use MAGMA', when='+cuda')
    variant('metal', default=is_darwin, description='Use Metal for Caffe2 iOS build')
    variant('nccl', default=True, description='Use NCCL', when='+cuda platform=linux')
    variant('nccl', default=True, description='Use NCCL', when='+cuda platform=cray')
    variant('nccl', default=True, description='Use NCCL', when='+rocm platform=linux')
    variant('nccl', default=True, description='Use NCCL', when='+rocm platform=cray')
    variant('nnpack', default=True, description='Use NNPACK')
    variant('numa', default=True, description='Use NUMA', when='platform=linux')
    variant('numa', default=True, description='Use NUMA', when='platform=cray')
    variant('numpy', default=True, description='Use NumPy')
    variant('openmp', default=True, description='Use OpenMP for parallel code')
    variant('qnnpack', default=True, description='Use QNNPACK (quantized 8-bit operators)')
    variant('valgrind', default=True, description='Use Valgrind', when='@1.8: platform=linux')
    variant('valgrind', default=True, description='Use Valgrind', when='@1.8: platform=cray')
    variant('xnnpack', default=True, description='Use XNNPACK', when='@1.5:')
    variant('mkldnn', default=True, description='Use MKLDNN')
    variant('distributed', default=not is_darwin, description='Use distributed')
    variant('mpi', default=not is_darwin, description='Use MPI for Caffe2', when='+distributed')
    variant('gloo', default=not is_darwin, description='Use Gloo', when='+distributed')
    variant('tensorpipe', default=not is_darwin, description='Use TensorPipe', when='@1.6: +distributed')
    variant('onnx_ml', default=True, description='Enable traditional ONNX ML API', when='@1.5:')
    variant('breakpad', default=True, description='Enable breakpad crash dump library', when='@1.9:')

    conflicts('+cuda+rocm')
    conflicts('+breakpad', when='target=ppc64:')
    conflicts('+breakpad', when='target=ppc64le:')

    conflicts('cuda_arch=none', when='+cuda',
              msg='Must specify CUDA compute capabilities of your GPU, see '
              'https://developer.nvidia.com/cuda-gpus')

    # Required dependencies
    depends_on('cmake@3.13:', when='@1.11:', type='build')
    depends_on('cmake@3.10:', when='@1.10:', type='build')
    depends_on('cmake@3.5:', type='build')
    # Use Ninja generator to speed up build times, automatically used if found
    depends_on('ninja@1.5:', when='@1.1:', type='build')
    # See python_min_version in setup.py
    depends_on('python@3.7:', when='@1.11:', type=('build', 'link', 'run'))
    depends_on('python@3.6.2:', when='@1.7.1:', type=('build', 'link', 'run'))
    depends_on('python@3.6.1:', when='@1.6:1.7.0', type=('build', 'link', 'run'))
    depends_on('python@3.5:', when='@1.5', type=('build', 'link', 'run'))
    depends_on('python@2.7:2,3.5:', when='@1.4', type=('build', 'link', 'run'))
    depends_on('python@2.7:2,3.5:3.7', when='@:1.3', type=('build', 'link', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-future', when='@1.5:', type=('build', 'run'))
    depends_on('py-future', when='@1.1: ^python@:2', type=('build', 'run'))
    depends_on('py-pyyaml', type=('build', 'run'))
    depends_on('py-typing', when='^python@:3.4', type=('build', 'run'))
    depends_on('py-pybind11@2.6.2', when='@1.8:', type=('build', 'link', 'run'))
    depends_on('py-pybind11@2.3.0', when='@1.1:1.7', type=('build', 'link', 'run'))
    depends_on('py-pybind11@2.2.4', when='@:1.0', type=('build', 'link', 'run'))
    depends_on('py-dataclasses', when='@1.7: ^python@3.6', type=('build', 'run'))
    depends_on('py-tqdm', type='run')
    # https://github.com/onnx/onnx#prerequisites
    depends_on('py-numpy@1.16.6:', type=('build', 'run'))
    depends_on('py-protobuf@3.12.2:', when='@1.10:', type=('build', 'run'))
    depends_on('py-protobuf@:3.14', when='@:1.9', type=('build', 'run'))
    depends_on('protobuf@3.12.2:', when='@1.10:')
    depends_on('protobuf@:3.14', when='@:1.9')
    depends_on('py-typing-extensions@3.6.2.1:', when='@1.7:', type=('build', 'run'))
    depends_on('blas')
    depends_on('lapack')
    depends_on('eigen')
    # https://github.com/pytorch/pytorch/issues/60329
    # depends_on('cpuinfo@2020-12-17', when='@1.8:')
    # depends_on('cpuinfo@2020-06-11', when='@1.6:1.7')
    # https://github.com/shibatch/sleef/issues/427
    # depends_on('sleef@3.5.1_2020-12-22', when='@1.8:')
    # https://github.com/pytorch/pytorch/issues/60334
    # depends_on('sleef@3.4.0_2019-07-30', when='@1.6:1.7')
    # https://github.com/Maratyszcza/FP16/issues/18
    # depends_on('fp16@2020-05-14', when='@1.6:')
    depends_on('pthreadpool@2021-04-13', when='@1.9:')
    depends_on('pthreadpool@2020-10-05', when='@1.8')
    depends_on('pthreadpool@2020-06-15', when='@1.6:1.7')
    depends_on('psimd@2020-05-17', when='@1.6:')
    depends_on('fxdiv@2020-04-17', when='@1.6:')
    depends_on('benchmark', when='@1.6:+test')

    # Optional dependencies
    # https://discuss.pytorch.org/t/compiling-1-10-1-from-source-with-gcc-11-and-cuda-11-5/140971
    depends_on('cuda@9.2:', when='@1.11:+cuda', type=('build', 'link', 'run'))
    depends_on('cuda@9.2:11.4', when='@1.6:1.10+cuda', type=('build', 'link', 'run'))
    depends_on('cuda@9:11.4', when='@1.1:1.5+cuda', type=('build', 'link', 'run'))
    depends_on('cuda@7.5:11.4', when='@:1.0+cuda', type=('build', 'link', 'run'))
    depends_on('cudnn@6:7', when='@:1.0+cudnn')
    depends_on('cudnn@7.0:7', when='@1.1:1.5+cudnn')
    depends_on('cudnn@7:', when='@1.6:+cudnn')
    depends_on('magma', when='+magma')
    depends_on('nccl', when='+nccl')
    depends_on('numactl', when='+numa')
    depends_on('llvm-openmp', when='%apple-clang +openmp')
    depends_on('valgrind', when='+valgrind')
    # https://github.com/pytorch/pytorch/issues/60332
    # depends_on('xnnpack@2021-02-22', when='@1.8:+xnnpack')
    # depends_on('xnnpack@2020-03-23', when='@1.6:1.7+xnnpack')
    depends_on('mpi', when='+mpi')
    # https://github.com/pytorch/pytorch/issues/60270
    # depends_on('gloo@2021-05-04', when='@1.9:+gloo')
    # depends_on('gloo@2020-09-18', when='@1.7:1.8+gloo')
    # depends_on('gloo@2020-03-17', when='@1.6+gloo')
    # https://github.com/pytorch/pytorch/issues/60331
    # depends_on('onnx@1.8.0_2020-11-03', when='@1.8:+onnx_ml')
    # depends_on('onnx@1.7.0_2020-05-31', when='@1.6:1.7+onnx_ml')
    depends_on('mkl', when='+mkldnn')

    # Test dependencies
    depends_on('py-hypothesis', type='test')
    depends_on('py-six', type='test')
    depends_on('py-psutil', type='test')

    # Fix BLAS being overridden by MKL
    # https://github.com/pytorch/pytorch/issues/60328
    patch('https://github.com/pytorch/pytorch/pull/59220.patch?full_index=1',
          sha256='6d5717267f901e8ee493dfacd08734d9bcc48ad29a76ca9ef702368e96bee675',
          when='@1.2:')

    # Fixes build on older systems with glibc <2.12
    patch('https://github.com/pytorch/pytorch/pull/55063.patch?full_index=1',
          sha256='2229bcbf20fbe88aa9f7318f89c126ec7f527875ffe689a763c78abfa127a65c',
          when='@1.1:1.8.1')

    # Fixes CMake configuration error when XNNPACK is disabled
    # https://github.com/pytorch/pytorch/pull/35607
    # https://github.com/pytorch/pytorch/pull/37865
    patch('xnnpack.patch', when='@1.5')

    # Fixes build error when ROCm is enabled for pytorch-1.5 release
    patch('rocm.patch', when='@1.5+rocm')

    # Fixes fatal error: sleef.h: No such file or directory
    # https://github.com/pytorch/pytorch/pull/35359
    # https://github.com/pytorch/pytorch/issues/26555
    # patch('sleef.patch', when='@:1.5')

    # Fixes compilation with Clang 9.0.0 and Apple Clang 11.0.3
    # https://github.com/pytorch/pytorch/pull/37086
    patch('https://github.com/pytorch/pytorch/commit/e921cd222a8fbeabf5a3e74e83e0d8dfb01aa8b5.patch?full_index=1',
          sha256='0f3ad037a95af9d34b1d085050c1e7771fd00f0b89e5b3a276097b7c9f4fabf8',
          when='@1.1:1.5')

    # Removes duplicate definition of getCusparseErrorString
    # https://github.com/pytorch/pytorch/issues/32083
    patch('cusparseGetErrorString.patch', when='@:1.0^cuda@10.1.243:')

    # Fixes 'FindOpenMP.cmake'
    # to detect openmp settings used by Fujitsu compiler.
    patch('detect_omp_of_fujitsu_compiler.patch', when='%fj')

    # Fixes to build with fujitsu-ssl2
    patch('fj-ssl2_1.11.patch', when='@1.11:^fujitsu-ssl2')
    patch('fj-ssl2_1.10.patch', when='@1.10^fujitsu-ssl2')
    patch('fj-ssl2_1.9.patch', when='@1.9^fujitsu-ssl2')
    patch('fj-ssl2_1.8.patch', when='@1.8^fujitsu-ssl2')
    patch('fj-ssl2_1.6-1.7.patch', when='@1.6:1.7^fujitsu-ssl2')
    patch('fj-ssl2_1.3-1.5.patch', when='@1.3:1.5^fujitsu-ssl2')
    patch('fj-ssl2_1.2.patch', when='@1.2^fujitsu-ssl2')

    # Fix compilation of +distributed~tensorpipe
    # https://github.com/pytorch/pytorch/issues/68002
    patch('https://github.com/pytorch/pytorch/commit/c075f0f633fa0136e68f0a455b5b74d7b500865c.patch?full_index=1',
          sha256='41271e494a3a60a65a8dd45ac053d1a6e4e4d5b42c2dac589ac67524f61ac41e', when='@1.10.0+distributed~tensorpipe')

    @property
    def libs(self):
        # TODO: why doesn't `python_platlib` work here?
        root = join_path(
            self.prefix, self.spec['python'].package.platlib, 'torch', 'lib'
        )
        return find_libraries('libtorch', root)

    @property
    def headers(self):
        # TODO: why doesn't `python_platlib` work here?
        root = join_path(
            self.prefix, self.spec['python'].package.platlib, 'torch', 'include'
        )
        headers = find_all_headers(root)
        headers.directories = [root]
        return headers

    @when('@1.5.0:')
    def patch(self):
        # https://github.com/pytorch/pytorch/issues/52208
        filter_file('torch_global_deps PROPERTIES LINKER_LANGUAGE C',
                    'torch_global_deps PROPERTIES LINKER_LANGUAGE CXX',
                    'caffe2/CMakeLists.txt')

    def setup_build_environment(self, env):
        """Set environment variables used to control the build.

        PyTorch's ``setup.py`` is a thin wrapper around ``cmake``.
        In ``tools/setup_helpers/cmake.py``, you can see that all
        environment variables that start with ``BUILD_``, ``USE_``,
        or ``CMAKE_``, plus a few more explicitly specified variable
        names, are passed directly to the ``cmake`` call. Therefore,
        most flags defined in ``CMakeLists.txt`` can be specified as
        environment variables.
        """
        def enable_or_disable(variant, keyword='USE', var=None, newer=False):
            """Set environment variable to enable or disable support for a
            particular variant.

            Parameters:
                variant (str): the variant to check
                keyword (str): the prefix to use for enabling/disabling
                var (str): CMake variable to set. Defaults to variant.upper()
                newer (bool): newer variants that never used NO_*
            """
            if var is None:
                var = variant.upper()

            # Version 1.1.0 switched from NO_* to USE_* or BUILD_*
            # But some newer variants have always used USE_* or BUILD_*
            if self.spec.satisfies('@1.1:') or newer:
                if '+' + variant in self.spec:
                    env.set(keyword + '_' + var, 'ON')
                elif '~' + variant in self.spec:
                    env.set(keyword + '_' + var, 'OFF')
            else:
                if '+' + variant in self.spec:
                    env.unset('NO_' + var)
                elif '~' + variant in self.spec:
                    env.set('NO_' + var, 'ON')

        # Build in parallel to speed up build times
        env.set('MAX_JOBS', make_jobs)

        # Spack logs have trouble handling colored output
        env.set('COLORIZE_OUTPUT', 'OFF')

        enable_or_disable('test', keyword='BUILD')
        enable_or_disable('caffe2', keyword='BUILD')

        enable_or_disable('cuda')
        if '+cuda' in self.spec:
            # cmake/public/cuda.cmake
            # cmake/Modules_CUDA_fix/upstream/FindCUDA.cmake
            env.unset('CUDA_ROOT')
            torch_cuda_arch = ';'.join('{0:.1f}'.format(float(i) / 10.0) for i
                                       in
                                       self.spec.variants['cuda_arch'].value)
            env.set('TORCH_CUDA_ARCH_LIST', torch_cuda_arch)

        enable_or_disable('rocm')

        enable_or_disable('cudnn')
        if '+cudnn' in self.spec:
            # cmake/Modules_CUDA_fix/FindCUDNN.cmake
            env.set('CUDNN_INCLUDE_DIR', self.spec['cudnn'].prefix.include)
            env.set('CUDNN_LIBRARY', self.spec['cudnn'].libs[0])

        enable_or_disable('fbgemm')
        enable_or_disable('kineto')
        enable_or_disable('magma')
        enable_or_disable('metal')
        enable_or_disable('breakpad')

        enable_or_disable('nccl')
        if '+nccl' in self.spec:
            env.set('NCCL_LIB_DIR', self.spec['nccl'].libs.directories[0])
            env.set('NCCL_INCLUDE_DIR', self.spec['nccl'].prefix.include)

        # cmake/External/nnpack.cmake
        enable_or_disable('nnpack')

        enable_or_disable('numa')
        if '+numa' in self.spec:
            # cmake/Modules/FindNuma.cmake
            env.set('NUMA_ROOT_DIR', self.spec['numactl'].prefix)

        # cmake/Modules/FindNumPy.cmake
        enable_or_disable('numpy')
        # cmake/Modules/FindOpenMP.cmake
        enable_or_disable('openmp', newer=True)
        enable_or_disable('qnnpack')
        enable_or_disable('qnnpack', var='PYTORCH_QNNPACK')
        enable_or_disable('valgrind')
        enable_or_disable('xnnpack')
        enable_or_disable('mkldnn')
        enable_or_disable('distributed')
        enable_or_disable('mpi')
        # cmake/Modules/FindGloo.cmake
        enable_or_disable('gloo', newer=True)
        enable_or_disable('tensorpipe')

        if '+onnx_ml' in self.spec:
            env.set('ONNX_ML', 'ON')
        elif '~onnx_ml' in self.spec:
            env.set('ONNX_ML', 'OFF')

        if not self.spec.satisfies('@master'):
            env.set('PYTORCH_BUILD_VERSION', self.version)
            env.set('PYTORCH_BUILD_NUMBER', 0)

        # BLAS to be used by Caffe2
        # Options defined in cmake/Dependencies.cmake and cmake/Modules/FindBLAS.cmake
        if self.spec['blas'].name == 'atlas':
            env.set('BLAS', 'ATLAS')
            env.set('WITH_BLAS', 'atlas')
        elif self.spec['blas'].name in ['blis', 'amdblis']:
            env.set('BLAS', 'BLIS')
            env.set('WITH_BLAS', 'blis')
        elif self.spec['blas'].name == 'eigen':
            env.set('BLAS', 'Eigen')
        elif self.spec['lapack'].name in ['libflame', 'amdlibflame']:
            env.set('BLAS', 'FLAME')
            env.set('WITH_BLAS', 'FLAME')
        elif self.spec['blas'].name in [
                'intel-mkl', 'intel-parallel-studio', 'intel-oneapi-mkl']:
            env.set('BLAS', 'MKL')
            env.set('WITH_BLAS', 'mkl')
            # help find MKL
            if self.spec['mkl'].name == 'intel-oneapi-mkl':
                env.set('INTEL_MKL_DIR', self.spec['mkl'].prefix.mkl.latest)
            else:
                env.set('INTEL_MKL_DIR', self.spec['mkl'].prefix.mkl)
        elif self.spec['blas'].name == 'openblas':
            env.set('BLAS', 'OpenBLAS')
            env.set('WITH_BLAS', 'open')
        elif self.spec['blas'].name == 'veclibfort':
            env.set('BLAS', 'vecLib')
            env.set('WITH_BLAS', 'veclib')
        elif self.spec['blas'].name == 'fujitsu-ssl2':
            env.set('BLAS', 'SSL2')
            env.set('WITH_BLAS', 'ssl2')
        else:
            env.set('BLAS', 'Generic')
            env.set('WITH_BLAS', 'generic')

        # Don't use vendored third-party libraries when possible
        env.set('BUILD_CUSTOM_PROTOBUF', 'OFF')
        env.set('USE_SYSTEM_NCCL', 'ON')
        env.set('USE_SYSTEM_EIGEN_INSTALL', 'ON')
        env.set('pybind11_DIR', self.spec['py-pybind11'].prefix)
        env.set('pybind11_INCLUDE_DIR',
                self.spec['py-pybind11'].prefix.include)
        if self.spec.satisfies('@1.10:'):
            env.set('USE_SYSTEM_PYBIND11', 'ON')
        # https://github.com/pytorch/pytorch/issues/60334
        # if self.spec.satisfies('@1.8:'):
        #     env.set('USE_SYSTEM_SLEEF', 'ON')
        if self.spec.satisfies('@1.6:'):
            # env.set('USE_SYSTEM_LIBS', 'ON')
            # https://github.com/pytorch/pytorch/issues/60329
            # env.set('USE_SYSTEM_CPUINFO', 'ON')
            # https://github.com/pytorch/pytorch/issues/60270
            # env.set('USE_SYSTEM_GLOO', 'ON')
            # https://github.com/Maratyszcza/FP16/issues/18
            # env.set('USE_SYSTEM_FP16', 'ON')
            env.set('USE_SYSTEM_PTHREADPOOL', 'ON')
            env.set('USE_SYSTEM_PSIMD', 'ON')
            env.set('USE_SYSTEM_FXDIV', 'ON')
            env.set('USE_SYSTEM_BENCHMARK', 'ON')
            # https://github.com/pytorch/pytorch/issues/60331
            # env.set('USE_SYSTEM_ONNX', 'ON')
            # https://github.com/pytorch/pytorch/issues/60332
            # env.set('USE_SYSTEM_XNNPACK', 'ON')

    @run_before('install')
    def build_amd(self):
        if '+rocm' in self.spec:
            python(os.path.join('tools', 'amd_build', 'build_amd.py'))

    @run_after('install')
    @on_package_attributes(run_tests=True)
    def install_test(self):
        with working_dir('test'):
            python('run_test.py')
