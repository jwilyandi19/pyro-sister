from src.filesystem import  *
import Pyro4

def start():
    #name server harus di start dulu dengan  pyro4-ns -n localhost -p 7777
    #gunakan URI untuk referensi name server yang akan digunakan
    #untuk mengecek service apa yang ada di ns, gunakan pyro4-nsc -n localhost -p 7777 list
    daemon = Pyro4.Daemon(host="localhost")
    ns = Pyro4.locateNS("localhost",7777)
    x_FileSystemServer = Pyro4.expose(FileSystemServer)
    uri_FileSystemServer = daemon.register(x_FileSystemServer)
    print("URI File System Server : ", uri_FileSystemServer)
    ns.register("filesystemserver", uri_FileSystemServer)
    daemon.requestLoop()


if __name__ == '__main__':
    start()
