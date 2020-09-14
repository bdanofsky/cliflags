import abc
import logging
import sys
import argparse
import pdb

class FlagType(type):
    def __new__(meta, name, bases, attrs):
        cls = super(FlagType, meta).__new__(meta, name, bases, attrs)
        Factory.Register(name,cls)
        return cls
        

class Factory(object):

    flagTypes = {}

    def __init__(self):
        self.parser = argparse.ArgumentParser() # root parser
    
    @staticmethod
    def Register(name, cls):
        if name not in Factory.flagTypes.keys():
            Factory.flagTypes[name] = cls
        else:
            logging.error('class %s has already been registered'%(name))
            sys.exit(1)
         

    def Create(self, name, *args, **kwargs):
        if name in Factory.flagTypes.keys():
            return Factory.flagTypes[name](self, name, *args, **kwargs)

        logging.error('cannot find %s in flagTypes'%(name))
        sys.exit(1)
