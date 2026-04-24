from typing import Optional, Tuple, Union


Action = Union[int, str]


def secure_archive(
    filename: str,
    action: Optional[Action] = "read",
    content: Optional[str] = None
) -> Tuple[bool, str]:
    if action is None:
        action_norm = "read"
    elif isinstance(action, int):
        action_norm = "write" if action == 1 else "read"
    else:
        a = action.strip().lower()
        if a in ("w", "write"):
            action_norm = "write"
        else:
            action_norm = "read"

    try:
        if action_norm == "read":
            with open(filename, "r") as f:
                return True, f.read()
        else:
            to_write = "" if content is None else content
            with open(filename, "w") as f:
                f.write(to_write)
            return True, "Content successfully written to file"
    except OSError as e:
        return False, str(e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))

    print("Using 'secure_archive' to read from a regular file:")
    ok, data_or_err = secure_archive("ancient_fragment.txt", "read")
    print((ok, data_or_err))

    if ok:
        print(
            "Using 'secure_archive' to write previous content to a new file:"
        )
        print(secure_archive("secured_copy.txt", "write", data_or_err))
