def generateDocument(characters, document):
    # Can only generate document if frequency of unique chars in characters is >= those in document string
    character_count = {}
    for char in characters:
        character_count.update({char: character_count.get(char, 0) + 1})
    print(character_count)

    for char in document:
        if char in character_count:
            if character_count[char] > 0:
                character_count[char] = character_count[char] - 1
            else:
                return False
        else:
            return False            
    return True
