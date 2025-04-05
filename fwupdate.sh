echo Updating Firmware
echo DONT SHUT DOWN THE DEVICE
echo Backing up firmware...
cp firmware.py firmware.py.old
#Scary!
rm -rf firmware.py
echo Downloading Updater...
git clone https://github.com/tails1154/tailswatch
mkdir tailswatch
cd tailswatch
cp updater.sh ..
./updater.sh
cd ..
rm -rf tailswatch
chmod +rwx updater.sh
echo Starting updater...
# ./updater.sh
rm -rf updater.sh
# Check if the firmware still exists
ls firmware.py && echo Firmware Updated! && exit 0
# If we reach here, copy the old firmware
echo Rolling back...
cp firmware.py.old firmware.py
echo Firmware Update Failed, Restored old firmware.
exit



