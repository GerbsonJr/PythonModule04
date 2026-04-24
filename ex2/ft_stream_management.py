import sys


def transform_add_hash_per_line(text: str) -> str:
    lines = text.splitlines(True)
    out = []
    for line in lines:
        if line.endswith("\n"):
            out.append(line[:-1] + "#\n")
        else:
            out.append(line + "#")
    return "".join(out)


def stderr(msg: str) -> None:
    sys.stderr.write(f"[STDERR] {msg}\n")


def read_user_line(prompt: str) -> str:
    # No input() allowed: write prompt and read from stdin
    sys.stdout.write(prompt)
    sys.stdout.flush()
    s = sys.stdin.readline()
    if s.endswith("\n"):
        s = s[:-1]
    return s


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
    except OSError as e:
        stderr(f"Error opening file '{filename}': {e}")
        return

    try:
        print("---")
        original = f.read()
        sys.stdout.write(original)
        if len(original) > 0 and not original.endswith("\n"):
            sys.stdout.write("\n")
        print("---")
    finally:
        try:
            f.close()
        finally:
            print(f"File '{filename}' closed.")

    print("Transform data:")
    transformed = transform_add_hash_per_line(original)
    print("---")
    sys.stdout.write(transformed)
    if len(transformed) > 0 and not transformed.endswith("\n"):
        sys.stdout.write("\n")
    print("---")

    new_name = read_user_line("Enter new file name (or empty): ")
    if new_name == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_name}'")
    try:
        out = open(new_name, "w")
    except OSError as e:
        stderr(f"Error opening file '{new_name}': {e}")
        print("Data not saved.")
        return

    try:
        out.write(transformed)
    finally:
        out.close()

    print(f"Data saved in file '{new_name}'.")


if __name__ == "__main__":
    main()
