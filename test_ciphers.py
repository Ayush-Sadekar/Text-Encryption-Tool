import unittest
from ciphers import caesar_cipher, vigenere_cipher

class CipherTestCases(unittest.TestCase):
    
    def test_caesar_encryption(self):
        self.maxDiff = None


        # w/o special characters 
        self.assertEqual("Kbyhua", caesar_cipher("Durant", 7, mode = 'encrypt'))

        # w special characters 
        self.assertEqual("Kb_y3hu4a", caesar_cipher("Du_r3an4t", 7, mode = 'encrypt'))

        # negative shift 
        self.assertEqual("Mc bc sghcm sb oqisfrc qcbhwuc.", caesar_cipher("Yo no estoy en acuerdo contigo.", -12, mode='encrypt'))

    def test_caesar_decryption(self):
        # w/o special characters 
        self.assertEqual("Durant", caesar_cipher("Kbyhua", 7, mode = 'decrypt'))

        # w special characters
        self.assertEqual("Du_r3an4t", caesar_cipher("Kb_y3hu4a", 7, mode = 'decrypt'))

        # w negative shift 
        self.assertEqual("When caterpillars undergo metamorphosis, they become butterflies after breaking out of their cocoons.", caesar_cipher("Kvsb qohsfdwzzofg ibrsfuc ashoacfdvcgwg, hvsm psqcas pihhsftzwsg othsf pfsoywbu cih ct hvswf qcqccbg.", -12, mode="decrypt"))

        
    
    def test_caesar_reversibility(self):

        phrase = "LeBron James might have surpassed Michael Jordan with the accolades that he continues to receive. However, it's only a matter of time before he retires. How much more will he cement into his legacy?"    

        encrypted = caesar_cipher(phrase, 5, mode='encrypt')

        decrypted = caesar_cipher(encrypted, 5, mode= 'decrypt')

        self.assertEqual(decrypted, phrase)

    def test_vigenere_encryption(self):
        # w/o special characters
        self.assertEqual("Lbt ulawz figqc jfp djqgk ikii 13 duoc ugah.", vigenere_cipher("The quick brown fox jumps over 13 lazy dogs.", "super", mode= "encrypt"))
        # w special characters 
        self.assertEqual("Ses_-0hccy4785-+yl4", vigenere_cipher("Akd_-0dlke4785-+jh4", "super", mode= 'encrypt'))
        
        
    
    def test_vigenere_decryption(self):

        # w/o special characters 
        self.assertEqual("The quick brown fox jumps over 13 lazy dogs.", vigenere_cipher("Lbt ulawz figqc jfp djqgk ikii 13 duoc ugah.", "super", mode= "decrypt"))

        # w special characters 
        self.assertEqual("Akd_-0dlke4785-+jh4", vigenere_cipher("Ses_-0hccy4785-+yl4", "super", mode= 'decrypt'))

        
        
    
    def test_vigenere_reversibility(self):
        phrase = "If there were no Batman fans, I would be the only one. If there were infinite Batman fans, I would be the greatest fan. Who is the Batman? To the blind, a vision, to the deaf, a voice. In the dark, a beacon of hope reaching out to all."

        encrypted = vigenere_cipher("If there were no Batman fans, I would be the only one. If there were infinite Batman fans, I would be the greatest fan. Who is the Batman? To the blind, a vision, to the deaf, a voice. In the dark, a beacon of hope reaching out to all.", "splendidly", mode='encrypt')

        decrypted = vigenere_cipher(encrypted, "splendidly", mode="decrypt")

        self.assertEqual(phrase, decrypted)
    
if __name__ == '__main__':
    unittest.main()
