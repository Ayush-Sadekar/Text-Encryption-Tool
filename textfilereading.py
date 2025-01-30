from ciphers import caesar_cipher, vigenere_cipher

caesar_list = [line.rstrip() for line in open("caesar_text.txt")]

phrase1 = caesar_list[0]
shift = int(caesar_list[1])
mode1 = caesar_list[2]

print(caesar_cipher(phrase1, shift, mode1))

vigenere_list = [line.rstrip() for line in open("vigenere_text.txt")]

phrase2 = vigenere_list[0]
keyword = vigenere_list[1]
mode2 = vigenere_list[2]

print(vigenere_cipher(phrase2, keyword, mode2))
