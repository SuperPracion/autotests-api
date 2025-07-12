import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 12345))
client_socket.send("Привет, сервер!".encode())

response = client_socket.recv(1024).decode()
print(response)

client_socket.close()
