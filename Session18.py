import hashlib

# SHA -> Secure Hash Function
# SHA256, SHA512 ...

s1 = "This is Awesome"
s2 = "John,"+str(80)+",john@example.com"
s3 = "John,"+str(80)+",john@example.com"

print(s1)
print(s2)

hashCode1 = int(hashlib.sha512(s1.encode("utf-8")).hexdigest(), 16) % 8
hashCode2 = int(hashlib.sha256(s2.encode("utf-8")).hexdigest(), 16) % 8
hashCode3 = int(hashlib.sha256(s3.encode("utf-8")).hexdigest(), 16) % 8

print(hashCode1)
print(hashCode2)
print(hashCode3)
