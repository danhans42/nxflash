#!/usr/bin/env python3
# nxflash.py beta 9 - download/upload tool for nxflash.
#
# * upload a ROM to nxflash for flashing
# * download ROM from nxflash
# * download PSX BIOS 
# * run EXE (hitserial/psxserial compatible)
#
# Runs on Python 3.7 - requires the pyserial libaries to be installed (do this via PyPi/pip)
# by @danhans42 (instag/twitter/psxdev/@gmail.com)

import sys
import serial
import os
import time
from time import sleep

args = int(len(sys.argv))
dumpsize = 524288 #temp - will become an option

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('- %s Data [%s] %s%s %s\r' % (stat,bar, percents, '%', status))
    sys.stdout.flush()

def usage():
	sys.stdout.write("   usage :  nxflash.py <command> <port> <file>\n\n")
	sys.stdout.write("commands\n")
	sys.stdout.write("     -ur  : upload a ROM to nxflash for flashing.\n")
	sys.stdout.write("     -dr  : download ROM from nxflash.\n")
	sys.stdout.write("     -db  : download PSX BIOS.\n")
	sys.stdout.write("     -run : upload & execute PSX-EXE (PSXSERIAL compatible)\n\n")
	sys.stdout.write("where <port> is the name of your serial port and <file> is the name of the file to upload/download\n\n")
	sys.stdout.write("      eg  : nxflash.py -ur /dev/ttyUSB0 caetla038.bin\n")
	sys.stdout.write("            nxflash.py -dr COM5 ar_backup.bin\n")

def romupload():
	#get serialport name
	serialport = sys.argv[2]
	#get filename from commandline
	filename = sys.argv[3]
	#get size of file
	filesize = os.path.getsize(filename)
	#convert filesize into bytearray
	fsz = (filesize).to_bytes(4, byteorder='little',signed=True)
	#open file and read as binary
	inputfile = open(filename, 'rb')
	inputfile.seek(0, 0)
	sys.stdout.write("Command    : upload ROM\n")
	sys.stdout.write("Port       : ")
	sys.stdout.write(serialport)
	sys.stdout.write("\nROM File   : {}\n".format(filename))
	sys.stdout.write("Rom Size   : {} bytes [".format(filesize))
	sys.stdout.write(hex(filesize))
	sys.stdout.write("h]\n")
	#open serial port
	ser = serial.Serial(serialport,115200)
	#send sync byte (lowercase ascii 'r' or 0x72h)
	ser.write(b'\x72')
	sys.stdout.write('\n- Sending Sync\n')
	sleep(1.0)
	ser.write(fsz)
	sys.stdout.write("- Sending Filesize [")
	sys.stdout.write(hex(filesize))
	sys.stdout.write("h]\n")
	sleep(2.0)
	byte = 0
	while byte < filesize:
		inputfile.seek(byte,0)
		bin = inputfile.read(1)
		ser.write(bin)
		byte += 1
		progress(byte, filesize, status='')
	sys.stdout.write('\n- Operation Complete\n')

def biosdownload():
	serialport = sys.argv[2]
	binfile = sys.argv[3]
	ser = serial.Serial(serialport,115200)
	inputfile = open(binfile,'wb')
	packet = 0
	sys.stdout.write("Command   : Download BIOS\n")
	sys.stdout.write("Port      : ")
	sys.stdout.write(serialport)
	sys.stdout.write("\nFilename  : {}\n".format(binfile))
	sys.stdout.write("\n")
	ser.write(b'\x62')
	sys.stdout.write("\n- Sending Sync\n")
	buffer = bytearray()
	packetmax = (524288/2048)
	while packet < packetmax:
		buffer = buffer+ser.read(2048)
		progress(packet, packetmax-1, status='')
		packet += 1
	inputfile.write(buffer)
	sys.stdout.write("\n- File Saved")
	inputfile.close()
	sys.stdout.write('\n- Operation Complete\n')

def romdownload():
	serialport = sys.argv[2]
	binfile = sys.argv[3]
	ser = serial.Serial(serialport,115200)
	inputfile = open(binfile,'wb')
	packet = 0
	sys.stdout.write("Command    : Download ROM\n")
	sys.stdout.write("Port       : ")
	sys.stdout.write(serialport)
	sys.stdout.write("\nFilename   : {}\n".format(binfile))
	sys.stdout.write("\n")
	ser.write(b'\x72')
	sys.stdout.write("\n- Sending Sync\n")
	buffer = bytearray()
	packetmax = (dumpsize/2048)
	while packet < packetmax:
		buffer = buffer+ser.read(2048)
		progress(packet, packetmax-1, status='')
		packet += 1
	inputfile.write(buffer)
	sys.stdout.write("\n- File Saved")
	inputfile.close()
	sys.stdout.write('\n- Operation Complete\n')

def uploadexe():
	serialport = sys.argv[2]
	filename = sys.argv[3]
	filesize = os.path.getsize(filename)
	inputfile = open(filename, 'rb')
	inputfile.seek(0, 0)
	header = inputfile.read(2048)
	inputfile.seek(16,0)
	pc = inputfile.read(4)
	inputfile.seek(24,0)
	addr= inputfile.read(4)
	inputfile.seek(28,0)
	fsz = inputfile.read(4)
	blockcount = int (filesize /2048)
	sys.stdout.write("Port       : ")
	sys.stdout.write(serialport)
	sys.stdout.write("\nEXE Name   : {}\n".format(filename))
	sys.stdout.write("EXE Size   : {} bytes\n\n".format(filesize))
	cont = 'y'
	if cont != 'y':
		quit()
	else:
		ser = serial.Serial(serialport,115200,writeTimeout = 1)
		ser.write(b'\x63')
		sys.stdout.write('- Sending Sync\n')
		sleep(2.0)
		ser.write(header)
		sys.stdout.write('- Sending Header\n')
		sleep(0.1)
		ser.write(pc)
		sys.stdout.write('- Sending Init PC\n')
		sleep(0.1)
		ser.write(addr)
		sys.stdout.write('- Sending Addr\n')
		sleep(0.1)
		ser.write(fsz)
		sys.stdout.write('- Sending Filesize\n')
		packet = 1
		offset = 2048
		while packet < blockcount:
			inputfile.seek(packet*2048,0)
			bin = inputfile.read(2048)
			progress(packet, blockcount-1, status='')
			ser.write(bin)
			offset += 2048
			packet += 1
		EOF = 0
		while EOF < 2048:
			ser.write(b'\xFF')
			EOF += 1
		sys.stdout.write('\n- Executing')
		sys.stdout.write('\n- Operation Complete\n')

#main

		
sys.stdout.write('\nnxflash.py Beta 9 - by @danhans42\n\n')

if args < 4:
	sys.stdout.write("error: insufficient parameters\n\n")
	usage()
	
else:
	command = sys.argv[1]
	serialport = sys.argv[2]
	file = sys.argv[3]
	
	if command == "-ur":
		stat = "Uploading" 
		romupload()
	elif command == "-dr":
		stat = "Downloading" 
		romdownload()
	elif command == "-db":
		stat = "Downloading" 
		biosdownload()
	elif command == "-run":
		stat = "Uploading"
		uploadexe()
	else:
		sys.stdout.write("error: invalid command\n\n")
		usage()
	
	
	