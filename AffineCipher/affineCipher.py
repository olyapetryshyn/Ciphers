import os
import sys
upperCased = list(map(chr, range(ord('A'), ord('Z')+1)))  	# A, B, C, ..., Z
lowerCased = list(map(chr, range(ord('a'), ord('z')+1))) 		# a, b, c, ..., z
probil = list(' ')
#otherSymbols = [' ', '?', '!', '.', ':', '-', '_', '(', ')']
alphabet = upperCased + lowerCased + probil
letterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99,
               'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
               'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
etaoin = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

a = int(input('Enter first key: '))
b = int(input('Enter second key: '))

def main():
     call_cipher()
     call_decipher()
     call_freq_decipher()

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
        print(f"The file {input_file_name} does not exist. Quitting... ")
        sys.exit()
    file_input = open(input_file_name)
    content = file_input.read()
    file_input.close()
    translated = decipher(content, a, b)
    print(translated)

def get_letter_count(message):
    letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for letter in message.upper():
        if letter in upperCased:
            letter_count[letter] += 1
    return letter_count

def get_item_at_index_zero(x):
    return x[0]

def get_frequency_order(message):
    letter_to_freq = get_letter_count(message)
    freq_to_letter = {}
    for letter in upperCased:
        if letter_to_freq[letter] not in freq_to_letter:
            freq_to_letter[letter_to_freq[letter]] = [letter]
        else:
            freq_to_letter[letter_to_freq[letter]].append(letter)
    for freq in freq_to_letter:
        freq_to_letter[freq].sort(key=etaoin.find, reverse=True)
        freq_to_letter[freq] = ''.join(freq_to_letter[freq])
    freq_pairs = list(freq_to_letter.items())
    freq_pairs.sort(key=get_item_at_index_zero, reverse=True)
    freq_order = []
    for freq_pair in freq_pairs:
        freq_order.append(freq_pair[1])
    return ''.join(freq_order)

def freq_match_score(message):
    freq_order = get_frequency_order(message)
    match_score = 0
    for commonLetter in etaoin[:6]:
        if commonLetter in freq_order[:6]:
            match_score += 1
    for uncommonLetter in etaoin[-6:]:
        if uncommonLetter in freq_order[-6:]:
            match_score += 1
    return match_score

def call_freq_decipher():
    input_file_name = "text.txt"
    if not os.path.exists(input_file_name):
        print(f"The file {input_file_name} does not exist. Quitting... ")
        sys.exit()
    file_input = open(input_file_name)
    content = file_input.read()
    file_input.close()
    translated = get_frequency_order(content)
    print(translated)

main()
