from dep_setup_utils import CONDA, Dependency, INSTALL
import dep_setup_utils

CONDA.env = 'py385_psu'
CONDA.channels = ['defaults']

dependent_libs = [
    Dependency(name='python', version='==3.8.5', scope=INSTALL, installer=CONDA),
    Dependency(name='coverage', version='==5.3', installer=CONDA, desc='test coverage'),  # DEV
    Dependency(name='requests', version='==2.24.0', installer=CONDA, desc='required by http_client'),
    Dependency(name='pycryptodome', version='==3.9.8', installer=CONDA),
    Dependency(name='paramiko', version='==2.7.2', installer=CONDA),
    Dependency(name='pysocks', version='==1.7.1', installer=CONDA),
    Dependency(name='pyyaml', version='==5.3.1', installer=CONDA),

    Dependency(name='pipdeptree'),  # latest version, DEV, PIP
    Dependency(name='coverage-badge'),
]

install_required = dep_setup_utils.get_install_required(dependent_libs)

test_required = dep_setup_utils.get_test_required(dependent_libs)

if __name__ == "__main__":
    dep_setup_utils.gen_conda_yaml(dependent_libs)
