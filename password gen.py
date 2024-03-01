import random
key="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM943462993782"
length=int(input())
password=""

for  i in range (length):
    password+=random.choice(key)
print(password)