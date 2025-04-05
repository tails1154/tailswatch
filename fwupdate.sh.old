echo Updating Firmware
echo DONT SHUT DOWN THE DEVICE
echo Backing up firmware...
cp firmware.py firmware.py.old
#Scary!
rm -rf firmware.py
echo Downloading Updater...
git clone https://github.com/tails1154/tailswatch
cd tailswatch
cp updater.sh ..
cd ..
rm -rf tailswatch
chmod +rwx updater.sh
echo Starting updater...
./updater.sh
rm -rf updater.sh
echo Firmware Updated!
exit
