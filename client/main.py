#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 valentin basel <valentin@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import socket
import sys
from clemente_client import Interface


def HELP():
	print " ------------------------"
	print " - Help Clemente Server -"
	print " ------------------------"
	print
	print "-ip : specified ip of Clemente Server"
	print "-p  : specified port of Clemente Server"
	print 

def VERSION():
	print "clemente-client version 1.0.1"

def main():

	_port = None
	_ip = None
	_arg={"-h": HELP, "-v":VERSION, "-p":_port, "-ip":_ip}	
	arguments = sys.argv
	if len(arguments)>1:
		play = 0
		for nroArg in range(1,len(arguments)):			
			if play:
				play = 0
			else:
				parameter = arguments[nroArg]
				if _arg.has_key(parameter):
					if parameter == "-p":
						_port = arguments[nroArg+1]
						play =1
					elif parameter == "-ip":
						_ip = arguments[nroArg+1]
						play =1
					elif parameter == "-h" or parameter == "-v":
						_arg[parameter]()
						exit()
				else:
					print "unknown parameter", parameter
					print "main.py -h for Help"
					return

	#servidor = Server(ip=_ip,port=_port)
	GUI = Interface()
	if _ip:
		GUI.set_ip_server(_ip)
	if _port:
		GUI.set_port_server(_port)
	GUI.main()
	return 0

if __name__ == '__main__':
	main()

