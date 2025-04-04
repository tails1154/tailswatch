echo OEM setup
rm -rf ship
rm -rf firmware.py*
mv initialsetup.py.old initialsetup.py
ln initialsetup.py firmware.py
mkdir ship
cp initialsetup.py ship
cp firmware.py ship
cp fwupdate.sh ship
cp initial.sh ship
echo OEM setup complete
