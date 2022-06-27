from operator import ne
from netmiko import ConnectHandler

device_conn = {
        'device_type': 'cisco_xr',
        'host': "114.1.201.13",
        'username': 'cisco',
        'password': "!1s4tmpl5!",
        'conn_timeout': 40,
        'banner_timeout': 40,
        'fast_cli': False,
        'ssh_config_file': '/home/yusran/.ssh/proxy_epnm',
    }

net_connect = ConnectHandler(**device_conn)
print("Connected")

show_interfaces = net_connect.send_command("show ip int brief")
print(show_interfaces)
# show_interfaces = net_connect.send_command("show ip int brief", use_textfsm=True, delay_factor=100)



net_connect.disconnect()
print(show_interfaces)
