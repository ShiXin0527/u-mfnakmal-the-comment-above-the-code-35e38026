#!/usr/bin/env python3
"""Entry for make.fun bounty: The Comment Above the Code

A tiny one-liner joke program. Run it and it prints the joke.
"""

JOKE = "// This code works. Don't touch it. I don't know why it works. Nobody knows. Just let it be."


def tell_joke():
    """Return the one-line joke for this bounty."""
    return JOKE


def main():
    print(tell_joke())


if __name__ == "__main__":
    main()
