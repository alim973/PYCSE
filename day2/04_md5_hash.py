import hashlib

def generate_md5(data):
    return hashlib.md5(data.encode()).hexdigest()

print(generate_md5("password")) # Output: 1a2b3c4d5e6f7g8h9i0j

