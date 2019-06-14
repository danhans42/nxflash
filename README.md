# NXFLASH

NXFLASH is a utility for the Sony Playstation. It allows you to dump/flash the EEPROM of a cheat cartridge from CD/SIO (serial) as well as via parallel using xkiller (untested)

## Introduction

NXFLASH is built on the source of XFLASH, which was written by Tim Schuerewegen. Thanks to Shadow of PSXDEV.net and Tim for releasing this.  I decided to give it a new name - it basically means 'next xflash'. I believe it needed a new name as the original author may no longer want to be associated with it and to save confusion about client side tool compatibility.

In order to run NXFLASH you will need a way to execute it on a console. I will not cover that here as plenty of guides are out there for mastering bootable PlayStation discs and booting them. Alternatively, you could execute it using your usual code upload method (catflap/psxexe/psxserial etc.).

NXFLASH also has a Python3 based client for uploading/downloading data. It has been tested on Python 3.7 on both Linux and Windows 10.

As well as all the existing features of XFLASH - NXFLASH adds the following features :-

* Dump cart EEPROM via Serial
* Dump PSX BIOS via Serial
* Upload/Flash cart EEPROM via Serial
* increased screen width to 640px (from 512).
* increased size of Flash From CD Browser


## nxflash.py
The nxflash.py is the client side tool for NXFLASH. As well as the supported features of xflash, nxflash.py will also allow you to upload & execute a PSX-EXE to PSXSERIAL/UniROM v4.4/v6. NXFLASH itself does not support EXE upload currently - although it is a future goal. 

nxflash.py requires pyserial - if you dont already have it installed you can install it using pip. Google will help you with this if youo get stuck

**nxflash.py usage**

nxflash.py *command port file*
* -ru : upload a ROM to nxflash for flashing.\n")
* -rd : download ROM from nxflash.\n")
* -bd : download PSX BIOS.\n")
* -re : upload & execute PSX-EXE (PSXSERIAL/HITSERIAL/UniROM 4.4/v6 compatible)\n\n")

**Examples**

* Upload ROM - 'nxflash.py -ru /dev/ttyUSB0 caetla038.bin'
* Download ROM - 'nxflash.py -rd /dev/ttyUSB0 ar_backup.bin'
* Download BIOS -'nxflash.py -rb /dev/ttyUSB0 scph1002.bin'
* Upload+Run EXE - 'nxflash.py -re /dev/ttyUSB0 greentro.exe'

## Xplorer + Parallel Port

Xflash supported dumping/flashing using a parallel port connection in conjunction with xkiller. This support has been left untouched in NXFLASH. I havent tested it as I dont have a windows machine running with a parallel port.

## Flashing from CD

If you wish, you can build a bootable NXFLASH CD. The process for this is exactly the same as XFLASH. You will need to combine roms together using the romfile utility.This is included with xflash - see here to obtain an older version http://www.psxdev.net/forum/download/file.php?id=74

## Uploading/Flashing via Serial

1. Connect your serial cable is connected to both your PSX and PC.
2. Run NXFLASH on your PlayStation via your chosen method - ensure your EEPROM is correctly detected (not unknown/unsupported).
3. Press TRIANGLE on the pad to go into serial ROM upload.
4. On your machine upload your rom eg. nxflash.py -ru /dev/ttyS0 uniromv66.bin 
5. Once it has successfully uploaded, NXFLASH will return to the main menu. 
6. You will now see the Flash ROM option appear, press X to flash. If there are no error messages the flash was successful.
7. Reboot your console.

## Dump BIOS via Serial

1. Connect your serial cable is connected to both your PSX and PC.
2. Run NXFLASH on your PlayStation via your chosen method - ensure your EEPROM is correctly detected (not unknown/unsupported).
3. Press SQUARE on the pad to go into dump bios to SIO.
4. On your machine upload your rom eg. nxflash.py -bd /dev/ttyS0 psxbios.bin 
5. Once it has successfully downloaded, NXFLASH will return to the main menu. 

## Dump Cheat Cart via Serial

1. Connect your serial cable is connected to both your PSX and PC.
2. Run NXFLASH on your PlayStation via your chosen method - ensure your EEPROM is correctly detected (not unknown/unsupported).
3. Press SQUARE on the pad to go into dump bios to SIO.
4. On your machine upload your rom eg. nxflash.py -rd /dev/ttyS0 actionreplaydump.bin 
5. Once it has successfully downloaded, NXFLASH will return to the main menu. 

## Limitations

* There is NO CRC/CHECKSUM/VERIFICATION 

Currently there are no CRC checks on transmitted/received data and the protocol is very simple. In testing I never once had an issue with transmission errors, but just be careful and ensure you have other means to flash as a contingency.

* ROM/BIOS Download

Currently, no matter what flash EEPROM your cart is fitted with nxflash will always download a full 512k. You can then trim this down. I will address this in future versions. BIOS download is always 512k

## EEPROM Support

NXFLASH supports the full set of EEPROMs that were supported by the last version of xflash. 

Manufacturer|Model|Size
------------|-----|----
ATMEL| 29C010A |128k
ATMEL| 29LV010A|128k
ATMEL| 29C020|256k
ATMEL| 29BV020|256k
ATMEL| 29C040A|512k
ATMEL| 29xV040A|512k
SST| 29EE010|128k
SST| 29xE010|128k
SST| 29EE010A|128k
SST| 29xE010A|128k
SST| 29EE020|256k
SST| 29xE020|256k
SST| 29EE020A|256k
SST| 2xEE020A|256k
SST| 28SF040|512k
WINBOND| 29EE01x|128k
WINBOND| 29C020|256k
WINBOND| 29C040|512k

## Thanks

This is a project that I am using to learn more about playstation programming, and C in general. Please take that into consideration and if you find any bugs - drop me a line or open an issue here and I will do my best to get onto it. 

Thanks to Tim S for writing xflash and for releasing the sources and to the members of PSXDEV.net.

## Future Goals

I will also be looking at adding further features into NXFLASH to make it even more useful - my aspiration is for it to turn into a bit of a multi purpose tool.

* Variable EEPROM size download (client initiated - 128/256/512k)
* Adding unsupported flash parts (starting with Am29Fxxx series) 
* EXE Upload (PSX Serial Compatible)
* Memory Card Dumping/Reading/Writing
* Overhaul the user interface/colours/fonts

contact: danhans42 at gmail.com
website: psx0.wordpress.com






