
def to_sha256(s):
    from hashlib import sha256
    
    s = sha256(s.encode()).hexdigest()

    return s
