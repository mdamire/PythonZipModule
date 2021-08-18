from genericpath import isfile
import os
import re

from .exec7za import Exec7za
from .zipcomplete import ZipComplete
from .ziplist import ZipList

class Zipper():

    def __init__(self, path, *, password=None) -> None:
        dir = os.path.dirname(path)
        zip = os.path.basename(path)
        if not re.search(r'\.zip$', zip):
            zip = zip + ".zip"

        self.zipfile = os.path.join(dir, zip)
        self.password = password


    def _dirCheck(self, outdir, create):
        if os.path.isfile(outdir):
            raise OSError(f"Specified directory: {outdir} is a file")

        if not os.path.isdir(outdir):
            if create:
                os.makedirs(outdir, mode=0o777)
            else:
                raise OSError("Directory do not exist: {}".format(outdir))


    def _zipCheck(self) -> bool:
        if not os.path.isfile(self.zipfile):
            raise OSError(f'Zip file {self.zipfile} do not exist')



    def add(self, *filelist, createDir=False) -> ZipComplete:
        self._dirCheck(os.path.dirname(self.zipfile), createDir)

        filelistfilter = [i for i in filelist if os.path.isfile(i)]
        
        if not len(filelistfilter):
            raise FileNotFoundError("Files do not exist. Could not create zip file")

        e7obj = Exec7za('a', self.zipfile)
        if self.password:
            e7obj.add_args(f'-p{self.password}')
        
        e7obj.add_args(*filelistfilter)
        zipcomplete = e7obj.run()

        return zipcomplete


    def remove(self, *filelist) -> ZipComplete:
        self._zipCheck()

        if not filelist:
            return ZipComplete(0, '', '')

        e7obj = Exec7za('d', self.zipfile)
        if self.password:
            e7obj.add_args(f'-p{self.password}')

        e7obj.add_args(*filelist, '-r')

        zipcomplete = e7obj.run()
        return zipcomplete


    def update(self, *filelist):
        self._zipCheck()

        if not filelist:
            return ZipComplete(0, '', '')

        e7obj = Exec7za('u', self.zipfile)
        if self.password:
            e7obj.add_args(f'-p{self.password}')

        e7obj.add_args(*filelist)

        zipcomplete = e7obj.run()
        return zipcomplete


    def getList(self) -> ZipList:
        self._zipCheck()
        e7obj = Exec7za('l', self.zipfile)
        zc = e7obj.run()

        return ZipList(zc)


    def extract(self, outdir:str, *filelist, createDir:bool=False) -> ZipComplete:
        """
        filelist can be a glob or a file name
        """
        self._zipCheck()
        self._dirCheck(outdir, createDir)

        filelistfilter = filelist #create a filelist filter with regex

        e7obj = Exec7za('e', self.zipfile, f'-o{outdir}')
        if self.password:
            e7obj.add_args(f'-p{self.password}')
        if filelistfilter:
            e7obj.add_args(*filelistfilter)
        e7obj.add_args('-r')

        zipcomplete = e7obj.run()
        return zipcomplete


    def extractWithPath(self, outdir:str, *filelist, createDir:bool=False) -> ZipComplete:
        """
        filelist can be a glob or a file name
        """
        self._zipCheck()
        self._dirCheck(outdir, createDir)

        e7obj = Exec7za('x', self.zipfile, f'-o{outdir}')
        if self.password:
            e7obj.add_args(f'-p{self.password}')
        if filelist:
            e7obj.add_args(*filelist)
        e7obj.add_args('-r')

        zipcomplete = e7obj.run()
        return zipcomplete