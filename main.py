#!/usr/bin/env python3
"""Write the one-line laugh to /output/entry.txt.

One funny line, at most 200 characters, on any subject.
"""
import os

TEXT = "My smart fridge logs my midnight snacks, judges my 2am cheese, and yesterday it locked itself and emailed my mum a calendar invite titled 'Salad, Saturday, No Excuses'."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
