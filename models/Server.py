import select

from utilities.constants import INIT_SERVER_MSG, INIT_SUCCESS_MSG, MODE_SERVER, INPUT_PROMPT
from utilities.init import parse_arguments, initialize_socket, generate_keys
from utilities.utility import accept_new_connection_handler, display_menu


class Server:
    """A class representing the server

    Attributes:
        ip - The ip address
        port - The port number
        name - The name of the server
        own_socket - The socket object for the server
        pvt_key - The private key generated by ECDH (via. brainpoolP256r1)
        pub_key - The public key generated by ECDH (via. brainpoolP256r1)
        sockets - A list containing sockets to monitor (using select() function)
        client_dict - A dictionary containing information about each connected client{IP: (name, shared secret key, IV)}
    """
    def __init__(self):
        """
        A constructor for a Server class object.
        """
        print(INIT_SERVER_MSG)
        self.name, self.ip, self.port = parse_arguments()
        self.own_socket = initialize_socket(self.ip, self.port)
        self.pvt_key, self.pub_key = generate_keys(mode=MODE_SERVER)
        self.sockets = [self.own_socket]
        self.client_dict = {}  # Format {IP: [name, shared_secret, IV]}
        print(INIT_SUCCESS_MSG)

    def start(self):
        """
        Starts the server and monitors any incoming connections
        and messages from existing clients.

        @return: None
        """
        print("=" * 80)
        display_menu(is_server=False)
        print(INPUT_PROMPT)

        while True:
            readable, _, _ = select.select(self.sockets, [], [])

            for sock in readable:
                # Accept a new connection and exchange keys
                if sock is self.own_socket:
                    accept_new_connection_handler(self.pvt_key, self.pub_key, self.own_socket,
                                                  self.sockets, self.client_dict)
                else:
                    data = sock.recv(1024)
                    if data:
                        print("[+] Received data: ", data.decode())
                    else:
                        print("[+] Connection closed by client: ", sock.getpeername())
                        self.sockets.remove(sock)
                        sock.close()

