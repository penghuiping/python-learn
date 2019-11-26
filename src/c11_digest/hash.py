# encoding=UTF-8
import hashlib

md5 = hashlib.md5()
md5.update("123456".encode())
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update("123456".encode())
print(sha1.hexdigest())

sha256 = hashlib.sha256()
sha256.update("123456".encode())
print(sha256.hexdigest())


