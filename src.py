from ftplib import FTP
from ftplib import error_perm
import os
import shutil
import auxiliary
import time

class FtpSync(object):
    def __init__(self):
        self.ftp = FTP()
        a = auxiliary.server()
        self.ip = a[0]
        self.port = a[1]
        self.localFile = []
        self.localDir = []
        self.remoteDir = []
        self.remoteFile = []
        self.rootDir = os.getcwd()
        self.cwd = ""
        self.UncheckDir= []
        try:
            self.ftp.connect(self.ip, self.port)
            self.ftp.login()
            self.ftp.getwelcome()
            print("Successfully connected to 2erep ftp server")
        except Exception as e:
            print("try again later")

    def __del__(self):
        self.ftp.close()

    def syncSingleDir(self,nowdir):
        self.cwd = "/"

        # compare dir
        # compare file(extra or lack)
        # downlaod file(auxiliary)
        # delete file(auxiliary)
        # compare file size or hash
        # delete file with different size
        # download file
        # for i,j,k in os.walk(os.path.join(self.rootDir,nowdir),topdown=False):
        #     self.localDir.append(j)
        #     self.localFile.append(k)

        # update local index
        for i in os.listdir(os.path.join(self.rootDir,nowdir)):
            if os.path.isdir(i):
                self.localDir.append(i)
            else:
                self.localFile.append(i)

        self.ftp.cwd(nowdir)

        # update remote index
        temp = self.ftp.nlst()
        for i in temp:
            if self.isdir(i):
                self.remoteDir.append(i)
            else:
                self.remoteFile.append(i)

        # sync new dir
        for i in self.remoteDir:
            if i in self.localDir:
                pass
            else:
                os.mkdir(os.path.join(self.rootDir,nowdir,i))

        # rm extra dir
        # for i in self.localDir:
        #     if i in self.remoteDir:
        #         pass
        #     else:
        #         a = os.path.join(self.rootDir,nowdir)
        #         a = os.path.join(a,i)
        #         shutil.rmtree(a)

        # sync new file
        for i in self.remoteFile:
            if i in self.localFile:
                pass
            else:
                b = os.path.join(self.rootDir,nowdir)
                self.download(i,b)

        # remove extra file
        for i in self.localFile:
            if i in self.remoteFile or i in "src.py" or i in "auxiliary.py": #delete condition
                pass
            else:
                b = os.path.join(self.rootDir,nowdir)
                b = os.path.join(b,i)
                os.remove(b)
                print("remove "+i)

        # update outdated file
        for i in os.listdir(os.path.join(self.rootDir,nowdir)):
            if os.path.isdir(i) or i == "auxiliary.py" or i == "src.py" or i == "updater.exe": # delete condition
                pass
            else:
                self.comparesize(nowdir,i)
        self.ftp.cwd(self.cwd)

    def isdir(self,fileOrDir):
        try:
            self.ftp.cwd(fileOrDir)
            self.ftp.cwd("../")
            return True
        except error_perm as e:
            return False

    def download(self,filen,absnowdir):
        a = os.path.join(absnowdir,filen)
        self.ftp.retrbinary("RETR "+filen,open(a,'wb').write)
        print("finished downlaoding "+ filen+" into "+ absnowdir)

    def comparesize(self,nowdir,filname):
        a = os.path.join(self.rootDir,nowdir)
        b = os.path.join(a,filname)
        c = os.path.join(nowdir,filname)
        #if os.path.getsize(b) != self.ftp.size(os.path.join(nowdir,filname)):
        if os.path.getsize(b)!= self.ftp.size(filname):
            os.remove(b)
            self.download(filname,a)

if __name__ == '__main__':
    # erep=FtpSync()
    ere = FtpSync()
    ere.syncSingleDir("")
    # print("finish ")
    # time.sleep()
    ere.syncSingleDir("addons/")
    ere.syncSingleDir("optional/")
