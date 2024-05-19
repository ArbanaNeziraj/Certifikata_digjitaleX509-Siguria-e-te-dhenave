import socket
import ssl
from cryptography.fernet import Fernet
import hashlib
import base64

# Detajet e serverit
server_address = ('127.0.0.1', 8000)

# Krijo nje socket dhe wrap me SSL
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(cafile="/Users/anditernava/server.crt")  # path ku jon ne pc lokalisht
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(sock, server_hostname='localhost')

# lidhu me server
ssl_sock.connect(server_address)
print("Connected to server")

# gjenero celsin per enkriptim
key1 = hashlib.sha256()
key1.update(socket.gethostname().encode('utf-8'))
key2 = key1.hexdigest()[:32]
key3 = base64.b64encode(key2.encode('utf-8'))
cipher_suite = Fernet(key3)
try:
  while true:
    message = input('Enter message foer server:')
    encrypted_message = cipher_suite.encrypt(message.encode('utf-8))
    ssl_sock.sendall(encrypted_message)

    if message.lower() == "bye";
    break
    response =ssl_sock.recv(1024)
    decrypted_response = cipher_suite.decrypt(response)
    print("\n>>Message sent from server(encrypted);",response)
    print(">> Decrypted message sent from server:",decrypted_response.decode(utf-8))
finally:
  print("closing connection")
  ssl_sock.close()
