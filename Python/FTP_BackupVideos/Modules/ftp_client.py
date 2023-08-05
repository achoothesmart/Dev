from ftplib import FTP
import os

class FTPClient:

    ftp = None

    def __init__(self, host: str, port: int, username: str, password: str) -> None:
        self.ftp = FTP()
        self.ftp.connect(host=host, port=port)
        self.ftp.login(user=username, passwd=password)
        

    def __download_file_from_ftp(self, ftp, remote_file_path, local_file_path):
        with open(local_file_path, 'wb') as local_file:
            ftp.retrbinary('RETR ' + remote_file_path, local_file.write)

    def CopyFilesFromFTPSource(self, FTP_SourceLocation: str, LocalDestinationPath: str, FilterInExtns: list = []):
        self.ftp.cwd(FTP_SourceLocation)
        file_list = []
        self.ftp.retrlines('LIST', lambda x: file_list.append(x.split()[-1]))  # Retrieve the list of filenames
        # print("Files in the current directory:")
        # print(file_list)
        # first_file = file_list[0]

        try:
            
            if len(FilterInExtns)>0: 
                file_list = [ftp_file 
                             for ftp_file in file_list
                             if ftp_file.split('.')[1].lower() in [extn.lower() for extn in FilterInExtns]
                             ]
                
            for idx, ftp_file in enumerate(file_list):
                    remote_file_path = f'{FTP_SourceLocation}{ftp_file}'
                    local_file_path = os.path.join(LocalDestinationPath, ftp_file)  

                    try:
                        # Download the file from the FTP server to the local machine
                        self.__download_file_from_ftp(self.ftp, remote_file_path, local_file_path)
                        print(f"({idx+1}/{len(file_list)}) File downloaded: '{local_file_path}'")

                    except Exception as e:
                        print(f"Error: {str(e)}")

        except Exception as e:
            print(f"Error: {str(e)}")

        finally:
            # Close the FTP connection
            self.ftp.quit()
    
    # ftp.dir()

    

if __name__ == '__main__':
    print('This is a lib file!')