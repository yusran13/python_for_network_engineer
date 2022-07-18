import os
from dotenv import load_dotenv
load_dotenv()

# os.environ["NTC_TEMPLATES_DIR"] = 
# os.environ["NET_TEXTFSM"] = 

def get_device_conn(ip_address):

    device_conn = {
        'device_type': 'cisco_xr',
        'host': ip_address,
        'username': os.getenv('PE_USER'),
        'password': os.getenv('PE_KEY'),
        'fast_cli': False,
        'ssh_config_file': os.getenv('SSH_CONFIG_FILE'),
        'conn_timeout': 40,
        'banner_timeout': 40
    }

    return device_conn