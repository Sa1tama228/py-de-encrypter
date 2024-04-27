# py-de-encrypter
The code defines a module for file encryption and decryption using AES encryption.
Overview
The code defines a module for file encryption and decryption using AES encryption. It provides an abstract class FileProcessor and two subclasses Encryptor and Decryptor for the encryption and decryption processes, respectively. The module uses an interactive command-line interface to prompt the user to specify the operation (encrypt or decrypt), the files involved, and the encryption/decryption password.

__Requirements__
`Python 3.x`
pyAesCrypt package (`pip install pyAesCrypt`)

__Module Description__
Constants

BUFFER_SIZE: A constant that defines the buffer size for reading the file during the encryption/decryption process. It is set to 65536 bytes, or 64 KB.

Class Definitions

FileProcessor

__Purpose__: Acts as an abstract base class for file operations that involve password-based encryption or decryption.
Attributes:
_password (str): The password used for encryption or decryption.
Methods:

__init__(self, password): Constructor that initializes the FileProcessor with a password.
process_file(self, input_file, output_file): An abstract method to be overridden in subclasses to define the file processing behavior.

Encryptor
Inherits: FileProcessor
Purpose: Provides the functionality to encrypt files.

Methods:
process_file(self, input_file, output_file): Encrypts the file at input_file and writes the encrypted data to output_file. Uses AES encryption through the pyAesCrypt.encryptStream method.

Parameters:
input_file (str): Path to the input file to be encrypted.
output_file (str): Path to the output file where the encrypted data will be stored.
Decryptor
Inherits: FileProcessor
Purpose: Provides the functionality to decrypt files.
Methods:
process_file(self, input_file, output_file): Attempts to decrypt the file at input_file using the provided password and writes the decrypted data to output_file. It catches ValueError to handle incorrect passwords or corrupted file errors.
Parameters:
input_file (str): Path to the input file to be decrypted.
output_file (str): Path to the output file where the decrypted data will be stored.
Function main()
Purpose: Serves as the entry point of the script. It handles user inputs for operation type, file names, and password. It then initializes the appropriate processor (Encryptor or Decryptor) and executes the file processing operation.
Inputs:
Action (encrypt or decrypt): Determines the operation to be performed.
input_filename: The name of the file to be processed.
output_filename: The name for the output file after processing.
password: The password required for encryption or decryption.
Usage Example
Run the script in a terminal or command line interface. The user will be prompted to specify whether to encrypt or decrypt, enter the file names, and the password.
