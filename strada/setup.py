from setuptools import setup
from setuptools.extension import Extension
import numpy as np

extensions = [
    Extension(
        "strada/_caffe_wrapper.cpp",
        libraries=["caffe"],
        library_dirs=['../build/lib'],
        include_dirs=['../include', np.get_include()],
    )
]


setup(
    name='strada',
    description="Python bindings for caffe, named after the cafe in berkeley",
    author_email='',
    version="1.0",
    packages=['strada'],
    install_requires=[
        "Cython>=0.19.2",
        "numpy>=1.7.1",
        "scipy>=0.13.2",
        "scikit-image>=0.9.3",
        "matplotlib>=1.3.1",
        "ipython>=3.0.0",
        "h5py>=2.2.0",
        "leveldb>=0.191",
        "networkx>=1.8.1",
        "nose>=1.3.0",
        "pandas>=0.12.0",
        "python-dateutil>=1.4,<2",
        "protobuf>=2.5.0",
        "python-gflags>=2.0",
        "pyyaml>=3.10",
        "Pillow>=2.3.0",
        "six>=1.1.0",
    ],
    dependency_links=[
        'http://edge.artifactory.yahoo.com:8000/artifactory/pypi/vision.ioutils/',
        'http://edge.artifactory.yahoo.com:8000/artifactory/pypi/vision.face/'
    ],
    zip_safe=False,
)
