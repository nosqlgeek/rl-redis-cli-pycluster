export MYPY_ENV=env_pycluster

## Make sure VirtualEnv is installed
pip install virtualenv

## Create a new Python VirtualEnv if not existing
if [ ! -d "$MYPY_ENV" ]; then
   virtualenv $MYPY_ENV
fi

## Activate the new VirtualEnv
source "$MYPY_ENV/bin/activate"

## Install Deps
pip install click
pip install redis==2.10.6
pip install redis-py-cluster==1.3.6

## Install PyInstaller
pip install pyinstaller

## Package
pyinstaller redis-cli-pycluster.py
WD=$PWD
cd dist
tar -cvf redis-cli-pycluster.tar redis-cli-pycluster
mv redis-cli-pycluster.tar $WD
cd $WD

## Test
./dist/redis-cli-pycluster/redis-cli-pycluster --help


## Clean
./clean.bash
