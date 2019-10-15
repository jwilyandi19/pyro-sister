import random
import os
import time

class FileSystemServer(object):
    def __init__(self):
        pass

    def send_heartbeat(self):
        return "I'm alive..."

    def get_greet(self, name='NoName'):
        lucky_number = random.randint(1, 100000)
        return "Hello {}, this is your lucky number {}".format(name, lucky_number)

    def createFile(self, content, file_name):
        print("Uploading {}...".format(file_name))
        path = "file_system/{}".format(file_name)
        if os.path.exists(path):
            return "File {} already exist".format(file_name)
        else:
            with open(path, "w+") as f:
                f.write(content)
            return "File {} has been uploaded".format(file_name)

    def readFile(self, file_name):
        print("Reading {}...".format(file_name))
        path = "file_system/{}".format(file_name)

        if not os.path.exists(path):
            return "File {} is not exist".format(file_name)
        else:
            with open(path) as f:
                content = f.read()
                return content

    def updateFile(self, content, file_name):
        print("Updating {}...".format(file_name))
        path = "file_system/{}".format(file_name)

        if not os.path.exists(path):
            return "File {} is not exist".format(file_name)
        else:
            with open(path, "w+") as f:
                f.write(content)
            return "File {} has been updated".format(file_name)

    def deleteFile(self, file_name):
        print("Deleting {}...".format(file_name))
        path = "file_system/{}".format(file_name)

        if not os.path.exists(path):
            return "File {} is not exist".format(file_name)
        else:
            os.remove(path)
            return "File {} has been deleted".format(file_name)

    def listFile(self):
        time.sleep(3.0)
        print("Listing...")
        path = "file_system/"

        files = []
        for root,dirs,files in os.walk(path):
            return files




if __name__ == '__main__':
    k = FileSystemServer()
    print(k.get_greet('royyana'))
