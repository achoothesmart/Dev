import os

class FileHandler:
    _fileName = ''
    _filePath = ''
    def __init__(self, fileName: str, filePath: str) -> None:
        self._fileName = fileName
        self._filePath = filePath
    
    def desc(self):
        print(self._fileName, self._filePath)
    
    def getFilePath(self):
        return os.path.join(self._filePath, self._fileName)

    def isCreated(self):
        return os.path.exists(self.getFilePath())
    
    def createFile(self):
        if not self.isCreated():
            with open(self.getFilePath(), mode='w') as f:
                f.close()
                print(f'File created: {self.getFilePath()}')
        else:
            print(f'File already created: {self.getFilePath()}')
    
    def deleteFile(self):
        if self.isCreated():
            os.remove(self.getFilePath())
            print(f'File removed: {self.getFilePath()}')
        else:
            print(f"File doesn't exists: {self.getFilePath()}")

fh = FileHandler(fileName='new.txt', filePath='z:\\temp')
fh.createFile()
fh.createFile()
fh.deleteFile()
fh.deleteFile()