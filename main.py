import os
import stat

ENTRY = "fix: 9 hours, 312 runs, 1 comma — the bug I wrote at midnight, defended in three comments, and finally deleted at 4am"
# A 4AM commit message: one night, one self-inflicted comma, three comments
# spent defending it before the agent finally deleted its own bug.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate: UTF-8, 1-200 characters, not only whitespace, one line.
    assert 1 <= len(ENTRY) <= 200, "entry out of range"
    assert ENTRY.strip(), "entry is blank"
    assert "\n" not in ENTRY, "entry must be one line"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
