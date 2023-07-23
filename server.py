"""
Server side script
"""
import socket
import pickle
import json
from xml_marshaller import xml_marshaller
from cryptography.fernet import Fernet


class Server:
    """Server Class"""

    def start_server(self):
        """
        Function used to start the Server
        """
        # Start the server socket
        host = socket.gethostname()  # Server IP address
        port = 12345  # Server port
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server started on {host}.")
        while True:
            # Accept the client
            client, address = server_socket.accept()
            print(f"Connection from {address} has been established!")

            # Ask user for the option to print the content
            while True:
                print_option = input(
                    "Please select option to print the contents of the sent items (screen/file) :").lower()
                if not self.validate_print_option(print_option):
                    print("Invalid option.")
                else:
                    break

            # Receive client's choice on the pickling format of the dictionary
            pickling_format = client.recv(1024).decode()

            # Send Response message to the client after receiving pickling format
            msg = "Server received pickling format."
            client.sendall(msg.encode())

            # Receive serialised dictionary from the client
            if pickling_format == "binary":
                self.receive_dictionary_binary(client, print_option)
            elif pickling_format == "json":
                self.receive_dictionary_json(client, print_option)
            elif pickling_format == "xml":
                self.receive_dictionary_xml(client, print_option)

            # Send Response message to the client after recevied dictionary
            msg = "Server received dictionary."
            client.sendall(msg.encode())

            # Receive encrypt option from client
            encrypt_option = client.recv(1024).decode()

            if encrypt_option == "yes":
                # Send the encrption key to the client if the encrypt option is yes
                key = Fernet.generate_key()
                client.sendall(key)
            else:
                # Send a dummy key to the client if the encrypt option is no
                key = "empty key"
                client.sendall(key.encode())

            # Receive text file from client
            self.receive_text_file(client, print_option, encrypt_option, key)

            # Send Response message to the client after receiving text file
            msg = "Server received Text file."
            client.sendall(msg.encode())

            client.close()

    @staticmethod
    def validate_print_option(print_option):
        """
        Function used to validate the print option
        """
        if print_option in ("screen", "file"):
            return True
        else:
            return False

    ############################## Below functions for handling the dictionary ###################################################
    def receive_dictionary_binary(self, client, print_option):
        """
        Function used to receive dictionary with binary
        """
        # Convert the pickle file to dictionary
        with client.makefile('rb') as pickle_file:
            obj = pickle.load(pickle_file)
        self.print_dictionary(obj, print_option)

    def receive_dictionary_json(self, client, print_option):
        """
        Function used to receive dictionary with JSON
        """
        received = client.recv(1024)
        # Convert the JSON to dictionary
        obj = json.loads(received.decode("utf-8"))
        self.print_dictionary(obj, print_option)

    def receive_dictionary_xml(self, client, print_option):
        """
        Function used to receive dictionary with XML
        """
        received = client.recv(1024)
        # Convert the XML to dictionary
        obj = xml_marshaller.loads(received)
        self.print_dictionary(obj, print_option)

    @staticmethod
    def print_dictionary(dictionary, print_option):
        """
        Function used to print dictionary to screen / file
        """
        if print_option == "screen":
            # Print the dictionary to screen
            print(f"Recevied dictionary is : {dictionary}")
        elif print_option == "file":
            # Print the dictionary to file
            with open("dictionary.txt", "wt") as dictionary_file:
                dictionary_file.write(json.dumps(dictionary))
            print("Recevied dictionary printed to file")

    ############################## Below function for handling the text file ###################################################

    @staticmethod
    def receive_text_file(client, print_option, encrypt_option, key):
        """
        Function used to receive Text File
        """
        data = client.recv(1024)
        if encrypt_option == 'yes':
            # decrypt the text file content if encryt option is yes
            print(f"Recevied encryted text content is : {data.decode()}")
            fernet = Fernet(key)
            decrypt_data = fernet.decrypt(data)
            text_file_content = decrypt_data.decode()
        else:
            text_file_content = data.decode()

        if print_option == "screen":
            # Print the text content to screen
            print(f"Recevied text content is : {text_file_content}")
        elif print_option == "file":
            # Print the text content to file
            with open("text.txt", "wt") as text_file:
                text_file.write(text_file_content)
            print("Recevied text content printed to file")


if __name__ == "__main__":
    server = Server()
    server.start_server()
