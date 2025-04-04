echo Updating Firmware
echo DONT SHUT DOWN THE DEVICE
echo Backing up firmware...
cp firmware.py firmware.py.old
#Scary!
rm -rf firmware.py
echo Downloading Updater...
wget http://10.0.0.25/tailswatch/updater.sh
chmod +rwx updater.sh
echo Starting updater...
./updater.sh
rm -rf updater.sh
echo Firmware Updated!
exit
