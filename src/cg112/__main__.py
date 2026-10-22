"""Main entry point for upmigrate CLI."""

from . import __app_name__, cli


def main():
    """Run the CLI application."""
    cli.app()


if __name__ == "__main__":
    main()
