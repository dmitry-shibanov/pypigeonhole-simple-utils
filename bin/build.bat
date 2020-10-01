SET WorkDir=%cd%
SET BatchDir="%~dp0"

call %BatchDir%cleanup.bat

cd %BatchDir%..
python setup.py bdist bdist_wheel sdist
cd %WorkDir%
