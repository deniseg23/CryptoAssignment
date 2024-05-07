from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

from .conf import Encryption_key

def encrypt_data(plaintext):
   
    
    key_bytes = bytes(Encryption_key, "utf-8")
    plaintext_bytes = bytes(plaintext, "utf-8")

    aes_cipher = Cipher(algorithms.AES(key_bytes),
                    modes.CBC(bytearray(16)),
                    backend=default_backend())
    aes_encryptor = aes_cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    padded_bytes = padder.update(plaintext_bytes) + padder.finalize()
    ciphertext_bytes = aes_encryptor.update(padded_bytes) + aes_encryptor.finalize()
    ciphertext = ciphertext_bytes.hex()

    return ciphertext

def decrypt_data(ciphertext):
    key_bytes = bytes(Encryption_key, "utf-8")
    ciphertext_bytes = bytes.fromhex(ciphertext)

    aes_cipher = Cipher(algorithms.AES(key_bytes),
                    modes.CBC(bytearray(16)),
                    backend=default_backend())
    aes_decryptor = aes_cipher.decryptor()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

    padded_bytes = aes_decryptor.update(ciphertext_bytes) + aes_decryptor.finalize()
    plaintext_bytes = unpadder.update(padded_bytes) + unpadder.finalize()
    plaintext = str(plaintext_bytes, "utf-8")

    return plaintext


def encrypt_password(password):
  
    hashedPassword=hashlib.sha256(password.encode()).hexdigest()
    return hashedPassword
