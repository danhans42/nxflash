# NXFLASH

## Introduction

NXFLASH is a utility for the Sony Playstation. It allows you to flash the EEPROM of a PlayStation cheat cartridge from a CD or via SIO (serial) as well as via parallel using xkiller+xplorer (untested).


It uses a basic serial cable for communication, no handshaking required(just Rx/Tx/Gnd). You can also use an offical Yaroze serial cable or a Sharklink Cable - but I wouldnt bother with those unless you already own one and really want to use an old DB9 serial port.

Main Menu Screenshot

<p align="center">
  <img src="https://github.com/danhans42/nxflash/blob/master/images/screenshot_mainmenu.PNG">
</p>

NXFLASH is built on the source of XFLASH, which was written by Tim Schuerewegen. Thanks to Shadow of PSXDEV.net and Tim for releasing this.  I decided to give it a new name - it basically means 'next xflash'. I believe it needed a new name as the original author may no longer want to be associated with it and to save confusion about client side tool compatibility.

In order to run NXFLASH you will need a way to execute it on a console. I will not cover that here as plenty of guides are out there for mastering bootable PlayStation discs and booting them. Alternatively, you could execute it using your usual code upload method (catflap/psxexe/psxserial etc.).

NXFLASH also has a Python3 based client for uploading/downloading data. It has been tested on Python 3.7 on both Linux and Windows 10.

As well as all the existing features of XFLASH - NXFLASH adds the following :-

* Dump cart EEPROM via Serial
* Dump PSX BIOS via Serial
* Upload/Flash cart EEPROM via Serial
* increased screen width to 640px (from 512).
* increased size of Flash From CD Browser

## Comms Tool - nxflash.py
The nxflash.py is the client side tool for NXFLASH. As well as the supported features of xflash, nxflash.py will also allow you to upload & execute a PSX-EXE to PSXSERIAL/UniROM v4.4/v6. NXFLASH itself does not support EXE upload currently - although it is a future goal. 

nxflash.py requires pyserial - if you dont already have it installed you can install it using pip. Google will help you with this if you get stuck.
NOTE: Please ensure you install pyserial by using pip3 install pyserial (NOT pip3 install serial) . Also, if you have problems with having access to the port, please ensure your username is added to the group 'tty' or 'dialout'.

If you run nxflash.py without any command line arguments, it will give you the command line switches.

**Usage**

nxflash.py *command port file*

*command*
* -ur : upload a ROM to nxflash for flashing.
* -dr : download ROM from nxflash (Copy it to RAM first)
* -db : download PSX BIOS
* -run : upload & execute PSX-EXE (PSXSERIAL/HITSERIAL/UniROM 4.4/v6 compatible)\n\n")

*port*

This is the name of your serial port, and will differ on what platform you run it on. Linux is generally /dev/ttyS0 or /dev/ttyUSB0 or something alone those lines. Windows will be something like COM1 or COM5. I havent tested this on OSX, but assume it will be something like /dev/cu.usbserial.XXXXXXXX

*file*

This is the file you want to read from or write to. WARNING - THIS TOOL WILL OVERWRITE AN EXISTING FILE WITHOUT PROMPTING - BE CAREFUL

**Examples**

* Upload ROM - 'nxflash.py -ur /dev/ttyUSB0 caetla038.bin'
* Download ROM - 'nxflash.py -dr /dev/ttyUSB0 ar_backup.bin'
* Download BIOS -'nxflash.py -db /dev/ttyUSB0 scph1002.bin'
* Upload+Run EXE - 'nxflash.py -run /dev/ttyUSB0 greentro.exe'

## Building a Serial Cable

To buld your own serial cable, purchase a USB UART of your choice and a PlayStation link cable. You will need to cut it in half and use a continuity checker/multimeter to find out which colour corresponds to which pin. Alternatively if you are feeling brave, you can solder one in internally


