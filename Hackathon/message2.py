msg_code=open("var2.txt")
z=msg_code.read()
file1=open("var.txt")
key=file1.read()

str1 = ""
stri = str(int(z) ^ int(key))
i = 0
a = len(stri)
while i < a:
	s = stri[i:i+3]
	b = chr(int(s))
	str1 += b
	i+=3

print(str1)