#!/usr/bin/env python
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    #Inicializa automatizacion para el manejo de usuarios virtuales
    authorizer = DummyAuthorizer()

    #Se define un usuario master con privilegios de lectura y escritura
    #Se define un usuario anonimo con privilegios de solo lectura
    authorizer.add_user('master','password', os.getcwd(), perm='elradfmwM')
    authorizer.add_anonymous(os.getcwd())

    #Manejador de instancias FTP
    handler = FTPHandler
    handler.authorizer = authorizer

    #Establece la direccion y puerto del servidor FTP
    address = ('127.0.0.1', 21)
    server = FTPServer(address, handler)

    #Establece un limite de conexiones
    server.max_cons = 256
    server.max_cons_per_ip = 5

    #Inicia el servidor FTP
    server.serve_forever()

if __name__ == '__main__':
    main()
