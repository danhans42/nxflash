# NXFLASH
## Introduction

NXFLASH is built on the source of XFLASH, which was written by Tim Schuerewegen. Thanks to Shadow of PSXDEV.net and Tim for releasing this.  I decided to give it a new name - it basically means 'next xflash'. I believe it needed a new name as the original author may no longer want to be associated with it and to save confusion about client side tool compatibility.

NXFLASH is a utility for the Sony Playstation. It allows you to dump/flash the EEPROM of a cheat cartridge. In order to run NXFLASH you will need a way to execute it on a console. I will not cover that here as plenty of guides are out there for mastering bootable PlayStation discs. Alternatively, you could execute it using your usual code upload method (catflap/psxexe etc.).

NXFLASH also has a Python3 based client for uploading/downloading data. It has been tested on Python 3.7 on both Linux and Windows 10.

As well as all the existing features of XFLASH - NXFLASH adds the following features :-

* Dump cart EEPROM via Serial
* Dump PSX BIOS via Serial
* Upload/Flash cart EEPROM via Serial
* increased screen width to 640px (from 512).
* increased size of Flash From CD Browser


## nxflash.py
The nxflash.py is the client side tool for NXFLASH. As well as the supported features of xflash, nxflash.py will also allow you to upload & execute a PSX-EXE to PSXSERIAL/UniROM v4.4/v6. NXFLASH itself does not support EXE upload currently - although it is a future goal.

**Commands**

* -ru : upload a ROM to nxflash for flashing.\n")
* -rd : download ROM from nxflash.\n")
* -bd : download PSX BIOS.\n")
* -re : upload & execute PSX-EXE (PSXSERIAL/HITSERIAL/UniROM 4.4/v6 compatible)\n\n")

**Usage**

**nxflash.py** *command port file*

**Examples**

* Upload ROM - 'nxflash.py -ru /dev/ttyUSB0 caetla038.bin'
* Download ROM - 'nxflash.py -rd /dev/ttyUSB0 ar_backup.bin'
* Download BIOS -'nxflash.py -rb /dev/ttyUSB0 scph1002.bin'
* Upload+Run EXE - 'nxflash.py -re /dev/ttyUSB0 greentro.exe'




