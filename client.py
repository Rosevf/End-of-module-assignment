"""
Client side script
"""
import sys
import socket
import pickle
import json
from xml_marshaller import xml_marshaller
from cryptography.fernet import Fernet


def connect_server():
    """
    Function used to connect the Server
    """

    # Connect to server socket
    host = socket.gethostname()  # Server IP address
    port = 12345  # Server port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Uses exception handling to handle potential conection errors
    try:
        server_socket.connect((host, port))
    except ConnectionRefusedError:
        print("Server has not started yet")
        # Exit the program if fail to connect the server
        sys.exit()

    # Ask user for the pickling format
    while True:
        pickling_format = input(
            "Enter the pickling format (binary/JSON/XML): ").lower()
        if not validate_pickling_format(pickling_format):
            print("Invalid pickling format.")
        else:
            break

    # Ask user for the encrypt option
    while True:
        encrypt_option = input(
            "Please select encrypt option for the text file (yes/no): ").lower()
        if not validate_encrypt_option(encrypt_option):
            print("Invalid option.")
        else:
            break

    # Ask user for the name to show in the dictionary
    name = input("Enter your name to show in the dictionary: ")
    # Create dictionary
    dictionary = {}
    dictionary["name"] = name
    dictionary["format"] = pickling_format
    dictionary = dict(sorted(dictionary.items()))

    # Send the pickling format to server
    server_socket.sendall(pickling_format.encode())

    # Print Server response message after sending pickling format
    print(server_socket.recv(1024).decode())

    # Send dictionary to the server
    if pickling_format == "binary":
        send_dictionary_with_binary(server_socket, dictionary)
    elif pickling_format == "json":
        send_dictionary_with_json(server_socket, dictionary)
    elif pickling_format == "xml":
        send_dictionary_with_xml(server_socket, dictionary)

    # Print Server response message after sending dictionary
    print(server_socket.recv(1024).decode())

    # Send the encrypt option to server
    server_socket.sendall(encrypt_option.encode())

    # Recevie the key used for encryption from the server
    key = server_socket.recv(1024)

    # Send the text file to server
    send_text_file(server_socket, encrypt_option, key)

    # Print Server response message after sending the text file
    print(server_socket.recv(1024).decode())
    server_socket.close()

############################## Below functions for handling the dictionary ###################################################


def validate_pickling_format(pickling_format):
    """
    Function used to validate the pickling format
    """
    if pickling_format in ("binary", "json", "xml"):
        return True
    else:
        return False


def validate_encrypt_option(encrypt_option):
    """
    Function used to validate the encrypt option
    """
    if encrypt_option in ("yes", "no"):
        return True
    else:
        return False


def send_dictionary_with_binary(server_socket, dictionary):
    """
    Function used to send dictionary with binary
    """
    # Serialise the dictionary with pickle and send to the server
    with server_socket.makefile('wb', buffering=0) as pickle_file:
        pickle.dump(dictionary, pickle_file)


def send_dictionary_with_json(server_socket, dictionary):
    """
    Function used to send dictionary with JSON
    """
    # Serialise the dictionary with JSON
    data = json.dumps(dictionary)
    # Send the serialised dictionary to the server
    server_socket.sendall(bytes(data, encoding="utf-8"))


def send_dictionary_with_xml(server_socket, dictionary):
    """
    Function used to send dictionary with XML
    """
    # Serialise the dictionary with XML
    data = xml_marshaller.dumps(dictionary)
    # Send the serialised dictionary to the server
    server_socket.sendall(data)

############################## Below function for handling the text file ###################################################


def send_text_file(server_socket, encrypt_option, key):
    """
    Function used to send Text File
    """
    # Create the text file
    with open('text.txt', 'wt') as text_file:
        text_file_msg = 'Text file created by client'
        text_file.write(text_file_msg)

    with open('text.txt', 'rt') as text_file:
        data = text_file.read()
        if encrypt_option == "yes":
            # Encrypt the text file content
            fernet = Fernet(key)
            server_socket.sendall(fernet.encrypt(data.encode()))
        else:
            server_socket.sendall(data.encode())


if __name__ == "__main__":
    connect_server()
