import hashlib
import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from tinyec import registry
from tinyec.ec import Curve

# Define the curve
curve = registry.get_curve('brainpoolP256r1')


def generate_keypair(curve: Curve):
    # Generate private key (a random integer in the range [1, n-1])
    private_key = secrets.randbelow(curve.field.n)

    # Generate public key (an (x,y) coordinate on the curve)
    public_key = private_key * curve.g
    return private_key, public_key


def compress_shared_secret(shared_secret):
    # Serialize the coordinates of the shared secret
    serialized_secret = shared_secret.x.to_bytes(32, 'big') + shared_secret.y.to_bytes(32, 'big')

    # Hash the serialized data using SHA-256
    sha256_hash = hashlib.sha256(serialized_secret).digest()
    return sha256_hash


def encrypt_aes(plaintext, key):
    # Encrypt using AES with the given key
    cipher = AES.new(key, mode=AES.MODE_CBC, iv=secrets.token_bytes(16))
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))  # Default padding with PKCS7
    return ciphertext, cipher.IV


def decrypt_aes(ciphertext, key, IV):
    # Decrypt using AES with the given key and IV
    cipher = AES.new(key, AES.MODE_CBC, IV)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext


# Generate Alice's keypair
alice_private_key, alice_public_key = generate_keypair(curve)

# Generate Bob's keypair
bob_private_key, bob_public_key = generate_keypair(curve)

# Perform ECDH to compute shared secret for Alice
alice_shared_secret = alice_private_key * bob_public_key

# Perform ECDH to compute shared secret for Bob
bob_shared_secret = bob_private_key * alice_public_key

# Compress the shared secrets
compressed_alice_shared_secret = compress_shared_secret(alice_shared_secret)
compressed_bob_shared_secret = compress_shared_secret(bob_shared_secret)

# Encrypt and decrypt using AES with the shared secret
plaintext = "Hello, world!".encode()
encrypted_text, iv = encrypt_aes(plaintext, compressed_alice_shared_secret)
decrypted_text = decrypt_aes(encrypted_text, compressed_bob_shared_secret, iv)

print(compressed_alice_shared_secret)
print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text.decode())
