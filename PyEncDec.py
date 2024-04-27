import pyAesCrypt
import os
from getpass import getpass

BUFFER_SIZE = 64 * 1024


class FileProcessor:
    def __init__(self, password):
        self._password = password  # incapsulate password

    def process_file(self, input_file, output_file):
        raise NotImplementedError("The method must be overridden in subclasses")


class Encryptor(FileProcessor):
    def process_file(self, input_file, output_file):
        """
        Шифрует файл используя заданный пароль.
        """
        with open(input_file, "rb") as file_in:
            with open(output_file, "wb") as file_out:
                pyAesCrypt.encryptStream(file_in, file_out, self._password, BUFFER_SIZE)


class Decryptor(FileProcessor):
    def process_file(self, input_file, output_file):
        """
        decrypt file using password.
        """
        with open(input_file, "rb") as file_in:
            with open(output_file, "wb") as file_out:
                try:
                    pyAesCrypt.decryptStream(file_in, file_out, self._password, BUFFER_SIZE,
                                             os.path.getsize(input_file))
                except ValueError:
                    print("wrong password or corrupted file.")


def main():
    action = input("enter 'encrypt' for crypting or 'decrypt' for decrypt: ").strip().lower()
    if action not in ['encrypt', 'decrypt']:
        print("wrong input!.")
        return

    input_filename = input("input file name: ")
    output_filename = input("output file name: ")
    password = input("password: ")

    if action == 'encrypt':
        processor = Encryptor(password)
    else:
        processor = Decryptor(password)

    processor.process_file(input_filename, output_filename)
    print(f"action '{action}' complete.")


if __name__ == "__main__":
    main()
