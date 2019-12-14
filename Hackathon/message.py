# reading the message
msg_code = open("var2.txt")
msg = msg_code.read()

# reading the public key
public_key_file = open("var.txt")
public_key = public_key_file.read()

# encoding the message
encoded_msg = ""
stri = str(int(msg) ^ int(public_key))
i = 0
length = len(stri)
while i < length:
	s = stri[i:i+3]
	# chr() returns a string representing a character
	# whose Unicode code point is an integer
	b = chr(int(s))
	encoded_msg += b
	i+=3

print(encoded_msg)