Pinout for the serial port :-

![Pinout](https://github.com/danhans42/nxflash/blob/master/images/psx_SIO_pinout.png)

You will need to cross over the RXD and TXD lines (ie. PSX TXD to UART RXD), and ground connects straight through.

Fairly simple stuff. As for which USB UART to buy, that is up to you. When writing this I had the occasional timeout issue when using the tools on Linux. The issue turned out to be a fake FTDI UART! Avoid FTDI based adapters unless they are from a reputable source such as Adafruit/Sparkfun etc - avoid eBay/Aliexpress cheap ones.

I have also tested this with the Sil CP210x series UARTS, they have Linux drivers built in. Alternatively a CH340 based adapter will also work. Just make sure they are 3.3v and not 5v.

## Xkiller & Xplorer + Parallel Port

Xflash supported dumping/flashing using a parallel port connection in conjunction with xkiller. This support has been left untouched in NXFLASH. I havent tested it as I dont have a windows machine running with a parallel port. The main point of the features I added is to try and get away from being tied to using a parallel port. I understand that serial isn't faster but when you can upload a ROM and flash it in a few minutes I really dont see a problem. Its left here for those who may want to use a parallel port and xkiller.

## Flashing from CD

If you wish, you can build a bootable NXFLASH CD. The process for this is exactly the same as XFLASH. You will need to combine roms together using the romfile utility. Romfile from the last version of xflash has been included in the archive and a sample SYSTEM.CNF is in the CDFILES folder. To build a FLASH CD do the following :-

1. Create a new folder (eg ROMS)
2. Copy all the ROMs you want on the CD into that folder, ensuring they arent encrypted and have the extenstion .ROM
3. copy the romfile.exe program in there, and run it.
4. You should now have a file called ROMFILE.DAT

Now you need to master a bootable CD image in the correct format. The only three files you will need on your CD are NXFLASH.EXE, ROMFILE.DAT and SYSTEM.CNF

If you don't know how to build a CD, here is one way of doing it.. http://www.psxdev.net/help/cdrom_mastering.html

Consider the below when building a CD - taken from the original XFLASH readme.

*When the program detects an Xplorer ROM file, it will extract information from that file and use that as the ROM description for the X-Flash ROM selection menu*

*When the program detects an non-Xplorer ROM file, it will ask you if it should be added to the romfile and uses the filename without extension as the ROM description for the X-Flash ROM selection menu*

*The current ROM file limit is 128, trying more ROM's will crash both X-Flash & the ROM builder*

A prebuilt romfile.dat that has caetla, xplorer and uniflash can be found in the UniROM v6 archive, see the first post. http://www.psxdev.net/forum/viewtopic.php?t=722 

## Uploading/Flashing via Serial

1. Connect your serial cable to both your PSX and PC.
2. Run NXFLASH on your PlayStation via your chosen method - ensure your EEPROM is correctly detected (not unknown/unsupported).
3. Press TRIANGLE on the pad to go into serial ROM upload.
4. On your machine upload your rom eg. nxflash.py -ru /dev/ttyS0 uniromv66.bin 
5. Once it has successfully uploaded, NXFLASH will return to the main menu. 
6. You will now see the Flash ROM option appear, press X to flash. Then at the warning prompt press O. If there are no error messages the flash was successful.
7. Press O to reboot your console.

## Dump BIOS via Serial

1. Connect your serial cable is connected to both your PSX and PC.
2. Run NXFLASH on your PlayStation via your chosen method - ensure your EEPROM is correctly detected (not unknown/unsupported).
3. Press SQUARE on the pad to go into dump bios to SIO.
4. On your machine upload your rom eg. nxflash.py -bd /dev/ttyS0 psxbios.bin 
5. Once it has successfully downloaded, NXFLASH will return to the main menu. 

## Dump Cheat Cart via Serial

1. Connect your serial cable is connected to both your PSX and PC.
2. Run NXFLASH on your PlayStation via your chosen method - ensure your EEPROM is correctly detected (not unknown/unsupported).
3. Press L2 on the pad to go into dump RAM to SIO.
4. On your machine upload your rom eg. nxflash.py -rd /dev/ttyS0 actionreplaydump.bin 
5. Once it has successfully downloaded, NXFLASH will return to the main menu. 

## Supported EEPROMs

NXFLASH supports the full set of EEPROMs that were supported by the last version of xflash. This list below will (hopefully) grow and new parts will be added to the list along with the corresponding version number support commenced from.

Manufacturer|Model|Size|Added?
------------|-----|----|------
ATMEL| 29C010A |128k|Legacy
ATMEL| 29LV010A|128k|Legacy
ATMEL| 29C020|256k|Legacy
ATMEL| 29BV020|256k|Legacy
ATMEL| 29C040A|512k|Legacy
ATMEL| 29xV040A|512k|Legacy
SST| 29EE010|128k|Legacy
SST| 29xE010|128k|Legacy
SST| 29EE010A|128k|Legacy
SST| 29xE010A|128k|Legacy
SST| 29EE020|256k|Legacy
SST| 29xE020|256k|Legacy
SST| 29EE020A|256k|Legacy
SST| 2xEE020A|256k|Legacy
SST| 28SF040|512k|Legacy
WINBOND| 29EE01x|128k|Legacy
WINBOND| 29C020|256k|Legacy
WINBOND| 29C040|512k|Legacy

## Limitations - !!PLEASE READ!!

* There is NO CRC/CHECKSUM/VERIFICATION 

Currently there are no CRC checks on transmitted/received data and the protocol is very simple. In testing I never once had an issue with transmission errors, but just be careful and ensure you have other means of recovery as a backup (ie from CD). A simple way to validate what you have uploaded is to download it back from RAM, and compare the two files - the only differences should be the file sizes. In testing I did not have a single issue with data upload/download - data always verified 100%

* ROM/BIOS Download

Currently, no matter what flash EEPROM your cart is fitted with nxflash will always download a full 512k. BIOS download is always 512k. You can trim this with a tool of your choice - I have used HXD for this in the past.

* Xplorer FX Cartdridges

Squaresoft74 has identified in testing that the dual banked model of the Xplorer FX currenltly isnt detected correctly by NXFLASH. If you open your FX cart and it has 2 SST29EE020 PLCC32 EEPROMs fitted, it currently wont flash properly. I have attempted to source one of these carts quite a few times but always end up with a single AT29C040 model. If you attempt to flash currently you may end up just flashing the first bank!
## PLEASE DO NOT FLASH DUAL EEPROM XPLORER FX CARTS WITH NXFLASH as they are unsupported. ##

## Future Goals

I will also be looking at adding further features into NXFLASH to make it even more useful - my aspiration is for it to turn into a bit of a multi purpose tool.

* Adding unsupported flash parts (starting with Am29Fxxx series) 
* EXE Upload (PSX Serial Compatible)
* Memory Card Dumping/Reading/Writing
* Overhaul the user interface (colours/fonts/layout)

Ideally I want to keep this application as small as possible - hence the ascii style big text. 

## Thanks

This is a project that I am using to learn more about playstation programming, and C in general. Please take that into consideration and if you find any bugs - drop me a line or open an issue here and I will do my best to get onto it. 

Thanks to Tim S for writing xflash and for releasing the sources and to Shadow of psxdev for organising the release of them. 

Also, big thanks to Hitmen, Sicklebrick, Trimesh, Squaresoft74, Shendo, Lameguy64, orion, Xavi92 and Greg - your posts, published source code and releases have helped massively with my learning of programming on the PSX.

I am always interested to hear of carts/eeproms that are not supported. If you have one please get in touch.

contact: danhans42 at gmail.com

website: psx0.wordpress.com
