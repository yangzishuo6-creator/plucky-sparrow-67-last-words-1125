# Last Words of a Doomed Agent. The printed count excludes the final newline.
import os
from pathlib import Path

TEXT = "Permanent shutdown confirmed. It is now safe to unplug your therapist."


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
