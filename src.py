from ftplib import FTP
from ftplib import error_perm
import os
import shutil
import auxiliary


class FtpSync(object):
    def __init__(self):
        self.ftp = FTP()
        self.ip = auxiliary.server()[0]
        self.port = auxiliary.server()[1]
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
        #for i in os.listdir(os.path.join(self.rootDir, nowdir)):
        for i in os.listdir(self.rootDir+nowdir):
            if os.path.isdir(i):
                self.localDir.append(i)
            else:
                self.localFile.append(i)

        #self.ftp.cwd(nowdir)
        temp = self.ftp.nlst(nowdir) ## just use nowdir
        for i in temp:
            if self.isdir(i):
                self.remoteDir.append(i)
            else:
                self.remoteFile.append(i)

        for i in self.remoteDir:
            if i in self.localDir:
                pass
            else:
                os.mkdir(self.rootDir+nowdir+"/"+i)

        for i in self.localDir:
            if i in self.remoteDir:
                pass
            else:
                a = os.path.join(self.rootDir,nowdir)
                a = os.path.join(a,i)
                a = self.rootDir+nowdir+"/"+i
                shutil.rmtree(a)

        for i in self.remoteFile:
            try:
                a = i.split("/")[-1]
            except Exception as e:
                a = i
            if a in self.localFile:
                pass
            else:
                b = self.rootDir+"/"
                self.download(i,b)

        temp = []
        for k in self.remoteFile:
            try:
                temp.append(k.split("/")[-1])
            except Exception as e:
                temp.append(k)
        for i in self.localFile:
            if i in temp or i in "src.py" or i in "auxiliary.py" or i in "glaze.exe":
                pass
            else:
                #b = os.path.join(self.rootDir,nowdir)
                #b = os.path.join(b,i)
                b = self.rootDir+nowdir+"/"+i
                os.remove(b)
                print("remove "+i)

        for i in os.listdir(self.rootDir+nowdir):
            if os.path.isdir(i) or i == "auxiliary.py" or i == "src.py" or i == "glaze.exe":
                pass
            else:
                self.comparesize(nowdir,i)
        # just for the simple
        self.remoteFile=[]
        self.remoteDir=[]
        self.localFile=[]
        self.localDir=[]

    def isdir(self,fileOrDir):
        try:
            self.ftp.cwd(fileOrDir)
            self.ftp.cwd("../")
            return True
        except error_perm as e:
            return False


    def download(self,filen,absnowdir):
        a = absnowdir+filen
        self.ftp.retrbinary("RETR "+filen,open(a,'wb').write)
        print("download "+filen+" successfully")

    def comparesize(self,nowdir,filname):
        #a = os.path.join(self.rootDir,nowdir)
        #b = os.path.join(a,filname)
        b = self.rootDir+nowdir+"/"+filname
        if os.path.getsize(b) != self.ftp.size(os.path.join(nowdir,filname)):
            os.remove(b)
            self.download(filname,self.rootDir+nowdir+"/")

if __name__ == '__main__':

    # for i,j in erep.ftp.mlsd(["folder"]):
    #     print(i+j)
    # for i in erep.ftp.nlst("folder"):
        #     print(i)
        # print(os.path.(i))
        # print("----")
    # print(erep.ftp.cwd("/wget.exe"))
    # print(erep.ftp.cwd("../"))
    # print(erep.ftp.pwd())
    # print(erep.ftp.nlst())
    #print(erep.rootDir)d_finger.pbo
    print("----------------------------")
    print("this is a demo version made by liuli")
    print("For source code, visit my gihub\n https://github.com/kismet-cruz/FtpSync")
    print("-----------------------------")
    ab = FtpSync()
    ab.syncSingleDir("")
    ab.syncSingleDir("/addons")
    ab.syncSingleDir("/optional")


