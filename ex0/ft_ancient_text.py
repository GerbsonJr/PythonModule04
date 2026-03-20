if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        with open("ancient_fragment.txt", 'r') as file:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            print(file.read())
            print()
            print("Data recovery complete. Storage unit disconnected.")
    except OSError:
        print("ERROR: Storage vault not found")
