#kdialog --sorry "Apps coming soon!"
#python3 apps.py
cd $(pwd)/apps
python3 $(kdialog --getopenfilename $(pwd)/apps)
