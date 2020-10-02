SET WorkDir=%cd%
SET BatchDir=%~dp0
SET ProjDir= %BatchDir%..

call %BatchDir%cleanup.bat

cd %ProjDir%
REM Other options are bdist, bdist_egg
python setup.py bdist_wheel sdist

REM Move this out of source folder.
REM We don't want to delete it in case we need to inspect it.
FOR /d %%G IN ("%ProjDir%\src\*.egg-info") DO MV "%%~G" %ProjDir%
cd %WorkDir%
