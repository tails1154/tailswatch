#!/bin/bash


# make temp dir and cd into it
mkdir temp && cd temp

# run git clone on the tailswatch repo

git clone https://github.com/tails1154/tailswatch

# cd into new dir that it made

cd tailswatch

# copy everything into the .. dir

cp -r * ..

# cd ..

cd ..

# rm -rf the tailswatch dir

rm -rf tailswatch

# copy old firmware.py

cp ../firmware.py ../firmware.py.old

# copy new firmware.py

cp firmware.py ../firmware.py

# cd ..

cd ..

# rm -rf the temp dir

rm -rf temp


# exit with success

exit 0
