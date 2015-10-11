

def findSentence(badString):
    goodString = ""
    for i in badString:
        if ord(i) >= 65 and ord(i) <= 122 or ord(i) == 46 or ord(i) == 32 or ord(i) == 39:
            goodString = goodString + i

    print(goodString)


def main():
 
    badString = """ÌTÔÀhª£eõrÄe îisÕÞ äa¥Ñ ýßnÚ×oðr°æmäa¤lðÒ ùíséeýn¾£tªen¥·cºe ³hÙûeéÍr¤íe·ë,îð ²y¯óo¢èuÑÀ j¨µußs»ûtÏ ÏÄdóÀoÆ§néÔ'÷t»¬ ¡²se¬eõ ÝäiÜ÷tøúå ye¡t°Æ.íä°Æ"""
    findSentence(badString)
    
main()

