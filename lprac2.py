p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
p8 = [6, 3, 7, 4, 8, 5, 10, 9]
p4 = [2, 4, 3, 1]
ip = [2, 6, 3, 1, 4, 8, 5, 7]
ep = [4, 1, 2, 3, 2, 3, 4, 1]
ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]

s0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

s1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]

def permutate(key, pbox):
    return ''.join([key[x - 1] for x in pbox])

def shift(key):
    left, right = key[:int(len(key) / 2)], key[int(len(key) / 2):]
    left = left[1:] + left[:1]
    right = right[1:] + right[:1]
    return left + right

def get_keys(key):
    key1 = permutate(shift(permutate(key, p10)), p8)
    key2 = permutate(shift(shift(permutate(key, p10))), p8)
    return key1, key2

def xor(a, b):
    # return ''.join(str(((bit + keybit) % 2)) for bit, keybit in zip (map(int, a), map(int, b)))
    return bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a))

def lookup(text, s):
    row = int(text[0] + text[3], 2)
    col = int(text[1:3], 2)
    return bin(s[row][col])[2:].zfill(8)

def f(ct, key):
    ct_left, ct_right = ct[:int(len(ct) / 2)], ct[int(len(ct) / 2):]
    temp = permutate(ct_right, ep)
    temp = xor(temp, key)
    temp = lookup(temp[:int(len(temp) / 2)], s0) + lookup(temp[int(len(temp) / 2):], s1)
    temp = permutate(temp, p4)
    return ct_right + xor(ct_left, temp)

def encrypt(pt, key1, key2):
    ct = permutate(pt, ip)
    ct = f(ct, key1)
    ct = f(ct, key2)
    return permutate(ct, ip_inv)

def decrypt(ct, key1, key2):
    pt = permutate(ct, ip)
    pt = f(pt, key2)
    pt = f(pt, key1)
    return permutate(pt, ip_inv)

pt = input("plaintext 12: ")
key = input("key 8: ")
#pt = '11101010'
#key = '0111111101'

key1, key2 = get_keys(key)
ct = encrypt(pt, key1, key2)
print(key1)

pt = decrypt(ct, key1, key2)
print(pt)
