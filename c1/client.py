import Pyro4
import base64
import json
import sys
import os

namainstance = sys.argv[1] or "fileserver"

def get_fileserver_object():
    uri = "PYRONAME:{}@localhost:7777" . format(namainstance)
    fserver = Pyro4.Proxy(uri)
    return fserver

def download(file_name, obj):
    try:
        content = obj.read(file_name)
        file_nama, ext = os.path.splitext(file_name)
        open(file_nama + '-downloaded' + ext,'w+b').write(base64.b64decode(content['data']))
        print("File has been downloaded")
    except FileNotFoundError:
        print("File not found")

def upload(file_name, obj):
    obj.create(file_name)
    obj.update(file_name, content = open(file_name, 'rb+').read())
    print("File has been uploaded")

def listdir(obj):
    print(obj.list())

if __name__=='__main__':
    f = get_fileserver_object()

    print("UPLOAD: up <file_name>")
    print("DOWNLOAD: dwnld <file_name>")
    print("LIST: ls")

    is_conn = True
    while is_conn:
        inputquery = input(">> ")
        query = inputquery.split()

        if query[0] == 'up':
            upload(query[1],f)
        elif query[0] == 'dwnld':
            download(query[1],f)
        elif query[0] == 'ls':
            listdir(f)
        elif query[0] == 'exit':
            print("Exiting...")
            is_conn = False





