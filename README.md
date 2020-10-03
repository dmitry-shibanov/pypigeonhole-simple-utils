### Simple Utilities

![Python Package using Conda](https://github.com/psilons/pypigeonhole-simple-utils/workflows/Python%20Package%20using%20Conda/badge.svg)
![Test Coverage](coverage.svg)

Provide convenience for some common tasks, with simplified interfaces.

#### With no external dependencies except Python SDK
___
- email
- logging
- timer
- OS command run
- file system operations
- string manipulations

#### With 3rd party dependencies
___
- encryption_utils needs pycryptodome 
- ftp_client and ssh_client need paramiko and pysocks
- http_client needs requests

If we don't use these modules, then don't need to install the dependencies.


#### Project Setup
Here is the new approach for project setup. Currently, setup.py is for project 
build, not for project setup. We use environment.txt or environment.yaml for
project setup. However, there are duplicated information between the setup.py 
and environment files. Maven is a very matured Java tool to manage Java 
projects. When we compare setup.py and Maven, we find that we miss the scope
information. 

So the dep_setup.py is added for developers to add dependencies with scope
information. The dep_setup.utils.py will generate install_required and
test_required for the setup.py, and generates the environment.yaml as well.

So the project setup is to run the following to generate the environment.yaml.

```python dep_setup.py```

Then set up Python environment with:

```conda env create -file environment.yaml ```

When development is done, run the build

```python setup.py```

In the future, we may extract dep_setup_utils.py to somewhere else.
