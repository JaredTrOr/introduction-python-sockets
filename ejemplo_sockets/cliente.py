import socket

#Formato de recibimiento
FORMAT = 'utf-8'
HEADER = 20480

#Configuración de constantes de socket de cliente
HOST = socket.gethostbyname(socket.gethostname()) # IP a la que nos queremos conectar
PORT = 5050 #Puerto al que nos queremos conectar
ADDR = (HOST, PORT)

#Creación del socket cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conexión con el servidor desde el cliente
try:
    cliente.connect(ADDR) #Línea que bloquea el flujo
    print('[Cliente] Conexión exitosa con el servidor')

except socket.error as e:
    print(f'[Cliente] Hubo un error al conectarse con el servidor {e}')


#Recibir y enviar mensajería
while True:
    try:
        mensaje_desde_el_servidor = cliente.recv(HEADER).decode(FORMAT)
                                                                
        if mensaje_desde_el_servidor == 'salir':
            break

        print(mensaje_desde_el_servidor)
    except socket.error as e:
        print(f'[Cliente] Error al recibir el mensaje del cliente')
        break

print('Desconexión :3')








