import os.path
import sys
from flagjsonreader import FlagJsonReader
from args import factory
import pdb


def main():
    reader = FlagJsonReader()
    reader.SetupFlags() # read json flags definition

if __name__ == "__main__":
    main()
