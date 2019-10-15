import Pyro4, Pyro4.errors
import threading as tred
import time

class HBThread(tred.Thread):
    def __init__(self, srvr):
        tred.Thread.__init__(self)
        self.srvr = srvr
        self._stop_event = tred.Event()
        self.exception = None

    def run(self):
        while not self.exiting():
            try:
                self.srvr.send_heartbeat()
            except Pyro4.errors.TimeoutError as e:
                print("Thread: Timeout. Press enter to exit")
                self.exception = e
                break
            except Pyro4.errors.ConnectionClosedError as e:
                print("Thread: No Heartbeat. Press enter to exit")
                self.exception = e
                break

    def get_exception(self):
        return self.exception

    def stop(self):
        self._stop_event.set()

    def exiting(self):
        return self._stop_event.is_set()


def start_server():
    uri = "PYRONAME:filesystemserver@localhost:7777"
    fileServer = Pyro4.Proxy(uri)
    fileServer._pyroTimeout = 5.0
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
    print(srvr)
    return srvr.listFile()


if __name__=='__main__':
    server = start_server()
    running = True
    thread = HBThread(server)
    server._pyroTimeout = 2.0
    thread.start()

    print("Simple file system. Only for file upload purpose. ")
    print("Menu list:")
    print("1. Upload file: UPLOAD <file_name>")
    print("2. Read File: READ <file_name>")
    print("3. Update File: UPDATE <file_name>")
    print("4. Delete File: DELETE <file_name>")
    print("5. List File: LIST")
    print("6. Exit program: EXIT")
    while running:
        try:
            query = input("\n>> ")
            query1 = query.split()
            if thread.get_exception():
                raise thread.get_exception()
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
        except Pyro4.errors.CommunicationError:
            print("Server disconnected. Exiting...")
            running = False
        except KeyboardInterrupt:
            print("Exiting...")
            running = False



