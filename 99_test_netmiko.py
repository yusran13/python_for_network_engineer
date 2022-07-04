from netmiko import ConnectHandler
import pprint

list_ip = [
    "114.1.201.13",
    "114.1.201.88",
    "114.1.215.16",
]

device_conn = {
    'device_type': 'cisco_xr',
    'username': 'cisco',
    'password': "!1s4tmpl5!",
    'conn_timeout': 40,
    'banner_timeout': 40,
    'fast_cli': False,
    'ssh_config_file': '/home/yusran/.ssh/proxy_epnm',
}

for ip in list_ip:
    print(f"Processing IP Address {ip}")
    device_conn['host'] = ip
    net_connect = ConnectHandler(**device_conn)
    print("Connected")

    # output = net_connect.send_command("show run router bgp 4761  neighbor-group AN | in route-policy")
    show_interfaces = net_connect.send_command("show ospf neighbor", use_textfsm=True, delay_factor=100)
    print(show_interfaces)

    # if "No such configuration item(s)" in output:
    #     print("Router ini belum ada config neighbor-group AN")
    net_connect.disconnect()
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(show_interfaces)

    print('=================================================')
