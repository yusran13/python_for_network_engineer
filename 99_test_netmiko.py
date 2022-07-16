from netmiko import ConnectHandler
import pprint
from list_target_ip import *

device_conn = {
    'device_type': 'cisco_xr',
    'username': 'XXXXXXX',
    'password': "XXXXXXX",
    'conn_timeout': 40,
    'banner_timeout': 40,
    'fast_cli': False,
    'ssh_config_file': '/home/yusran/.ssh/proxy_epnm',
}

with open('config_acl_nso.txt') as f:
    nso_acl_config = f.read().splitlines()

for ip in list_ip:
    print(f"Processing IP Address {ip}")
    device_conn['host'] = ip
    net_connect = ConnectHandler(**device_conn)
    print("Connected")

    #SEND COMMAND ONE LINE
    # output = net_connect.send_command("show run router bgp 4761  neighbor-group AN | in route-policy")
    output = net_connect.send_command("show run ipv4 access-list ACL_SNMP_MANAGEMENT | in 10.34.28.16", use_textfsm=True, delay_factor=100)
    

    output_split = output.split("\n")
    print(output_split)
    
    if len(output_split)<3:
        net_connect.send_config_set(["ipv4 access-list ACL_SNMP_MANAGEMENT", "permit ipv4 10.34.28.16/28 any"])
        net_connect.commit()
        print(f"Success commit {ip}")
        net_connect.disconnect()
    else:
        print(f"ACL Solarwind at Router {ip} is been applied")
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(show_interfaces)

    #SEND COMMAND MULTIPLE LINE
    net_connect.send_config_set(nso_acl_config)

    print('=================================================')
