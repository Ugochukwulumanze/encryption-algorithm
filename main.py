file=open('bob.txt')
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
        code = ord(char) + key
        if code > ord('Z'):
            result = code - 90
            code = ord('@') + result
        cipher += chr(code)
        continue
    if char.isspace():
        cipher+=' '
        continue
    code = ord(char) + key
    if code > ord('z'):
        result=code-122
        code = 96+result
    cipher += chr(code)
file2=open('newbob.txt','w')
for ch in cipher:
    file2.write(ch)
file.close()
file2.close()