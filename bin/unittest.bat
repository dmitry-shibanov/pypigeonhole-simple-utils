SET WorkDir=%cd%
SET BatchDir="%~dp0"

cd %BatchDir%..
coverage run -m unittest discover -s test
coverage report
cd %WorkDir%
