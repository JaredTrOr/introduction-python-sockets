import socket

HEADER = 20480
FORMAT = 'utf-8'

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect(ADDR)
    print('[Cliente] Conexión exitosa con el servidor :)')

except socket.error as e:
    print(f'[Cliente] Hubo un error al realizar la conexión con el servidor {e}')

while True:
    try:
        intruccion_del_servidor = cliente.recv(HEADER).decode(FORMAT)
        print(intruccion_del_servidor)

    except socket.error as e:
        print(f'[Cliente] Hubo un error al recibir la mensajeria')

