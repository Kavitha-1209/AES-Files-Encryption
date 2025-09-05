from cryptography.fernet import Fernet

# 1. Generate or load a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as secret.key")

def load_key():
    return open("secret.key", "rb").read()

# 2. Encrypt a file
def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        data = file.read()
    
    encrypted = f.encrypt(data)
    
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)
    
    print(f"{filename} encrypted successfully!")

# 3. Decrypt a file
def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        data = file.read()
    
    decrypted = f.decrypt(data)
    
    # Remove .enc from filename
    original_filename = filename.replace(".enc", "_decrypted")
    with open(original_filename, "wb") as file:
        file.write(decrypted)
    
    print(f"{filename} decrypted successfully to {original_filename}")

if __name__=="__main__":
 decrypt_file("example.txt.enc")