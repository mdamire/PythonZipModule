import re

from .zipcomplete import ZipComplete

class ZipList():

    def __init__(self, zipcomplete: ZipComplete) -> None:
        fileList = []
        fileListFull = []
        self._extractInfo(zipcomplete.get_stdout(), fileList, fileListFull)

        self.fileList = fileList
        self.fileListFull = fileListFull
        self.zipcomplete = zipcomplete


    def _extractInfo(self, msg, fileList, fileListFull) -> None:
        flg = False
        for line in msg.split('\n'):
            if re.match(r'^------.*$', line):
                if flg:
                    flg = False
                else: 
                    flg = True
            elif flg:
                splited = re.split(r'\s+', line, 5)
                fileListFull.append(tuple(splited))
                fileList.append(splited[5])
            
                
    
    def get_fileList(self, regex:str='') -> list:
        if regex:
            filteredlist = [ i for i in self.fileList if re.search(regex, i)]
            return filteredlist
        return self.fileList

    def get_fileListFull(self, regex:str='') -> list:
        if regex:
            filteredlist = [ i for i in self.fileListFull if re.search(regex, i[5])]
            return filteredlist
        return self.fileListFull

    def get_zipComplete(self) -> ZipComplete:
        return self.zipcomplete
