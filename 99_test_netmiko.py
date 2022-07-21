from netmiko import ConnectHandler
from pprint import pprint
from list_target_ip import list_ip
from device_driver import get_device_conn



with open('config_acl_nso.txt') as f:
    nso_acl_config = f.read().splitlines()

for ip in list_ip:
    print(f"Processing IP Address {ip}")
    device_conn = get_device_conn(ip_address=ip)
    net_connect = ConnectHandler(**device_conn)
    print("Connected")

    #SEND COMMAND ONE LINE
    # output = net_connect.send_command("show run router bgp 4761  neighbor-group AN | in route-policy")
    # output_split = output.split("\n")
    # print(output_split)
    
    # if len(output_split)<3:
    #     net_connect.send_config_set(["ipv4 access-list ACL_SNMP_MANAGEMENT", "permit ipv4 10.34.28.16/28 any"])
    #     net_connect.commit()
    #     print(f"Success commit {ip}")
    #     net_connect.disconnect()
    # else:
    #     print(f"ACL Solarwind at Router {ip} is been applied")

    # #SEND COMMAND MULTIPLE LINE
    # net_connect.send_config_set(nso_acl_config)

    #GET OUTPUT COMMAND WITHOUT PARSING
    # output = net_connect.send_command("show interface brief")
    # pprint(output)

    #GET OUTPUT COMMAND WITH TEXTFSM PARSING
    output = net_connect.send_command("show interface brief", use_textfsm=True)
    pprint(output)
    
    print('=================================================')
