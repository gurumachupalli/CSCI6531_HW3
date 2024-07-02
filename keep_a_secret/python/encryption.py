import os
import uuid
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Encrypt():
    def __init__(self, password, message):
        self.encoded_password = password.encode()
        self.encoded_message = message.encode()

    # Stores the given salt in salt_file. Required for info
    def write_salt(self):
        salt = os.urandom(16)
        unique_id = uuid.uuid4().hex
        with open(f"salts/salt_file_{unique_id}.txt", "wb") as file:
            file.write(salt)
        return salt, unique_id

    # Takes the given password and salt and generates a key
    def get_password_key(self, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.encoded_password))
        return key

    # Encrypts the message with the generated salt and key from the helper functions (write_salt and get_password_key)
    def encrypt(self):
        salt, unique_id = self.write_salt()
        key = self.get_password_key(salt)

        fernet = Fernet(key)
        cipher_message = fernet.encrypt(self.encoded_message)
        return cipher_message, unique_id