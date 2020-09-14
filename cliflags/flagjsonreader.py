import json
import logging
import os
import sys
from args import factory
import pdb


class FlagJsonReader():

    def __init__(self):
        import __main__
        self.mainpath = os.path.abspath(__main__.__file__)
        self.mainpath = os.path.dirname(self.mainpath)
        self.mainpath = os.path.join(self.mainpath)

        # check for json description and schema
        # current dir, current dir/flags and `file pat to main`/flags
        #
        self.flagsDirs = [os.getcwd(),
                          os.path.join(os.getcwd(), 'flags'),
                          os.path.join(self.mainpath, 'flags')
        ]

    
    def readJson(self, file, flagsDirs):
        '''
        file: name of flags file to read
        flagsDir: search directories for flags

        read chain of include JSON files.
        files are merged from bottom to top
        '''
        if not os.path.exists(file):
            logging.error('cannot open JSON flags file %s'%(file))
            sys.exit(1)
        
        fh = open(file)
        localJson = json.load(fh)
        fh.close()
        if 'include' in localJson:
            found = False
            for sd in flagsDirs:
                incpath = os.path.join(sd, localJson['include'])
                if os.path.exists(incpath):
                    incJson = self.readJson(incpath, flagsDirs)
                    incJson.update(localJson)
                    localJson = incJson
                    found = True
                    break # first match wins
            if not found:
                logging.error('cannot find include file %s'%(localJson['include']))
                sys.exit(1)
                
        return localJson
    
    def processJsonFlags(self):
        '''
        process JSON based flags:
        1) start with localflags.json in execution directory if exists.  This file may include other flags files
        2) if no localflags.json file exists see if <script dir>/schema/flags.json exists and read
        3) otherwise error
        '''
    
        flagsJson = None
        if os.path.exists('localflags.json'):
            path = os.path.join(os.getcwd(), 'localflags.json')
            flagsJson = self.readJson(path, self.flagsDirs)
        else:
            for fdir in self.flagsDirs:
                '''
                read first occurance of flags.json since localflags.json does not exist
                '''
                path = os.path.join(fdir, 'flags.json')
                if os.path.exists(path):
                    flagsJson = self.readJson(path, self.flagsDirs)
                    break

        if flagsJson is None:
            logging.error('cannot find flags file to parse')
            sys.exit(1)
        
        return flagsJson
        

    def SetupFlags(self):
        '''
        read flags JSON files and create flag objects
        after setup the flags can be parsed
        '''
        flagsJson = self.processJsonFlags()
        argFactory = factory.Factory()
        for k,v in flagsJson.items():
            if k in ['include']:
                continue
            arg = argFactory.Create('Arg', k, v)
