def caesar_cipher(text, shift, mode = 'encrypt'):
    result = ''
    shift = shift % 26

    if mode == 'decrypt':
        shift = -shift  # reverse if decryption

    for character in text:
        if character.isalpha():
            start = ord('A') if character.isupper() else ord('a')   # check if upper or lower case 
            enc = chr(((ord(character) - start + shift) % 26) + start)

            result += enc

        else:
            result += character   # if character is not a letter then just keep it the same 
    return result



def vigenere_cipher(text, keyword, mode='encrypt'):
    keyword = keyword.lower()
    result = ''
    keyword_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(keyword[keyword_index]) - ord('a')  # Calculate shift from keyword
            if mode == 'decrypt':
                shift = -shift  # Reverse shift for decryption
            
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)

            # Move to the next keyword letter
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result


