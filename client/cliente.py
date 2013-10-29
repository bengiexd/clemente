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
#  
import socket
import sys
import threading

class Cliente(threading.Thread):
	""" ClassName Cliente
    	Clase cliente para interactuar con el servidor
	"""
	mensaje = "Bienvenido Cliente"
	activado = 1
    
	def __init__(self, ip, port):
		"""Class __init__
			Esta clase nos ayuda a crear un cliente 
			tiene como parametros ir y port 
			para establecer conexion con el servidor.
		"""
		threading.Thread.__init__(self)
		try:
			# Instanciamos un objeto de la clase Socalo
			self.Socalo = socket.socket()
			# Nos conectamos con el servidor utilizando ip y port del servidor
			self.Socalo.connect((str(ip), int(port)))
		except Exception, ex:
			print "No se puede establecer la comunicacion"
			exit(0)
		

	def run(self):		
		while self.activado:
			pass
		print "cliente desconectado"
		return
			
	def Stop(self):
		self.activado = 0
		self.Socalo.close()				
			
	def Recived(self):
		return self.Socalo.recv(1024)


	def Send(self,mensaje):
		self.Socalo.send(mensaje)	
		return self.Socalo.recv(1024)



					
									
		
