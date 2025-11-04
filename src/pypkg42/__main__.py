"""
Module entry point for direct execution: uv run python -m pypkg42

When Python's -m flag is used with a package name, it executes the __main__.py file
within that package. This pattern allows the package to be run directly as a script
while maintaining its importability as a library.

If -m is used with a single module file (not a package), Python will execute the code
under `if __name__ == "__main__":` within that module instead.
"""

import sys

from pypkg42.cli import main

if __name__ == "__main__":
    sys.exit(main())
