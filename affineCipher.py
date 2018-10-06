import os
import sys
upperCased = list(map(chr, range(ord('A'), ord('Z')+1)))  	# A, B, C, ..., Z
lowerCased = list(map(chr, range(ord('a'), ord('z')+1))) 		# a, b, c, ..., z
otherSymbols = [' ', '?', '!', '.', ':', '-', '_', '(', ')']
alphabet = upperCased + lowerCased + otherSymbols

a = int(input('Enter first key: '))
b = int(input('Enter second key: '))

def main():
    call_cipher()
    call_decipher()

def hcf(a, b): return a if b == 0 else hcf(b, a % b)
def are_relatively_primes(a, b): return hcf(a, b) == 1
def get_multiplicative_inverse(a):
    result = 1
    for i in range(1, len(alphabet)):
        if (a * i) % len(alphabet) == 1:
            result = i
    return result

def affine_cipher(normal_text, a, b):
    if a < 1 or a > len(alphabet):
        print(f"'a' must be in the interval [1,{len(alphabet)}]")
    elif b < 1 or b > len(alphabet):
        print(f"'b' must be in the interval [1,{len(alphabet)}]")
    elif not are_relatively_primes(a, len(alphabet)):
        print(f"'a'must be relatively prime to {len(alphabet)}")
    else:
        print("Great input!")
    result = ""

    m = len(alphabet)

    for p_char in normal_text:
        p = alphabet.index(p_char)
        c = a * p + b % m
        c_index = c % len(alphabet)
        c_char = alphabet[c_index]

        result += c_char

    return result

def decipher(cipher_text, a, b):
    if a < 1 or a > len(alphabet):
        print(f"'a' must be in the interval [1,{len(alphabet)}]")
    elif b < 1 or b > len(alphabet):
        print(f"'b' must be in the interval [1,{len(alphabet)}]")
    elif not are_relatively_primes(a, len(alphabet)):
        print(f"'a'must be relatively prime to {len(alphabet)}")
    else:
        print("Great input!")
    result = ""

    m = len(alphabet)

    for c_char in cipher_text:
        c = alphabet.index(c_char)
        a_inverse = get_multiplicative_inverse(a)
        p_index = a_inverse * (c - b) % len(alphabet)
        if p_index < 0:
            p_index += len(alphabet)
        p_char = alphabet[p_index]
        result += p_char
    return result

def call_cipher():
    input_file_name = "text.txt"
    output_file_name = "ciphered_text.txt"
    if not os.path.exists(input_file_name):
        print(f"The file {input_file_name}s does not exist. Quitting... ")
        sys.exit()
    file_input = open(input_file_name)
    content = file_input.read()
    file_input.close()
    ciphered = affine_cipher(content, a, b)
    file_output = open(output_file_name, 'w')
    file_output.write(ciphered)
    file_output.close()

def call_decipher():
    input_file_name = "ciphered_text.txt"
    if not os.path.exists(input_file_name):
        print(f"The file {input_file_name}s does not exist. Quitting... ")
        sys.exit()
    file_input = open(input_file_name)
    content = file_input.read()
    file_input.close()
    translated = decipher(content, a, b)
    print(translated)

main()