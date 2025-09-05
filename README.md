"""
AES File Encryption 🔐
----------------------

This project lets you encrypt and decrypt files using AES (Fernet).

USAGE:
1. Generate a secret key (only once):
   >>> generate_key()

2. Encrypt a file:
   >>> encrypt_file("example.txt")

   This will create: example.txt.enc

3. Decrypt a file:
   >>> decrypt_file("example.txt.enc")

   This will create: example_decrypted

⚠️ IMPORTANT:
- Keep 'secret.key' safe. Without it, you cannot decrypt your files.
- Do NOT upload 'secret.key' to GitHub (it's ignored using .gitignore).
"""

from cryptography.fernet import Fernet

def generate_key():
    """Generate and save a secret key."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as secret.key")

def load_key():
    """Load the previously generated secret key."""
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    """Encrypt a file and save it with .enc extension."""
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

    print(f"{filename} encrypted successfully as {filename}.enc")

def decrypt_file(filename):
    """Decrypt a file and save it as *_decrypted."""
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    output_file = filename.replace(".enc", "_decrypted")
    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print(f"{filename} decrypted successfully to {output_file}")


# Example usage (uncomment as needed)
if __name__ == "__main__":
    # generate_key()
    # encrypt_file("example.txt")
    # decrypt_file("example.txt.enc")
    pass