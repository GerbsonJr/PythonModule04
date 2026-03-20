if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as file:
            file.read()
        print("SUCCESS: Archive recovered")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
    print("STATUS: Crisis handled, system stable\n")
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", "r") as file:
            file.read()
        print("SUCCESS: Archive recovered")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
    print("STATUS: Crisis handled, security maintained\n")
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as file:
            data = file.read()
        print(f"SUCCESS: Archive recovered - \"{data}\"")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
    print("STATUS: Normal operations resumed\n")
    print("All crisis scenarios handled successfully. Archives secure.")
