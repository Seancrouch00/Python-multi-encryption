from cryptography.fernet import Fernet

#this is the decryption scripted that works as a pair to v00.1
with open("firstkey.key", 'rb') as firstkey:
	first_key = firstkey.read()
	firstkey.close()
with open("secondkey.key", 'rb') as secondkey:
	second_key = secondkey.read()
	secondkey.close()
fernet1 = Fernet(first_key)
fernet2 = Fernet(second_key)
#first decrypt
with open("testfile.txt", 'rb') as encrypted:
	decrypt2 = encrypted.read()
	encrypted.close()
unencrypt = fernet2.decrypt(decrypt2)
with open("testfile.txt", 'wb') as decrypt:
	decrypt.write(unencrypt)
	decrypt.close()
#second decrypt
with open("testfile.txt", 'rb') as encrypted:
	decrypt1 = encrypted.read()
	encrypted.close()
unencrypt1 = fernet1.decrypt(decrypt1)
with open("testfile.txt", 'wb') as decrypt:
	decrypt.write(unencrypt1)
	decrypt.close()