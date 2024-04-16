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
    
