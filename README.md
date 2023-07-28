# End-of-module-assignment

# Client/Server Network

This project is a client/server network built in Python. The client and server can be on separate machines or on the same machine.

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

## Features

- The client can create a dictionary, populate it, serialise it, and send it to the server.
- The client can create a text file and send it to the server.
- The user can set the pickling format for the dictionary to one of the following: binary, JSON, or XML.
- The user can choose to encrypt the text in the text file.
- The server has a configurable option to print the contents of the sent items to the screen or to a file.
- The server can handle encrypted contents.

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

The project contains two main files: `client.py` and `server.py`.

`client.py` contains the `Client` class with methods to connect to the server, validate the pickling format and encrypt option, send a dictionary to the server using binary, JSON, or XML serialisation, and send a text file to the server with an option to encrypt its contents.

`server.py` contains the `Server` class with methods to start the server, validate the print option, receive a serialised dictionary from the client using binary, JSON, or XML serialisation, print the dictionary to the screen or a file, and receive a text file from the client with an option to decrypt its contents.

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
