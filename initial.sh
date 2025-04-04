echo Initial Setup
echo DO NOT CLOSE
cp initialsetup.py initialsetup.py.old
rm -rf initialsetup.py
#ln initialsetup.py firmware.py
./fwupdate.sh
ln firmware.py initialsetup.py
exit
