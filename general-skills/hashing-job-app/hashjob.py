import hashlib

unhashed = bytes(input("the input:"), "utf-8")

print(hashlib.md5(unhashed).hexdigest())

