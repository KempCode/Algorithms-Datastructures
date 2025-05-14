# O(N) Time and space
def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    # you dont need to create a new alphabet, just use the formula!!
    for letter in string:
        old_pos = alphabet.index(letter)
        new_pos = (old_pos + key) % 26
        output += alphabet[new_pos]
    return output
    

# Turns out prevoiusly the += operation creates a new string every time due to strings being immutable in python.
def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = []
    for letter in string:
        old_pos = alphabet.index(letter)
        new_pos = (old_pos + key) % 26
        result.append(alphabet[new_pos])
    return ''.join(result)