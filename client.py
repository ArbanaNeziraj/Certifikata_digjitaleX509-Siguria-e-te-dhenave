try:
    while True:
        message = input('Enter message for server: ')
        encrypted_message = cipher_suite.encrypt(message.encode('utf-8'))
        ssl_sock.sendall(encrypted_message)

        if message.lower() == "bye":
            break

        # Receive and decrypt server response
        response = ssl_sock.recv(1024)
        decrypted_response = cipher_suite.decrypt(response)
        print("\n>> Message sent from server (encrypted):", response)
        print(">> Decrypted message sent from server:", decrypted_response.decode('utf-8'))

finally:
    print("Closing connection")
    ssl_sock.close()
