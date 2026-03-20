if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        with open("file_read.txt", 'r') as file_r:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(file_r.read())
    except FileNotFoundError:
        print("Non-existent file\n")
    try:
        with open("file_write.txt", 'w') as file_w:
            print("SECURE PRESERVATION:")
            file_w.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion")
    except PermissionError:
        print("Permission denied")
    print()
    print("All vault operations completed with maximum security")
