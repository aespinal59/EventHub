import hashlib

def hash_password(password):
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
    return hashed_pass

def check_password(input_pass, hashed_pass):
    hashed_input = hashlib.sha256(input_pass.encode()).hexdigest()
    return hashed_input == hashed_pass