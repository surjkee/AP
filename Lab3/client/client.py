from socket import *
import sys

host = 'localhost'
port = 25015
addr = (host,port)
tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(addr)

def sendtoserver(command):
    data = command

    #str.encode - перекодирует введенные данные в байты, bytes.decode - обратно
    data = str.encode(data)
    tcp_socket.send(data)
    data = bytes.decode(data)
    data = bytes.decode(tcp_socket.recv(1024))
    return data    

def close_connection():
    tcp_socket.close()

def kill_server(password):
    if(password=="12345"):
        sendtoserver('shutdown')
        close_connection()
    else:
        print("wrong password")
