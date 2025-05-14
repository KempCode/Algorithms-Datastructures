original_alphabet = "abcdefghijklmnopqrstuvwxyz"
original_alphabet = list(original_alphabet)
ceasar_alphabet = [0] * 26
my_dict = {}
s = "There's-a-starman-waiting-in-the-sky"
k = 3
output = ""

#Loop to create ceasar_alphabet
for i in range(len(original_alphabet)):
    ceasar_alphabet[i] = original_alphabet[(i+k) % 26] 


for i in range(len(original_alphabet)):
    my_dict.update({original_alphabet[i]: ceasar_alphabet[i]})


for i in range(len(s)):
    if(s[i].isalpha()):
        #First letter is a capital.
        if(s[i].isupper()):
            temp = s[i].lower()
            temp2 = my_dict[temp]
            temp2 = temp2.upper()
            output += temp2
            continue
        output += my_dict[s[i]]
    else:
        output += s[i]
            
print(output)
    




