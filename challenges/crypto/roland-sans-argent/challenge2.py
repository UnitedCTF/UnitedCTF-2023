# pip install pycryptodome
from Crypto.Util.number import getPrime, GCD, bytes_to_long


def encrypt_rsa(message, e, n):
    m = bytes_to_long(message.encode())
    c = pow(m, e, n)
    return c


def generate_rsa_keys(e1, e2):
    while True:
        p = getPrime(512)
        q = getPrime(512)

        n = p * q
        phi = (p - 1) * (q - 1)

        # Ensure both e1 and e2 are coprime with phi
        if GCD(e1, phi) == 1 and GCD(e2, phi) == 1:
            return (e1, n), (e2, n)


flag = input("Enter the secret flag: ")

e1 = 65537
e2 = 65539  # Next prime after 65537

public_key1, public_key2 = generate_rsa_keys(e1, e2)

encrypted_flag1 = encrypt_rsa(flag, *public_key1)
encrypted_flag2 = encrypt_rsa(flag, *public_key2)

print(f"Encrypted flag with e1: {encrypted_flag1}")
print(f"Encrypted flag with e2: {encrypted_flag2}")
print(f"Common public key n: {public_key1[1]}")
print(f"Public key e1: {public_key1[0]}")
print(f"Public key e2: {public_key2[0]}")
