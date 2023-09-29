from Crypto.Util.number import inverse, long_to_bytes
from sympy import factorint

# Given parameters from the challenge
n = 102812568668937980441364628030483631731
e = 65537
ciphertext = 8963789834135020795224347902733157530

# Factorize n to get p and q
factors = factorint(n)
p, q = factors.keys()

# Calculate totient (phi)
phi = (p - 1) * (q - 1)

# Compute the private key exponent (d)
d = inverse(e, phi)

# Decrypt the ciphertext to get the original message (as an integer)
m = pow(ciphertext, d, n)

# Convert the integer message back into bytes
flag_bytes = long_to_bytes(m)

# Convert the bytes into a string
flag = flag_bytes.decode()

print("Decrypted flag: ", flag)
