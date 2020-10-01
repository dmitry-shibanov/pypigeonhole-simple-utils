from setuptools import setup, find_packages

# for dev, cd this folder and run pip install -e .
# for build, python setup.py sdist bdist bdist_wheel
# wheel with -none-any.whl means pure python and any platform
setup(name='pypigeonhole-simple-utils',
      version=0.1,
      description='Python Simple Utilities',
      url='https://github.com/psilons/pypigeonhole-simple-utils',

      package_dir={'': 'src'},
      packages=find_packages("src", exclude=["test"]),

      python_requires='>=3',
      )
