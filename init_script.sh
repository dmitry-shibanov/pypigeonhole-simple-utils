source /usr/share/miniconda/bin/activate
conda config --set auto_activate_base true
conda init bash

$CONDA/bin/conda env update --file environment.yaml --name base
$CONDA/bin/conda install flake8
# stop the build if there are Python syntax errors or undefined names
$CONDA/bin/flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
$CONDA/bin/flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

python -m unittest discover -s test