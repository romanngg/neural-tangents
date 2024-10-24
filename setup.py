# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Setup the package with pip."""

import os
import setuptools


# https://packaging.python.org/guides/making-a-pypi-friendly-readme/
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()


INSTALL_REQUIRES = [
    'jax>=0.4.34',
    'frozendict>=2.4.6',
    'tensorflow>=2.16.2',
    'keras>=3.6.0',
    'tf2jax>=0.3.6',
]


TESTS_REQUIRES = [
    'more-itertools>=10.5.0',
    'tensorflow-datasets>=4.9.6',
    'flax>=0.10.0',
]


def _get_version() -> str:
  """Returns the package version.

  Adapted from:
  https://github.com/deepmind/tf2jax/blob/41ea640c7525ed42f7dcd02937b1f308f8949521/setup.py#L24

  Returns:
    Version number.
  """
  current_dir = os.path.dirname(os.path.abspath(__file__))

  with open(os.path.join(current_dir, 'neural_tangents', '__init__.py')) as fp:
    for line in fp:
      if line.startswith('__version__') and '=' in line:
        version = line[line.find('=') + 1:].strip(' \'"\n')
        if version:
          return version
    raise ValueError('`__version__` not found in `neural_tangents/__init__.py`')


setuptools.setup(
    name='neural-tangents',
    version=_get_version(),
    license='Apache 2.0',
    author='Neural Tangents',
    author_email='neural-tangents-dev@google.com',
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'testing': TESTS_REQUIRES,
    },
    url='https://github.com/google/neural-tangents',
    download_url='https://pypi.org/project/neural-tangents/',
    project_urls={
        'Source Code':
            'https://github.com/google/neural-tangents',

        'Paper':
            'https://arxiv.org/abs/1912.02803',

        'Finite Width NTK paper':
            'https://arxiv.org/abs/2206.08720',

        'Video':
            'https://iclr.cc/virtual_2020/poster_SklD9yrFPS.html',

        'Finite Width NTK video':
            'https://youtu.be/8MWOhYg89fY?t=10984',

        'Documentation':
            'https://neural-tangents.readthedocs.io/en/latest/?badge=latest',

        'Bug Tracker':
            'https://github.com/google/neural-tangents/issues',

        'Release Notes':
            'https://github.com/google/neural-tangents/releases',

        'PyPi':
            'https://pypi.org/project/neural-tangents/',

        'Linux Tests':
            'https://github.com/google/neural-tangents/actions/workflows/linux.yml',

        'macOS Tests':
            'https://github.com/google/neural-tangents/actions/workflows/macos.yml',

        'Pytype':
            'https://github.com/google/neural-tangents/actions/workflows/pytype.yml',

        'Coverage':
            'https://app.codecov.io/gh/google/neural-tangents'
    },
    packages=setuptools.find_packages(exclude=('presentation',)),
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='Fast and Easy Infinite Neural Networks in Python',
    python_requires='>=3.10',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Development Status :: 4 - Beta',
    ])
