
file1=open("var.txt")
key=file1.read()
# printing original string

#encryption
test_str = input('Enter your message: ')
stri = ""

for x in test_str:
	s = ord(x)
	if s<100 and s>=10 :
		s = "0" + str(s)
	elif s < 10 :
		s = "00" + str(s)
	stri = stri + str(s)

# decimal = bin(n).replace("0b", "")
x = str(int(key) ^ int(stri))
print("The XOR of message and secret key is : " + x)
file2=open('var2.txt', 'w')
file2.write(x)
file2.close()

