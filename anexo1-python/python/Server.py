import socket
import sys
import threading
from ChatMessage import ChatMessage

class Server:
    def __init__(self, port):
        self.port = port
        self.server_socket = None
        self.clients = {}
        self.lock = threading.Lock()

    def start(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind(('localhost', self.port))
            self.server_socket.listen(5)
            print("Server started on port", self.port)
            self.accept_clients()
        except Exception as e:
            print("Error starting server:", e)
            self.stop()

    def accept_clients(self):
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
        except Exception as e:
            print("Error accepting clients:", e)
            self.stop()

    def handle_client(self, client_socket):
        try:
            s_input = client_socket.makefile('r')
            s_output = client_socket.makefile('w')
            username = s_input.readline().strip()
            self.lock.acquire()
            self.clients[username] = s_output
            self.lock.release()
            self.broadcast(ChatMessage(ChatMessage.MESSAGE, f"{username} has joined the chat room."))
            while True:
                msg = s_input.readline().strip()
                if not msg:
                    break
                self.handle_message(username, msg)
        except Exception as e:
            print("Error handling client:", e)
        finally:
            client_socket.close()
            self.lock.acquire()
            del self.clients[username]
            self.lock.release()
            self.broadcast(ChatMessage(ChatMessage.MESSAGE, f"{username} has left the chat room."))
    
    def handle_message(self, username, msg):
        if msg.lower() == 'whoisin':
            self.send_to_client(username, ChatMessage(ChatMessage.WHOISIN, '\n'.join(self.clients.keys())))
        else:
            self.broadcast(ChatMessage(ChatMessage.MESSAGE, f"{username}: {msg}"))

    def broadcast(self, message):
        self.lock.acquire()
        for client_output in self.clients.values():
            try:
                client_output.write(str(message) + '\n')
                client_output.flush()
            except Exception as e:
                pass
        self.lock.release()

    def send_to_client(self, client, message):
        self.lock.acquire()
        if client in self.clients:
            try:
                self.clients[client].write(str(message) + '\n')
                self.clients[client].flush()
            except Exception as e:
                pass
        self.lock.release()

    def stop(self):
        try:
            if self.server_socket:
                self.server_socket.close()
        except Exception as e:
            pass

if __name__ == "__main__":
    port_number = 1500
    if len(sys.argv) == 2:
        port_number = int(sys.argv[1])

    server = Server(port_number)
    server.start()

