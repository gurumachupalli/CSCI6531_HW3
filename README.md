# CSCI6531_HW3
CSCI 6531 HW3 Encryption and Decryption Program

## Overview
This is a simple password encryption CLI of a given message. It is able to encrypt and decrypt a message, provided a few other variables.

## Components of the Program
There are 2 components to this program and they are encryption and decryption. Both of these CLIs will require certain variables to function properly. Below you can find an explanation of them.
### Encryption
The encryption requires 2 variables to function properly:
- Password: This is the password that the user wants to encrypt their message with.
- Message: This is the message that the user wants to encrypt.

The encryption will output 2 values and the user will need to save both of these values:
- Encrypted Message: This is the encrypted message and will be needed to decrypt it to the original message.
- Unique ID: This is the ID that will associate the encrypted message to the salt that was used to encrypt.

### Decryption
The decryption requires 3 values to be passed in:
- Password: Password that user used to encrypt the message with.
- Cipher Message: The encrypted message from the encryption.
- Unique ID: This is the ID that's associated with the cipher message's salt. It must be the same id that was the output from encryption for the cipher message.

The decryption will output 1 value:
- Message: This is the decrypted output


## How to run the Program
Below we can see how to run the program for the encryption and decryption using poetry.
### 1. Poetry Setup
Run the following from the folder that contains pyproject.toml:
- poetry shell
Then navigate to the keep_a_secret folder.

### 2. Encryption
Once the poetry shell is up. Run the following for the encryption:
- python3 keep-a-secret.py encrypt --password ENTER_PASSWORD_HERE --message ENTER_MESSAGE_HERE

Copy the outputs of the encryption, the Encrypted Message and Unique ID.

### Decryption
After running the encryption, if you want to decrypt the encrypted message with the password run the decryption:
- python3 keep-a-secret.py decrypt --password ENTER_PASSWORD_HERE --cipher-message ENTER_CIPHER_MESSAGE --unique-id ENTER_UNIQUE_ID

## Sample Ciphers
### Cipher 1
Cipher:
- gAAAAABmg2qfEremZpjIE4NmyQc5XYBDUIUiI7-321m1bh_Dbb3RuRixv6edQvEV_vXH3KOQ4F_LPeINjmsmIZI8kwElbQqqdTzUGRkHiYSdfceK312hEV0=

Password:
- chalupa

Unique ID:
- 59ea7a8a51b54850ad8371aa7cdeb60b

### Cipher 2
Cipher:
- gAAAAABmg2vfTl4McAdIAMQXzCVUzTvGTGiTTfjCzTzkYw_y0RDlwtEz2bkvZrd_guxGi3tlSndzwB1-YRUygLASlzBW7rckIQ==

Unique ID:
- 8dd154f185c04e9daf65a6117b70b0a8