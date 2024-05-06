MIN_PORT_VALUE = 1
MAX_PORT_VALUE = 65536
INVALID_SRC_IP_ARG_ERROR = ("[+] INIT ERROR: Invalid format for the source IP address was provided "
                            "(-s option): {}")
INVALID_SRC_PORT_RANGE = ("[+] INIT ERROR: The value provided for source port (-p option) is not "
                          "valid: (not between 1 and 65535)")
INVALID_FORMAT_SRC_PORT_ARG_ERROR = "[+] INIT ERROR: Invalid format provided for the source port (-p option): {}"


INIT_SERVER_MSG = "[+] Now initializing the server..."
INIT_CLIENT_MSG = "[+] Now initializing the client..."
INIT_SUCCESS_MSG = "[+] Initialization Successful!"


MODE_SERVER = "SERVER"
MODE_CLIENT = "CLIENT"


MIN_MENU_ITEM_VALUE = 1
MAX_MENU_ITEM_VALUE = 3
MENU_TITLE = "Menu Options"
MENU_FIELD_OPTION = "Option"
MENU_FIELD_DESC = "Description"
INPUT_PROMPT = "[+] Select a menu option: "
CLIENT_MENU_OPTIONS_LIST = [
    ["1", "Connect to a Server"],
    ["2", "View Current Connection"],
    ["3", "Disconnect (Close Application)"]
]
SERVER_MENU_OPTIONS_LIST = [
    ["1", "Send Message to a Client"],
    ["2", "View Current Connections"],
    ["3", "Disconnect (Close Application)"]
]
SEND_MESSAGE_OPTION = ["1", "Send Message to Server"]
INVALID_MENU_SELECTION = "[+] MENU SELECTION: Please enter a valid menu option ({} to {}): "
INVALID_INPUT_MENU_ERROR = "[+] ERROR: Invalid input was provided to menu: {}"
MENU_ACTION_START_MSG = "\n[+] ACTION SELECTED: Now performing menu item {}..."


CONNECTION_INFO_TITLE = "Current Connections"
CONNECTION_INFO_FIELD_NAME = "Name"
CONNECTION_INFO_FIELD_IP = "IP Address"
CONNECTION_INFO_FIELD_SECRET = "Shared Secret"
CONNECTION_INFO_FIELD_IV = "Initialization Vector (IV)"
