@echo off
rem step 1: build pacakge
echo .
echo Building package... (you have updated setup.py parameters, right?)
echo .
set name=oyb

rem step 2: copy package contents
echo .
echo Copying package contents (except build/) into this directory...
echo .
mkdir %name%
xcopy .. %name% > NUL
xcopy ..\data %name%\data\ /e > NUL
xcopy ..\docs %name%\docs\ /e > NUL
xcopy ..\test %name%\test\ /e > NUL
copy ..\README.rst . > NUL

rem step 3: test/build/register/publish
echo .
echo Testing, building, registering, and publishing package...
echo .
python setup.py test
python setup.py sdist --format=targz
python setup.py register
python setup.py sdist --format=targz upload

rem step 4: clean up
echo .
echo Removing build artifacts
echo .
rmdir dist /S /Q
rmdir %name% /S /Q
rmdir %name%.egg-info /S /Q
del README.rst

rem step 5: there is no step 5
echo .
echo Done!
echo .
