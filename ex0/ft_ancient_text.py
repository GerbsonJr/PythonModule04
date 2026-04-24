import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return

    try:
        print("---")
        data = f.read()
        sys.stdout.write(data)
        if len(data) > 0 and not data.endswith("\n"):
            sys.stdout.write("\n")
        print("---")
    finally:
        try:
            f.close()
        finally:
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
