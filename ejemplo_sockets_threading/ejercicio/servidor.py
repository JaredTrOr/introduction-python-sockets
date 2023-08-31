import socket
import threading

HOST = socket.gethostbyname(socket.gethostname()) # --> IP
PORT = 5050
ADDR = (HOST, PORT)

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(ADDR)
servidor.listen()

print(f'[Servidor] Servidor corriendo en el puerto {PORT}')

conexiones = []

def aceptar_conexiones():
    print('[Servidor] Aceptando conexiones...')
    while True:
        try:
            conn, addr = servidor.accept()

            conexiones.append({
                'conexion': conn,
                'direccion': addr[0],
                'puerto': addr[1]
            })

            print(f'[Servidor] Se ha realizdo una conexión con la computadora con el puerto TCP {addr[1]}')

        except socket.error as e:
            print(f'[Servidor] Hubo un error al aceptar la  {e}')

def panel_control():
    print('[Servidor] PANEL DE CONTROL DE OPERACIÓN')
    print('--> listar')
    print('--> seleccionar')
    print('--> cerrar')

    while True:
        operacion_realizar = input('[Servidor] Introduzca la operación a realizar: \n')

        if operacion_realizar == 'listar':
            if conexiones:
                listar()
            else:
                print('[Servidor] Todavía no hay ninguna conexión en el servidor :(')

        elif 'seleccionar' in operacion_realizar:
            if conexiones:
                conexion_seleccionada = seleccionar_conexion(operacion_realizar)

                if conexion_seleccionada is None:
                    print('[Servidor] No existe esa conexión :(')

                else:
                    manejar_cliente(conexion_seleccionada)

            else:
                print('[Servidor] Todavía no hay ninguna conexión en el servidor para seleccionar :(')

        elif operacion_realizar == 'cerrar':
            print('[Servidor] Bye bye...')

        else:
            print(f'[Servidor] Instrucción "{operacion_realizar}" no encontrada :(') 

def listar():
    print('[CONEXIONES]:')
    print('')
    for i, conexion in enumerate(conexiones):
        print(f'{i}.-   TCP_PORT={conexion["puerto"]}   IP={conexion["direccion"]}')

    print('')

def seleccionar_conexion(operacion):
    operacion = operacion.replace('seleccionar', '')
    index = int(operacion)

    if index > len(conexiones):
        print('[Servidor] Selección no válida')
        return None

    conexion = conexiones[index]

    if conexion is None:
        return None
    
    return conexion

def manejar_cliente(conexion):
    #Conexión del cliente
    conn = conexion['conexion']

    print(f'[Servidor] Conexión con el cliente {conexion["puerto"]}')
    
    while True:
        operacion_realizar = input('[Servidor] Escriba la operación a realizar: \n')
    
        if operacion_realizar == 'salir':
            break

        try:
            conn.send(operacion_realizar.encode())

        except socket.error as e:
            print(f'[Servidor ] Hubo un error al enviar el mensaje al cliente {e}')
            break

#Creación de hilos
aceptar_conexiones_thread = threading.Thread(target=aceptar_conexiones)
aceptar_conexiones_thread.start()

panel_control_thread = threading.Thread(target=panel_control)
panel_control_thread.start()