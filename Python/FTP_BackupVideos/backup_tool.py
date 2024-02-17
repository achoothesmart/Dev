import os
from Modules.ftp_client import FTPClient
from Modules.vide_compressor import VideoCompressor

class BackupTool:

    # Inputs 
    Folder_Original = 'Z:/Temp/Original'
    Folder_Compressed = 'Z:/Temp/Compressed'
    host = '192.168.29.164'
    port=1111
    user = 'pc'
    pwd = '123456'
    SourceFolder = '/device/DCIM/Camera/'

    def CreateFolders(self, path: str):
        if not os.path.exists(path):
            os.makedirs(path)
            print(f'Folder {path} created')
        else:
            print(f'Folder {path} already exists')

if __name__ == '__main__':
    btool = BackupTool()
    btool.CreateFolders(btool.Folder_Original)
    btool.CreateFolders(btool.Folder_Compressed)
    # ftpClient = FTPClient(host=btool.host, port=btool.port, username=btool.user, password=btool.pwd)
    # ftpClient.CopyFilesFromFTPSource(FTP_SourceLocation=btool.SourceFolder,
    #                                  LocalDestinationPath=btool.Folder_Original,
    #                                  FilterInExtns=['mp4'])
    # print('Backup complete!')


    vc = VideoCompressor()
    vc.CompressVideosFromFolder(SourceFolderPath=btool.Folder_Original,
                                DestinationFolderPath=btool.Folder_Compressed,
                                CompressionPercentage=60)
    
    # vc.CompressVideosFromFolder(SourceFolderPath=btool.Folder_Compressed,
    #                             DestinationFolderPath=None,
    #                             CompressionPercentage=None)
    print('Compression Complete!')
