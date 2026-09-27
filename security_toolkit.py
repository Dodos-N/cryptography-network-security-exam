#!/usr/bin/env python3
"""
ULK Polytechnic Institute - Cryptography & Network Security
Task 2: Security Toolkit (Encryption, Decryption, Integrity Verification)
"""

import sys
import os
import hashlib
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

def generate_or_load_key():
    """Generates a key or loads an existing key from local file system."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as kf:
            kf.write(key)
        print(f"[+] Key File Created: Generated new symmetric key in '{KEY_FILE}'.")
    else:
        with open(KEY_FILE, "rb") as kf:
            key = kf.read()
        print(f"[+] Key Loaded: Successfully read key from '{KEY_FILE}'.")
    return Fernet(key)

def encrypt_file(file_path, fernet):
    """Encrypts a file and saves the encrypted output with a .enc extension."""
    if not os.path.isfile(file_path):
        print(f"[-] Error: Target file '{file_path}' does not exist.")
        return False
    
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        
        encrypted_data = fernet.encrypt(data)
        out_path = file_path + ".enc"
        
        with open(out_path, "wb") as f:
            f.write(encrypted_data)
            
        print(f"[+] Encryption Successful: Encrypted data saved to '{out_path}'.")
        return True
    except Exception as e:
        print(f"[-] Encryption Failed: {e}")
        return False

def decrypt_file(enc_file_path, original_file_path, fernet):
    """Decrypts a file and verifies that its contents match the original."""
    if not os.path.isfile(enc_file_path):
        print(f"[-] Error: Encrypted file '{enc_file_path}' does not exist.")
        return False

    try:
        with open(enc_file_path, "rb") as f:
            enc_data = f.read()
            
        decrypted_data = fernet.decrypt(enc_data)
        
        dec_path = enc_file_path + ".dec"
        with open(dec_path, "wb") as f:
            f.write(decrypted_data)
            
        # Verify decrypted content matches original file
        if os.path.isfile(original_file_path):
            with open(original_file_path, "rb") as f:
                orig_data = f.read()
            
            if decrypted_data == orig_data:
                print("[+] Decryption Verified: Decrypted content EXACTLY matches original file.")
            else:
                print("[-] Decryption Warning: Decrypted content DOES NOT match original file.")
        else:
            print(f"[+] Decrypted successfully to '{dec_path}' (Original file omitted for comparison).")
            
        return True
    except Exception as e:
        print(f"[-] Decryption Failed (Key mismatch or corrupted payload): {e}")
        return False

def calculate_sha256(file_path):
    """Calculates and returns the SHA-256 hash of a specified file."""
    if not os.path.isfile(file_path):
        print(f"[-] Error: File '{file_path}' not found for hash calculation.")
        return None

    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        digest = sha256_hash.hexdigest()
        print(f"[+] SHA-256 Digest ({file_path}): {digest}")
        return digest
    except Exception as e:
        print(f"[-] Hash Calculation Error: {e}")
        return None

def verify_integrity(file_path, expected_hash):
    """Calculates SHA-256 and detects whether the file has changed."""
    current_hash = calculate_sha256(file_path)
    if current_hash is None:
        return False
    
    if current_hash == expected_hash:
        print("[+] Integrity Verification PASSED: File is intact and unchanged.")
        return True
    else:
        print("[!] Integrity Verification FAILED: File alteration or tampering detected!")
        return False

def main():
    print("=" * 65)
    print("  ULK SECURITY TOOLKIT - ENCRYPTION & INTEGRITY TESTING HARNESS  ")
    print("=" * 65)

    sample_file = "sample_student_record.txt"
    
    # Generate sample file if missing
    if not os.path.exists(sample_file):
        print(f"[*] Creating sample student record file: '{sample_file}'...")
        with open(sample_file, "w") as f:
            f.write("STUDENT_ID: ULK-2026-9812\nNAME: John Doe\nSTATUS: Enrolled\nMARKS: 85\n")

    # 1. Initialize Encryption Key
    print("\n--- 1. Key Initialization ---")
    fernet = generate_or_load_key()

    # 2. Baseline SHA-256 Calculation
    print("\n--- 2. Calculate Initial SHA-256 Hash ---")
    original_hash = calculate_sha256(sample_file)

    # 3. Encrypt File
    print("\n--- 3. Encrypting Student Record ---")
    encrypt_file(sample_file, fernet)

    # 4. Decrypt File & Verify Match
    print("\n--- 4. Decrypting & Verifying Record ---")
    decrypt_file(sample_file + ".enc", sample_file, fernet)

    # 5. Integrity Check Demonstration (Original vs Altered)
    print("\n--- 5. Integrity & Tamper Detection Test ---")
    print("[*] Testing unmodified original file:")
    verify_integrity(sample_file, original_hash)

    print("\n[*] Simulating unauthorized alteration...")
    tampered_file = "tampered_student_record.txt"
    with open(sample_file, "r") as f:
        content = f.read()
    with open(tampered_file, "w") as f:
        f.write(content + "TAMPERED_ENTRY: Grade modified to 100\n")

    print(f"[*] Testing modified file '{tampered_file}':")
    verify_integrity(tampered_file, original_hash)

    # Cleanup temporary simulation file
    if os.path.exists(tampered_file):
        os.remove(tampered_file)

    # 6. Error Handling Demonstration
    print("\n--- 6. Error Handling Check ---")
    print("[*] Attempting to encrypt non-existent file:")
    encrypt_file("non_existent_file.txt", fernet)

if __name__ == "__main__":
    main()
