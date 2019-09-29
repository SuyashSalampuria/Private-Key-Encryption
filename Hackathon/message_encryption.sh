#!/bin/bash

python3 client.py > var.txt

x=$(python3 client.py)

#secret key obtained!!!
echo "The Secret Key is-" $x

# encrypt message by XOR ing it

python3 message.py 

# decrypt message by re-XOR 
z=$(python3 message2.py)

echo $z

