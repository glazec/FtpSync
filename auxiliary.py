from ftplib import FTP
import shutil
import leancloud

def server():
    try:
        leancloud.init("Y54bP9lNMxGU2qOADoutgBDs-9Nh9j0Va","kWVCNpFdceAEz12ybiET30Xo")
        leancloud.use_region("CN")
        erep = leancloud.Object.extend("erep")
        query = leancloud.Query("erep")
        query_result = query.get("5b1f3a0f7b1a02001a974eaa")
        ip = query_result.get("ip")
        port = query_result.get("port")
        return[ip,port]
    except Exception as e:
        a = input("Network error\nPlease type in the server ip form the QQ chat group:\n")

    # ip =erep.ip
    # port = erep.port:

    # ip = "49.83.25.218"
    # port = 37
        return[str(a.split(":")[0]),int(a.split(":")[-1])]

if __name__ == '__main__':
    print(server())


