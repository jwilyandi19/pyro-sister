import Pyro4
import base64
import json
import sys
import os

namainstance = sys.argv[1]

def get_fileserver_objects():
    uri = []
    fserver = []
    print("CHECK")
    for i in range(0,3):
        uri.append("PYRONAME:{}@localhost:7777" . format("fileserver" + str(i+1)))
        fserver.append(Pyro4.Proxy(uri[i]))

    return fserver

def get_fileserver_object():
    uri = "PYRONAME:{}@localhost:7777" . format(namainstance)
    fserver = Pyro4.Proxy(uri)
    return fserver

def create(file_name,fss):
    print("File {} has been created".format(file_name))
    for fs in fss:
        fs.create(file_name)

def update(file_name,fss):
    print("File {} has been updated".format(file_name))
    for fs in fss:
        fs.update(file_name,content = open(file_name,'rb+').read())

def delete(file_name,fss):
    print("File {} has been deleted".format(file_name))
    for fs in fss:
        fs.delete(file_name)

def read(file_name,f):
    return f.read(file_name)



if __name__=='__main__':
    fss = get_fileserver_objects()
    f = get_fileserver_object()

    print("UPLOAD: upload <file_name>")
    print("DOWNLOAD: download <file_name>")
    print("DELETE: delete <file_name>")
    print("LIST: ls")
    print("EXIT: exit")

    is_connected = True

    while is_connected:
        query = input(">>")
        query_input = query.split()

        if(query_input[0]=="upload"):
            create(query_input[1],fss)
            update(query_input[1],fss)

        elif(query_input[0]=="delete"):
            delete(query_input[1],fss)

        elif(query_input[0]=="download"):
            con = read(query_input[1],f)
            filename,ext = os.path.splitext(query_input[1])
            open(filename + '-kembali' + ext, 'w+b').write(base64.b64decode(con['data']))

        elif(query_input[0]=="ls"):
            print(f.list())

        elif(query_input[0]=="exit"):
            is_connected = False


    #f.create('slide1.pdf')
    #f.update('slide1.pdf', content = open('slide1.pdf','rb+').read() )

    #f.create('slide2.pptx')
    #f.update('slide2.pptx', content = open('slide2.pptx','rb+').read())

    #print(f.list())
    #d = f.read('slide1.pdf')
    #kembalikan ke bentuk semula ke dalam file name slide1-kembali.pdf
    #open('slide1-kembali.pdf','w+b').write(base64.b64decode(d['data']))

    #k = f.read('slide2.pptx')
    #kembalikan ke bentuk semula ke dalam file name slide2-kembali.pptx
    #open('slide2-kembali.pptx','w+b').write(base64.b64decode(k['data']))

    #f.create('pesugihan.txt')
    #f.update('pesugihan.txt', content=open('pesugihan.txt', 'rb+').read())

    #d = f.read('pesugihan.txt')
    #open('pesugihan-returned.txt','w+b').write(base64.b64decode(d['data']))
