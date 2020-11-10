import sys

def getMessage():
	file = open(str(input()),"r")
	s = file.read()
	s = str(s)
	return s

def getKey():
	print("enter your key(you can provide nothing if you dont want key):", end = " ")
	key = input()
	if key == "":
		key = 'none_public_key'
	return key

def createBox(key):
	box = list(range(256))
	j = 0
	for i in range(256):
		j = (j+box[i] + ord(key[i%len(key)]))%256
		box[i], box[j] = box[j], box[i]
	return box

def decrypt(msg, box, key):
	msg = msg.replace(key, '')
	msg = msg.replace("\n Key:", '')
	res = []
	i, j = 0, 0
	for s in msg:
		i = (i+1)%256
		j = (j+box[i])%256
		box[i], box[j] = box[j], box[i]
		t = (box[i] + box[j])%256
		k = box[t]
		res.append(chr(ord(s)^k))
	ans = "".join(res)
	file = open("decrypted.txt", "wb+")
	file.write(ans.encode())
	print(ans)

def encrypt(msg, box, key):
	res = []
	i, j = 0, 0
	for s in msg:
		i = (i+1)%256
		j = (j+box[i])%256
		box[i], box[j] = box[j], box[i]
		t = (box[i] + box[j])%256
		k = box[t]
		res.append(chr(ord(s)^k))
	ans = "".join(res)
	file = open("encrypted.txt", "wb+")
	file.write(ans.encode())
	line = ("\n Key:" + str(key)).encode()
	file.write(line)
	print(ans)

if __name__ == "__main__":
	print("select 1 for encryption 2 for decryption:", end = " ")
	t = int(input())
	print("give the file you want to encrpyt or decrpyt(specify path):", end = " ")
	if t == 1:
		msg = getMessage()
		key = getKey()
		box = createBox(key)
		encrypt(msg, box, key)
	if t == 2:
		msg =getMessage()
		print("give the same key which you gave for encrption")
		key = getKey()
		box = createBox(key)
		decrypt(msg, box, key)