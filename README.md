# End-of-module-assignment

# Client/Server Network

This project implements a Client/Server application in Python, enabling bidirectional communication between a client and a server. The application allows users to create and populate dictionaries, serialize them using binary, JSON, or XML formats, and optionally encrypt text files. The server receives and processes the data, offering flexible printing options for received items.


## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Code Structure](#code-structure)
- [Code Standards](#code-standards)
- [Team Members](#team-members)
- [License](#license)
- [Contribution Guidelines](#contribution-guidelines)



## Features

The client can perform the following actions:
-	Create a dictionary
-	Populate the dictionary
-	Serialize the dictionary
-	Send the serialized dictionary to the server
-	Create a text file
-	Send the text file to the server
-	Set the pickling format for the dictionary to one of the following: binary, JSON, or XML
-	Choose to encrypt the text in the text file

The Server does the following:
-	Print the contents of the sent items to the screen or to a file (configurable option)
-	If the text file is encrypted, the server decrypts it.
-	The server prints the dictionary's contents and the text file. It asks the user to print the data to the screen or save it in a file.


## Getting Started

### Prerequisites

- Python 3.x
- cryptography
- xml_marshaller

### Installation

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.

### Usage

1. Start the server by running `python server.py`.
2. Start the client by running `python client.py`.
3. Follow the prompts on the client side to set the pickling format, encrypt option, and name for the dictionary.
4. Follow the prompts on the server side to set the print option for the contents of the sent items.

## Code Structure

The project contains the following main files:

1. **Client.py:** Contains the Client class with the following methods:
•	The client end requests the user's name, which is used to create and populate a dictionary.
•	The client end allows the user to choose the dictionary's serialization (or 'pickling') format. The options are binary, JSON, or XML.
•	The client end creates a text file and seeks user input on whether to encrypt it.
•	Send a text file to the server with an option to encrypt its contents
2. **Server.py**: Contains the Server class with the following methods:
•	Start the server
•	Validate the print option
•	Receive a serialized dictionary from the client using binary, JSON, or XML serialization
•	Print the dictionary to the screen or a file
•	Receive a text file from the client with an option to decrypt its contents


## Code Standards

The code is written to PEP standard and uses exception handling to handle potential errors. Unit tests are included.

## Team Members

- Wan Chi Dickson Chan
- Maikel Handersonn
- Yee Man Keung
- Ramz Aftab
- Niousha Vafamanesh

## License

This project is licensed under MIT License.

## Contribution Guidelines

Contributions to this project are welcome. To contribute:
-	Fork the repository.
-	Create a new branch for your feature or bug fix.
-	Make your changes and commit them with descriptive messages.
-	Push your changes to your forked repository.
-	Submit a pull request to the main repository.

