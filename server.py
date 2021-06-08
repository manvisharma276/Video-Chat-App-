import socket
import cv2
import pickle
import struct

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 9999
socket_address = ('192.168.29.27',port)
print("Socket Created")
server_socket.bind(socket_address)
server_socket.listen()
print("LISTENING AT:", socket_address)

while True:
    client_socket,addr = server_socket.accept()
    print('GOT CONNECTION FORM:', addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a))+a
            client_socket.sendall(message)
            
            cv2.imshow('TRANSMITTING VIDEO', frame)
            if cv2.waitKey(1) ==13:
                cv2.destoryAllWindows()
                client_socket.close()
                break