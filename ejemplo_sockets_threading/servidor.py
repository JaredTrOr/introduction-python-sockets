import socket
import threading

FORMAT = 'utf-8'
HEADER = 20480

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(ADDR)
servidor.listen()

#Arreglo de conexiones
conexiones = []

def aceptar_conexiones():
    while True:
        try:
            conn, addr = servidor.accept()

            conexiones.append({
                'direccion': addr[0],
                'puerto_tcp': addr[1],
                'conexion': conn
            })

            print(f'[Servidor] Conexión realizada con {addr}')

        except socket.error as e:
            print(f'[Servidor] Hubo un error al aceptar la conexión :( {e}')

def panel_operaciones():
    print('[PANEL ADMINISTRATIVO]')

    while True:
        operacion_ejecutar = input('[Servidor]: Escriba la operación a realizar: \n')

        if operacion_ejecutar == 'listar':
            if conexiones:
                listar()

            else:
                print('[Servidor] Todavía no hay conexiones')

        elif 'seleccionar' in operacion_ejecutar:
            if conexiones:
                conexion_realizada = seleccionar(operacion_ejecutar)
                if conexion_realizada is not None:
                    manejar_operaciones(conexion_realizada)
                else:
                    print('[Servidor] No existe la selección')

            else:
                print('[Servidor] No hay conexiones, no se puede realizar la conexión')

        else:
            print(f'[Servidor] Operación {operacion_ejecutar} no encontrada...')

def listar():
    print('[Servidor] Conexiones existentes:')
    for i, conexion in enumerate(conexiones):
        print(f'{i} TCP={conexion["puerto_tcp"]} DIRECCIÓN={conexion["direccion"]}')

    print('\n')

def seleccionar(seleccion):
    posicion = seleccion.replace('seleccionar', '')
    posicion = int(posicion)

    conexion = conexiones[posicion]

    if conexion is None:
        return None
    
    return conexion

def manejar_operaciones(conexion):
    print(f'Realizaste la conexión con el equipo con el puerto {conexion["puerto_tcp"]}')
    conexion_cliente = conexion['conexion']

    while True:
        mensaje = input('[Servidor] Ingresa el mensaje a enviar al cliente:')
        
        if mensaje == 'salir':
            break

        try:
            conexion_cliente.send(mensaje.encode())
        except socket.error as e:
            print(f'[Servidor] Error al enviar el mensaje {e}')
            break

thread_aceptar_conexiones = threading.Thread(target=aceptar_conexiones)
thread_aceptar_conexiones.start()

thread_panel_operaciones = threading.Thread(target=panel_operaciones)
thread_panel_operaciones.start()