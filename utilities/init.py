import getopt
import ipaddress
import secrets
import socket
import sys
from _socket import SO_REUSEADDR, SOL_SOCKET
from tinyec import registry
from utilities.constants import INVALID_SRC_IP_ARG_ERROR, INVALID_SRC_PORT_RANGE, \
    INVALID_FORMAT_SRC_PORT_ARG_ERROR, MIN_PORT_VALUE, MAX_PORT_VALUE, MODE_SERVER
from utilities.utility import compress


def parse_arguments():
    """
    Parse the command line for arguments.

    @return name, src_ip, src_port:
        Strings containing name, source IP address and source port
    """
    # Initialize variables
    name, src_ip, src_port = "", "", ""
    arguments = sys.argv[1:]
    opts, user_list_args = getopt.getopt(arguments, 'n:s:p:')

    if len(opts) == 0:
        sys.exit("[+] INIT ERROR: No arguments were provided!")

    for opt, argument in opts:
        if opt == '-n':  # For name
            name = argument

        if opt == '-s':  # For source IP
            try:
                src_ip = str(ipaddress.ip_address(argument))
            except ValueError as e:
                sys.exit(INVALID_SRC_IP_ARG_ERROR.format(e))

        if opt == '-p':  # For source port
            try:
                src_port = int(argument)
                if not (MIN_PORT_VALUE <= src_port < MAX_PORT_VALUE):
                    sys.exit(INVALID_SRC_PORT_RANGE)
            except ValueError as e:
                sys.exit(INVALID_FORMAT_SRC_PORT_ARG_ERROR.format(e))

    # Check if parameters are provided
    if len(name) == 0:
        sys.exit("[+] INIT ERROR: A name was not provided! (-n option)")
    if len(src_ip) == 0:
        sys.exit("[+] INIT ERROR: A source IP was not provided! (-s option)")
    if len(str(src_port)) == 0:
        sys.exit("[+] INIT ERROR: A source port was not provided! (-p option)")

    return name, src_ip, src_port


def initialize_socket(ip: str, port: int):
    """
    Creates and initializes a Socket object.

    @param ip:
        The IP address of the Node

    @param port:
        The port number of the Node

    @return: None
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((ip, port))
        sock.listen(5)  # Listen for incoming connections (maximum 5 clients in the queue)
        print(f"[+] Socket has been initialized and is now listening on {ip} | (Port {port})")
        return sock
    except socket.error as e:
        sys.exit("[+] INIT ERROR: An error has occurred while creating socket object ({})".format(e))


def generate_keys(mode: str):
    """
    Generates a public/private key pair using
    the brainpool256r1 elliptic curve.

    @param mode:
        A string that declares whether calling class is
        a 'Server' or 'Client'

    @return: private_key, public_key
    """
    # Define BrainPool 256-bit Elliptic Curve
    curve = registry.get_curve('brainpoolP256r1')

    # Generate Private Key (a random int from [1, n-1])
    private_key = secrets.randbelow(curve.field.n)

    # Generate Public Key (a * G)
    public_key = private_key * curve.g
    print("[+] ECDH Private/Public Key pairs have been successfully generated!")

    if mode == MODE_SERVER:
        print(f"[+] Server private key: {hex(private_key)}")
        print(f"[+] Server public key: {compress(public_key)}")
    else:
        print(f"[+] Client private key: {hex(private_key)}")
        print(f"[+] Client public key: {compress(public_key)}")

    return private_key, public_key
