#!/bin/bash

# Check if initialsetup.py.old exists
if [ -f "initialsetup.py.old" ]; then
    # Run firmware.py with Python 3
    python3 firmware.py
else
    # Run initialsetup.py with Python 3
    python3 initialsetup.py
fi

