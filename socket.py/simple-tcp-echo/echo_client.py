# coding=utf8
import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_to_sent = 'hello tcp socket'
    try:
        sock.connect(('127.0.0.1', 8080))

        sent = sock.send(data_to_sent)
        print(sock.recv(1024))
    finally:
        sock.close()
        print('socket closed')