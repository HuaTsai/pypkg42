"""Command-line interface for pypkg42."""

import sys

from pyfiglet import Figlet

from pypkg42 import __version__


def main() -> int:
    """Main entry point for the CLI."""
    figlet = Figlet(font="slant")
    print(figlet.renderText("pypkg42"))
    print(f"Hello world from pypkg42 {__version__}!")


if __name__ == "__main__":
    sys.exit(main())
