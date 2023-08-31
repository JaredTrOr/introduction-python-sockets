import socket

#Formato de recibimiento
FORMAT = 'utf-8'
HEADER = 20480

#Configuración inicial socket
HOST = socket.gethostbyname(socket.gethostname()) # 192.167.0.2
PORT = 5050
ADDR = (HOST, PORT)

#Creación del socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(ADDR)
servidor.listen()

print('[Servidor] Esperando conexión...')

#Realizar la conexión con cliente (aceptación)
try:
    #Bloqueo de flujo del programa
    conn, addr = servidor.accept() #Linea que bloquea el flujo
    print(f'Conexión con el cliente {addr}')
except socket.error as e:
    print(f'[Servidor ]Hubo un error al aceptar la conexión {e}')


#Enviar mensajería con cliente
while True:
    try:
        mensaje = input('[Servidor] Escriba un mensaje para el cliente:')
        conn.send(mensaje.encode())

        if mensaje == 'salir':
            break
    except socket.error as e:
        print(f'[Servidor] Error al enviar la mensajería {e}')
        break


print('Hemos salido del envio de mensajeria')
             