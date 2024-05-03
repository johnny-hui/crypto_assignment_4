from utilities.init import parse_arguments, initialize_socket


class Server:
    def __init__(self):
        """
        A constructor for a Server class object.
        """
        self.name, self.ip, self.port = parse_arguments()
        self.own_socket = initialize_socket(self.ip, self.port)
        # TODO: Make public/private key pair
        self.sockets = [self.own_socket]
        self.client_info = {}  # Key: IP, Value: Name

    def start(self):
        """
        Starts the server.
        @return: None
        """