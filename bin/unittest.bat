SET WorkDir=%cd%
SET BatchDir="%~dp0"
SET SrcDir= %BatchDir%..\src

cd %SrcDir%..
python -m unittest discover -p "*test.py" -s ..\test
cd %WorkDir%
