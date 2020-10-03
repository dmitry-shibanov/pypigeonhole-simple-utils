from setuptools import setup, find_packages

import dep_setup

# for dev, cd this folder and run pip install -e .
# for build, python setup.py sdist bdist bdist_wheel
# wheel with -none-any.whl means pure python and any platform
setup(name='pypigeonhole-simple-utils',
      version=0.1,
      description='Python Simple Utilities',
      url='https://github.com/psilons/pypigeonhole-simple-utils',

      author='psilons',
      author_email='***@gmail.com',

      package_dir={'': 'src'},
      packages=find_packages("src", exclude=["test"]),

      python_requires='>=3',

      # install_requires=[],
      #
      # tests_require=[
      #       'pycryptodome==3.9.8',
      #       'requests==2.24.0',
      #       'pyyaml==5.3.1'
      #       'paramiko==2.7.2',
      #       'pysocks==1.7.1'
      # ],
      install_requires=dep_setup. install_required,

      tests_require=dep_setup.test_required,

      extras_require={},
      )
