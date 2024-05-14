import socket
import sys
import threading

# Clase para manejar la comunicación del cliente con el servidor
class Client:
    def __init__(self, server, port, username):
        self.server = server
        self.port = port
        self.username = username
        self.socket = None
        self.sInput = None
        self.sOutput = None

    # Método para iniciar la conexión
    def start(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.server, self.port))
            self.sInput = self.socket.makefile('r')
            self.sOutput = self.socket.makefile('w')
            self.sendMessage(self.username)
            return True
        except Exception as e:
            print(f"Error de conexión: {e}")
            return False

    # Método para enviar un mensaje al servidor
    def sendMessage(self, msg):
        try:
            self.sOutput.write(msg + "\n")
            self.sOutput.flush()
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")

    # Método para recibir mensajes del servidor
    def receiveMessage(self):
        try:
            while True:
                msg = self.sInput.readline().strip()
                if not msg:
                    break
                print(msg)
        except Exception as e:
            print(f"Error al recibir mensaje: {e}")

    # Método para cerrar la conexión
    def disconnect(self):
        try:
            if self.socket:
                self.socket.close()
            if self.sInput:
                self.sInput.close()
            if self.sOutput:
                self.sOutput.close()
        except Exception as e:
            print(f"Error al cerrar conexión: {e}")

# Función principal para ejecutar el cliente
def main():

    username = input("Escribe tu nombre de usuario: ")
    server = "localhost"
    port = 1500

    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("Puerto inválido.")
            return

    client = Client(server, port, username)
    if client.start():
        print("\n¡Hola! Bienvenido al chat.")
        print("Instrucciones:")
        print("1. Escribe tu mensaje para enviarlo a todos los clientes activos.")
        print("2. Escribe '@username mensaje' sin comillas para enviar un mensaje privado a un cliente específico.")
        print("3. Escribe 'WHOISIN' sin comillas para ver la lista de clientes activos.")
        print("4. Escribe 'LOGOUT' sin comillas para desconectarte del servidor.")

        # Hilo para recibir mensajes del servidor
        receiveThread = threading.Thread(target=client.receiveMessage)
        receiveThread.start()

        # Loop para enviar mensajes
        while True:
            msg = input("> ")
            if msg.lower() == "logout":
                client.sendMessage("LOGOUT")
                break
            elif msg.lower() == "whoisin":
                client.sendMessage("WHOISIN")
            else:
                client.sendMessage(msg)

        # Cerrar conexión al salir del loop
        client.disconnect()

if __name__ == "__main__":
    main()

