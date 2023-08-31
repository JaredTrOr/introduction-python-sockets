import socket

FORMAT = 'utf-8'
HEADER = 20480

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect(ADDR)
    print('[Cliente] Conexión con cliente exitosa')
except socket.error as e:
    print(f'[Cliente] Hubo un error al realizar la conexión {e}')



print('[Cliente] Esperando ordenes del administrador')

while True:
    try:
        mensaje = cliente.recv(HEADER).decode(FORMAT)
        if mensaje == 'salir':
            continue

        print(mensaje)
    except socket.error as e:
        print(f'[Cliente] Error al recibir la mensajería')
        break

print('[Cliente] Desonexión')

