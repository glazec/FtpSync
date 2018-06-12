import leancloud

def server():
    leancloud.init("Y54bP9lNMxGU2qOADoutgBDs-9Nh9j0Va","kWVCNpFdceAEz12ybiET30Xo")
    leancloud.use_region("CN")
    erep = leancloud.Object.extend("erep")
    query = leancloud.Query("erep")
    query_result = query.get("5b1f3a0f7b1a02001a974eaa")
    ip = query_result.get("ip")
    port = query_result.get("port")
    # ip =erep.ip
    # port = erep.port:

    # ip = "49.83.25.218"
    # port = 37
    return[ip,port]

if __name__ == '__main__':
    print(server()[0])
    print(server()[1])

