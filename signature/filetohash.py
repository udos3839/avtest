import hashlib

def filetohash(filepath):
    hasher = hashlib.md5()
    with open(filepath,'rb') as hash_file:
        r_hash = hash_file.read()
        hasher.update(r_hash)
        return hasher.hexdigest()
