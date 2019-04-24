def cal_e(x):
    cal_elist = [n for n in range(2, x) if gcd(n, x) == 1]
    return cal_elist

def gcd(a, b):
    while b is not 0:
        c = a % b
        a = b
        b = c
    return a

def cal_d(a, e):
    for n in range(1, 1000):
        i = ((a * n) + 1)
        if i % e == 0:
            return i / e
    return None

def encrypt(m):
    return ''.join([chr(encrypt_byte(ord(x))) for x in m])
def encrypt_byte(b):
    c = (b ** e) % n
    return c

def decrypt(c):
    return ''.join([chr(decrypt_byte(ord(x))) for x in c])
def decrypt_byte(b):
    c = (b ** d) % n
    return c

p = int(input("Enter large prime int p: "))
q = int(input("Enter large prime int q: "))
n = p * q
phi = (p - 1) * (q - 1)
print("Choose an e from a below coprimes array:\n")
elist = cal_e(phi)
e = int(input(elist))
d = int(cal_d(phi, e))
print("d is : ",d)
m = input("Enter plain text : ")
ct = encrypt(m)
print("Cipher text is : ", ct)
msg = decrypt(ct)
print("Decrypted text is : ",msg)
