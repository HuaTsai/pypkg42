"""Command-line interface for pypkg42."""

import argparse
import os
import shutil
import sys
import tomllib
from pathlib import Path

from pyfiglet import Figlet

import pypkg42


def get_config_path() -> Path:
    if sys.platform == "win32":
        base = Path(os.environ["APPDATA"])
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Application Support"
    else:
        xdg_config = os.environ.get("XDG_CONFIG_HOME")
        base = Path(xdg_config) if xdg_config else Path.home() / ".config"
    return base / "pypkg42" / "config.toml"


def load_config() -> dict:
    config_path = get_config_path()

    if not config_path.exists():
        config_path.parent.mkdir(parents=True, exist_ok=True)
        default_config = Path(pypkg42.__file__).parent / "config" / "config.toml"
        if default_config.exists():
            shutil.copy2(default_config, config_path)
        else:
            config_path.write_text("[pypkg42]\n# Add your configuration here\n")

    with open(config_path, "rb") as f:
        return tomllib.load(f)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="pypkg42 Command-Line Interface",
        epilog="Enjoy using pypkg42!",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"pypkg42 {pypkg42.__version__}",
        help="Show the version number and exit.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output.",
    )
    return parser.parse_args()


def main() -> int:
    """Main entry point for the CLI."""
    args = parse_args()
    cfg = load_config()
    figlet = Figlet(font="slant")
    print(figlet.renderText("pypkg42"))
    print(f"Hello world from pypkg42 {pypkg42.__version__}!")
    print(f"Configuration: {cfg}")
    if args.verbose:
        print("Verbose mode is enabled.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
