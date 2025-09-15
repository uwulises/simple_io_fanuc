import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
message= "StartMotor"
message = "StopMotor"
#message= "SetScrewRpmSetpoint<50>"
addr = ("192.168.1.5", 4711)
client_socket.sendto(message.encode(), addr)
#data, server = client_socket.recvfrom(1024)