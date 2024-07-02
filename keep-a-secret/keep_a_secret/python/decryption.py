import os
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import logging

class Decrypt():
    def __init__(self, password, cipher_message, unique_id):
        self.password_bytes = password.encode()
        self.cipher_message = cipher_message.encode()
        self.unique_id = unique_id

    def read_salt(self):
        with open(f"salts/salt_file_{self.unique_id}.txt", "rb") as file:
            return file.read()
        
    # Takes the given password and salt and generates a key
    def get_password_key(self, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.password_bytes))
        return key

    def decrypt(self):
        salt = self.read_salt()
        key = self.get_password_key(salt)
        
        fernet = Fernet(key)
        try:
            message = fernet.decrypt(self.cipher_message)
        except InvalidToken:
            logging.error("Decryption error. The provided password or salt is invalid. Please verify your entry.")
            return None
        return message.decode()