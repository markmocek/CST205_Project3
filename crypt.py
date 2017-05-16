'''
CST205 - Project 3 - Justin Hines, Francisco Hernandez, Mark Mocek - 5/16/17
'''

from Crypto.Cipher import AES
import string
import base64
import time

# import modules
PADDING = '{'
BLOCK_SIZE = 32
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
# prepare crypto method
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
# set encryption/decryption variables


# Encrypt function for call in main file
def encryption(userString):
    letter = 3
    while letter == 3:
        secret = '0123456789abcdef'
        countTotal = (len(secret))
        if countTotal == 16:
            cipher = AES.new(secret)
            letter = 0
        else:
            print("Please Ensure The Key You Entered Is 16 Characters In Length\n")
            letter = 3
            # this checks the encryption key to ensure it matches the correct length
    # encode a string
    data = userString
    encoded = EncodeAES(cipher, data)
    print('Encrypted string:', encoded)


# Decrypt function for call in main file
def decryption(userString):
    encoded = userString
    letter = 3
    while letter == 3:
        secret = '0123456789abcdef'
        countTotal = (len(secret))
        # this checks the encryption key to ensure it matches the correct length
        if countTotal == 16:
            cipher = AES.new(secret)
            letter = 0
            decoded = DecodeAES(cipher, encoded)
            print('Decrypted string:', decoded)
        else:
            print("Please Ensure The Key You Entered Is 16 Characters In Length\n")
            letter = 3
