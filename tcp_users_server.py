import socket

pool_data = []


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(10)

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        data = client_socket.recv(1024).decode()
        pool_data.append(data)
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

        client_socket.send("\n".join(pool_data).encode())

        client_socket.close()


if __name__ == "__main__":
    server()
