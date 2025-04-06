#!/bin/bash

cd /home/tails1154/tailswatch || exit 1

while true; do
    choice=$(kdialog --menu "TailsWatch Menu" \
        1 "Start TailsWatch" \
        2 "Play music" \
        3 "Logout" \
        4 "Update Firmware"          )

    case $choice in
        1)
            python3 firmware.py
            ;;
        2)
            kdialog --msgbox "Playing music.mp3"
            cvlc --play-and-exit music.mp3 &
            kdialog --msgbox "Press OK to stop music"
            killall vlc
            ;;
        3)
            kdialog --msgbox "Logging out..."
            exit 0
            ;;
        4)
            kdialog --msgbox "Press OK to update firmware"
            ./fwupdate.sh
            kdialog --msgbox "./fwupdate.sh completed!"
            ;;
        *)
            # If user closes the dialog or presses cancel
            exit 0
            ;;
    esac
done
