def main():
    right_data = False
    while right_data is False:
        p = int(input("Enter p: "))
        q = int(input("Enter q: "))
        x = int(input("Enter x: "))
        n = p * q
        var_gcd = gcd(x, n)
        if (var_gcd == 1) & ((p - 3) % 4 == 0) & ((q - 3) % 4 == 0):
            right_data = True
        print()

    text = "text to be ciphered"
    print(f'Original text: {text}')
    print(f'Encrypted: {bbs_encryption(text, p, q, x)}')
    print(f'Decrypted: {bbs_decryption(bbs_encryption(text, p, q, x), p, q, x)}')


def make_random(p, q, x):
    result = 0
    n = p * q
    xi = (x * x) % n
    si = xi % 2
    k = 1
    result = result | (k * si)
    for i in range(1, 8):
        xi = (xi * xi) % n
        si = xi % 2
        if si != 0:
            k = pow(2, i)
            result = result | k
    return result


def bbs_encryption(text, p, q, x):
    result = ''
    r = make_random(p, q, x)
    for char in text:
        result += ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(char, str(r)))  # char ^ r
    return result


def bbs_decryption(text, p, q, x):
    result = ''
    r = make_random(p, q, x)
    for char in text:
        result += ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(char, str(r)))  # char ^ r
    return result


def gcd(u, v):
    while v != 0:
        r = u % v
        u = v
        v = r
    return u


main()

