import Pyro4

def start_server():
    uri = "PYRONAME:filesystemserver@localhost:7777"
    fileServer = Pyro4.Proxy(uri)
    print(fileServer.get_greet('Bolang'))
    return fileServer

def upload_file(file_name, srvr):
    with open(file_name) as f:
        content = f.read()
        return srvr.createFile(content, file_name)


if __name__=='__main__':
    server = start_server()

    print("Menu list:")
    print("1. Upload file: UPLOAD <file_name>")

    while True:
        query = input("\n>>")
        query1 = query.split()

        if query1[0] == 'UPLOAD':
            res = upload_file(query1[1], server)
            print(res)


