from cryptography.fernet import Fernet

#This version is a test to see if its possible to
#encrypt a file using multiple keys v00.2 will be decrypting using the keyfiles generated within this script


#first key
key = Fernet.generate_key()
with open("firstkey.key", 'wb') as keyfile:
	keyfile.write(key)
	keyfile.close()
#second key
key1 = Fernet.generate_key()
with open("secondkey.key",'wb') as keyfile2:
	keyfile2.write(key1)
	keyfile2.close()
#make testfile.txt
with open("testfile.txt", 'w') as file:
	file.write("this is a test file")
	file.close()
#encrypt testfile with first key
with open("testfile.txt", 'rb') as testfile:
	origanal = testfile.read()
	testfile.close()
fernet = Fernet(key)
encrypted = fernet.encrypt(origanal)
with open("testfile.txt",'wb') as encrypt:
	encrypt.write(encrypted)
	encrypt.close()
#encrypt testfile with second key
with open("testfile.txt", 'rb') as testfile2:
	origanal2 = testfile2.read()
	testfile2.close()
fernet2 = Fernet(key1)
encrypted2 = fernet2.encrypt(origanal2)
with open("testfile.txt", 'wb') as encrypt2:
	encrypt2.write(encrypted2)
	encrypt2.close()