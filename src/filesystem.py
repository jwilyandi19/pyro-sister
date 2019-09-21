import random
import os

class FileSystemServer(object):
    def __init__(self):
        pass

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


if __name__ == '__main__':
    k = FileSystemServer()
    print(k.get_greet('royyana'))
