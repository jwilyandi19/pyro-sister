import Pyro4, Pyro4.errors
import sys

def start_server():
    uri = "PYRONAME:filesystemserver@localhost:7777"

    fileServer = Pyro4.Proxy(uri)
    fileServer._pyroTimeout = 3.0
    return fileServer

#untuk UPLOAD
def upload_file(file_name, srvr):
    with open(file_name) as f:
        content = f.read()
        return srvr.createFile(content, file_name)

#untuk READ
def read_file(file_name, srvr):
    return srvr.readFile(file_name)

#untuk UPDATE
def update_file(file_name, srvr):
    with open(file_name) as f:
        content = f.read()
        return srvr.updateFile(content, file_name)

#untuk DELETE
def delete_file(file_name, srvr):
    return srvr.deleteFile(file_name)

#untuk LIST
def list_file(srvr):
    return srvr.listFile()


if __name__=='__main__':
    server = start_server()

    try:
        server.ack()
    except  Pyro4.errors.TimeoutError:
        print("Server Timeout. Exiting...")
        sys.exit()

    print("Simple file system. Only for file upload purpose. ")
    print("Menu list:")
    print("1. Upload file: UPLOAD <file_name>")
    print("2. Read File: READ <file_name>")
    print("3. Update File: UPDATE <file_name>")
    print("4. Delete File: DELETE <file_name>")
    print("5. List File: LIST")
    print("6. Exit program: EXIT")
    running = True
    while running:
        try:
            server.ack()
            query = input("\n>> ")
            query1 = query.split()
            if query1[0] == 'UPLOAD':
                res = upload_file(query1[1], server)
                print(res)
            elif query1[0] == 'READ':
                res = read_file(query1[1],server)
                print(res)
            elif query1[0] == 'UPDATE':
                res = update_file(query1[1], server)
                print(res)
            elif query1[0] == 'DELETE':
                res = delete_file(query1[1], server)
                print(res)
            elif query1[0] == 'LIST':
                files = list_file(server)
                for filename in files:
                    print(filename)
            elif query1[0] == 'EXIT':
                print("Exiting...")
                running = False
            else:
                print("Query does not exist. Please try listed query")
        except Pyro4.errors.TimeoutError:
            print("Server Timeout. Exiting...")
            running = False
        except  Pyro4.errors.ConnectionClosedError:
            print("Connection error. Exiting...")
            running = False
        except KeyboardInterrupt:
            print("Exiting...")
            running = False



