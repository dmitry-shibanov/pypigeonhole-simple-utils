SET WorkDir=%cd%
SET BatchDir="%~dp0"

REM Need to make sure the test coverage is only for src, not for both src and test
cd %BatchDir%..
REM python -m coverage run -m unittest discover -s test
coverage run -m unittest discover -s test
coverage report

del /s coverage.svg
coverage-badge -o coverage.svg
cd %WorkDir%
