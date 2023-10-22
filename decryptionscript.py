file=open('newbob.txt')
text=file.read()

# Caesar cipher.
#text = input("Enter your message: ")
key=int(input('Enter a key '))
cipher = ''
for char in text:
    if not char.isalnum():
        cipher+=char
        continue
    if char.isdigit():
        cipher+=char
        continue
    if char.isupper():
        code = ord(char) - key
        if code < ord('A'):
            result = 65-code
            code = 91 - result
        cipher += chr(code)
        continue
    if char.isspace():
        cipher+=' '
        continue
    code = ord(char) - key
    if code < ord('a'):
        result=97-code
        code = 123-result
    cipher += chr(code)
file2=open('decryptedfile.txt','w')
for ch in cipher:
    file2.write(ch)
file.close()
file2.close()