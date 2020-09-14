from .factory import FlagType
import logging
import sys
import argparse
import pdb

class Arg(metaclass = FlagType):
    keywords = ['include', "type", "description", "default" ]

    def __init__(self, factory, name, *argv, **kwargs):
        self.name = name
        if not hasattr(argv, 'type'):
            logging.error("cannot find argument type in json description")
            sys.exit(1)
        self.type = argv['type']
       
        if hasattr(argv, 'description'):
            self.description = argv['description']
        else:
            self.description = "no description provided"

        if hasattr(argv,'default'):
            self.default = argv['description']
        else:
            self.default = None

        for k,v in argv:
            if k not in Arg.keywords:
                factory.Create(k,v)
