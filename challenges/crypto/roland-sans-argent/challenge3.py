# pip install pycryptodome
from Crypto.Util.number import getPrime, GCD, bytes_to_long
from math import gcd


def encrypt_rsa(message, e, n):
    m = bytes_to_long(message.encode())
    c = pow(m, e, n)
    return c


def generate_rsa_modulus():
    p = getPrime(512)
    q = getPrime(512)
    return p * q


def are_pairwise_coprime(ns):
    for i in range(len(ns)):
        for j in range(i + 1, len(ns)):
            if gcd(ns[i], ns[j]) != 1:
                return False
    return True


def generate_three_coprime_moduli():
    while True:
        n1 = generate_rsa_modulus()
        n2 = generate_rsa_modulus()
        n3 = generate_rsa_modulus()

        if are_pairwise_coprime([n1, n2, n3]):
            return n1, n2, n3


flag = input("Enter the secret flag: ")

e = 3

n1, n2, n3 = generate_three_coprime_moduli()

encrypted_flag1 = encrypt_rsa(flag, e, n1)
encrypted_flag2 = encrypt_rsa(flag, e, n2)
encrypted_flag3 = encrypt_rsa(flag, e, n3)

print(f"Encrypted flag with n1: {encrypted_flag1}")
print(f"Encrypted flag with n2: {encrypted_flag2}")
print(f"Encrypted flag with n3: {encrypted_flag3}")
print(f"Public key n1: {n1}")
print(f"Public key n2: {n2}")
print(f"Public key n3: {n3}")
print(f"Public exponent e: {e}")
