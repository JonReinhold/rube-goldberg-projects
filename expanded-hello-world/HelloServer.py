from subprocess import call
import socket
import sys
import time

connect = 1
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = time.time() + 60

server_address = ('192.168.1.191', 10000)
print('starting server on {} port {}'.format(*server_address))

sock.bind(server_address)
sock.listen(1)

while connect > 0:
        print('waiting for a connection')
        connection, client_address = sock.accept()

        try:
                print('connection from', client_address)
                while True:
                        if time.time() > timeout:
                                connect -= 1
                                raise StopIteration
                        data = connection.recv(1024)
                        print('received {!r}'.format(data))
                        connect -= 1
                        raise StopIteration


        except StopIteration: pass

print("Goodbye")
connection.close()


with open('stream_file.c', 'w') as stream_file:
        stream_file.write(data)


call(["gcc", "stream_file.c"])
