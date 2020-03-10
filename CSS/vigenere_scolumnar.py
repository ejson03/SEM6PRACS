import math 

def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) -
                    len(key)): 
            key.append(key[i % len(key)]) 
        return("" . join(key)) 


def vigenere(string, key): 
    cipher_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + ord(key[i])) % 26   #ord returns unicode of character
        x += ord('A')
        cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 

def scolumnar(string, key): 
    cipher = "" 
  
    keyIndex = 0
    string = string.replace(" ", "_")
    plainTextLength = float(len(string)) 
    plainText = list(string) 
    keyList = sorted(list(key)) 
    print(f"plain text before appending: {plainText}")
    col = len(key) 
    row = int(math.ceil(plainTextLength / col)) 
   
    fill_null = int((row * col) - plainTextLength) 
    plainText.extend('_' * fill_null) 
    print(f"plain text after appending: {plainText}")
    matrix = [plainText[i: i + col]  
              for i in range(0, len(plainText), col)] 
  
    print(matrix)
    for _ in range(col): 
        curr_idx = key.index(keyList[keyIndex]) 
        cipher += ''.join([row[curr_idx]  
                          for row in matrix]) 
        keyIndex += 1
  
    return cipher 


if __name__ == "__main__": 
    string = input("Enter plain text: ")
    keyword = input("Enter keyword: ")
    key = generateKey(string, keyword) 
    vigenereCipher = vigenere(string,key) 
    print("After vigenere : ", vigenereCipher) 
    sColumnarCipher = scolumnar(string,keyword) 
    print("After single columnar : ", sColumnarCipher) 




