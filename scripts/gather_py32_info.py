"""Gather information about the Python 3.2.5 environment.

Run this script using the 3.2.5 interpreter to capture details
useful for debugging the porting effort.

Example:
    python3.2 scripts/gather_py32_info.py
"""

import json
import pkgutil
import platform
import sys


def main() -> None:
    data = {
        "python_version": sys.version,
        "executable": sys.executable,
        "platform": platform.platform(),
        "prefix": sys.prefix,
        "modules": sorted(m[1] for m in pkgutil.iter_modules()),
    }
    with open("py32_info.json", "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)
    print("Environment information written to py32_info.json")


if __name__ == "__main__":
    main()
