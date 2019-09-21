import Pyro4

def test_with_ns():
    uri = "PYRONAME:filesystemserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('Bolang'))

if __name__=='__main__':
    test_with_ns()
