import socket
import Crypto
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

BLOCK_SIZE = 32

def encrypto(message):
        raw = AES.new(b'thetestkey123456', AES.MODE_CBC, b'thetestIV1234567')
        encrypted_msg = raw.encrypt(pad(message, BLOCK_SIZE))

        return encrypted_msg


# hard code private IP of linux box
ip = '192.168.1.191'
port = 10000
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

message = input("Enter path to source file(s): ")
stream_file = open(message, "rb")
stream = stream_file.read(1024)

print(stream)

stream = encrypto(stream)

print(stream)

while(stream):
        s.send(stream)
        stream = stream_file.read(1024)
            
s.close()
