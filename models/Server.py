from utilities.init import parse_arguments, initialize_socket, generate_keys


class Server:
    def __init__(self):
        """
        A constructor for a Server class object.
        """
        self.name, self.ip, self.port = parse_arguments()
        self.own_socket = initialize_socket(self.ip, self.port)
        self.pvt_key, self.pub_key = generate_keys()
        self.sockets = [self.own_socket]
        self.client_dict = {}  # Key: IP, Value: (name, shared_secret)

    def start(self):
        """
        Starts the server.
        @return: None
        """
