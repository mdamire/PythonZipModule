from genericpath import isfile
import os
import sys

from .exec7za import Exec7za
from .zipcomplete import ZipComplete
from .ziplist import ZipList

class Zipper():

    def __init__(self, path) -> None:
        self.zipfile = path

    def __dirCheck(self, outdir, create):
        if os.path.isfile(outdir):
            raise OSError("Specified out directory is a file")

        if not os.path.isdir(outdir):
            if create:
                os.makedirs(outdir)
            else:
                raise OSError("Directory do not exist: {}".format(outdir))

    def zipCheck(self) -> bool:
        if not os.path.isfile(self.zipfile):
            raise OSError(f'Zip file {self.zipfile} do not exist')


    def add(self, *filelist) -> ZipComplete:
        e7obj = Exec7za('a', self.zipfile)

        filelistfilter = [i for i in filelist if os.path.isfile(i)]
        
        if not len(filelistfilter):
            raise FileNotFoundError("Files do not exist. Could not create zip file")
        
        e7obj.add_args(*filelistfilter)
        zipcomplete = e7obj.run()

        return zipcomplete


    def remove(self, *filelist) -> ZipComplete:
        if not filelist:
            return ZipComplete(0, '', '')

        e7obj = Exec7za('d', self.zipfile)
        e7obj.add_args(*filelist, '-r')

        zipcomplete = e7obj.run()
        return zipcomplete


    def update(self):
        pass


    def getList(self) -> ZipList:
        e7obj = Exec7za('l', self.zipfile)
        zc = e7obj.run()

        return ZipList(zc.get_stdout())

    def extract(self, outdir:str, *filelist, create:bool=False) -> ZipComplete:
        """
        filelist can be a glob or a file name
        """
        self.__dirCheck(outdir, create)

        filelistfilter = filelist #create a filelist filter with regex

        e7obj = Exec7za('e', self.zipfile, f'-o{outdir}')
        if filelistfilter:
            e7obj.add_args(*filelistfilter)
        e7obj.add_args('-r')

        zipcomplete = e7obj.run()
        return zipcomplete

    def extractWithPath(self, outdir:str, *filelist, create:bool=False) -> ZipComplete:
        """
        filelist can be a glob or a file name
        """

        self.__dirCheck(outdir, create)

        e7obj = Exec7za('x', self.zipfile, f'-o{outdir}')
        if filelist:
            e7obj.add_args(*filelist)
        e7obj.add_args('-r')

        zipcomplete = e7obj.run()
        return zipcomplete