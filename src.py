from ftplib import FTP
import os

import auxiliary
class FtpSync(object):
    def __init__(self):
        self.ftp = FTP()
        self.ip = auxiliary.ip()
        self.port = auxiliary.port()
        try:
            self.ftp.connect(self.ip(), self.port())
            self.ftp.login()
            self.ftp.getwelcome()
        except Exception as e:
            print("try again later")
        finally:
            print("Successfully connected to 2erep ftp server")

    def __del__(self):
        self.ftp.close()

    def download(self):
        self.ftp.retrbinary("RETR"+self.downloadFile,open(localDir+downloadFile,'wb').write)

if __name__ == '__main__':
    erep=FtpSync()
