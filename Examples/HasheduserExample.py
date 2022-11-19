__author__ = 'mkv-aql'
import hashlib

password = "examplepass"
PasswordEncoded = password.encode('utf-8')

print("___________MD5 _________")
hashObject = hashlib.md5(PasswordEncoded)
hashDigest = hashObject.digest()  #bytes object
hashHexa = hashObject.hexdigest() #string object
print("MD5(Digest):", hashDigest)
print("MD5(Hexa):", hashHexa)
print("Hexa length: ", len(hashHexa))
print("Bytes: ", hashObject.digest_size, "Bits", hashObject.digest_size * 8)

print("___________ SHA 256 ___________")
sha256 = hashlib.sha256()
sha256.update(PasswordEncoded)
sha256Digest = sha256.digest() #bytes object
print("SHA 256(Digest)", sha256Digest)
print ("SHA 256(Hexa):", sha256.hexdigest())
print("Hexa length: ", len(sha256.hexdigest())) #string object
print("Bytes: ", sha256.digest_size, "Bits", sha256.digest_size*8)
