SET WorkDir=%cd%
SET BatchDir="%~dp0"

cd %BatchDir%..
REM python -m coverage run -m unittest discover -s test
coverage run -m unittest discover -s test
coverage report
cd %WorkDir%
