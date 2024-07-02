import argparse
from python.decryption import Decrypt
from python.encryption import Encrypt
import logging


def decrypt_message(keep_a_secret):
    decryption = keep_a_secret.decrypt()
    logging.info(f"Decrypted Message: {decryption}")
    return decryption


def encrypt_message(keep_a_secret):
    encryption, unique_id = keep_a_secret.encrypt()
    print(f"Encrypted Message: {encryption}")
    print(f"Unique ID: {unique_id}")
    return encryption, unique_id


def main(args):
    if args.command == "encrypt":
        keep_a_secret = Encrypt(
            password=args.password,
            message=args.message
        )
        args.func(keep_a_secret)
    elif args.command == "decrypt":
        keep_a_secret = Decrypt(
            password=args.password,
            cipher_message=args.cipher_message,
            unique_id=args.unique_id
        )
        args.func(keep_a_secret)
    else:
        parser.print_help()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='keep-a-secret', description='CLI to encrypt and decrypt messages given a password.')
    subparsers = parser.add_subparsers(title='commands', dest='command')

    # Decrypt subparser
    decrypt_parser = subparsers.add_parser('decrypt', help='Decrypts the provided cipher message with the password and salt.')
    decrypt_parser.add_argument('--password', required=True, help='Password to use for the decryption.')
    decrypt_parser.add_argument('--cipher-message', required=True, help='Cipher message to decrypt.')
    decrypt_parser.add_argument('--unique-id', required=True, help='Unique ID to look up the salt.')
    decrypt_parser.set_defaults(func=decrypt_message)
    
    # Encrypt subparser
    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypts the given message with the password.')
    encrypt_parser.add_argument('--password', required=True, help='Password to use for the encryption.')
    encrypt_parser.add_argument('--message', required=True, help='The message to encrypt.')
    encrypt_parser.set_defaults(func=encrypt_message)
    
    args = parser.parse_args()
    main(args)
