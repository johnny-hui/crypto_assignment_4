from models.Server import Server
from utilities.init import parse_arguments

if __name__ == '__main__':
    name, src_ip, src_port = parse_arguments()
    server = Server()
    server.start()
