SET BatchDir="%~dp0"
SET ProjDir= %BatchDir%..

echo Project Folder: %ProjDir%

RMDIR /Q /S %ProjDir%build

RMDIR /Q /S %ProjDir%dist

RMDIR /Q /S %ProjDir%src\pypigeonhole-simple-utils.egg-info
