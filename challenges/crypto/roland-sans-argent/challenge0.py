# pip install pycryptodome
from Crypto.Util.number import getPrime, inverse, bytes_to_long


def encrypt_rsa(message, e, n):
    m = bytes_to_long(message.encode())
    c = pow(m, e, n)
    return c


def generate_rsa_keys(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    return (e, n), d


flag = input("Enter the secret flag: ")

p = getPrime(512)
q = getPrime(512)

e = 65537

public_key, private_key = generate_rsa_keys(p, q, e)
encrypted_flag = encrypt_rsa(flag, *public_key)

print(f"Encrypted flag: {encrypted_flag}")
print(f"Public key n: {public_key[1]}")
print(f"Public key e: {public_key[0]}")
print(f"Prime p: {p}")
