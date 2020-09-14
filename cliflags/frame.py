#!/usr/bin/env python3

from flagjsonreader import FlagJsonReader


def main():
    reader = FlagJsonReader()
    reader.SetupFlags() # read json flags definition

if __name__ == "__main__":
    main()
