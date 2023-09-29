from Crypto.Util.number import inverse, long_to_bytes
import math

# Given parameters from the challenge
n = 75028926564243095350876556253054002059048724162557616616984189236507249837906571739103341249511617617686728055121809964555365800748123277977503402143848791135583759511900470314822144753821175349989759114593174302727420916174556594489335976199015832911621980456957179023125962485241644610617345637998571255579
e = 65537
ciphertext = 56008170769554887262576319302940601118185325126886908098084196135436308065377532766072584970927988557945463342052117388311916233341535457277134719836517077918981273317076166502671280138135633782266262824257003537995945302780023802715707789751684451670470443189343490113838854309789410818510249988212513174403


# Fermat's factorization method
def fermat_factorization(n):
    a = math.isqrt(n) + 1
    b2 = a * a - n
    iterations = 0
    max_iterations = 10000  # Adjust as needed
    while not is_perfect_square(b2) and iterations < max_iterations:
        a += 1
        b2 = a * a - n
        iterations += 1
    if iterations == max_iterations:
        raise ValueError("Fermat factorization failed. p and q might not be close enough.")
    b = math.isqrt(b2)
    return a - b, a + b


def is_perfect_square(num):
    return int(num ** 0.5 + 0.5) ** 2 == num


# Factorize n to get p and q using Fermat's factorization
p, q = fermat_factorization(n)

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
