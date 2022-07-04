from netmiko import ConnectHandler
import pprint

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

# show_interfaces = net_connect.send_command("show ip int brief")

show_interfaces = net_connect.send_command("show ip int brief", use_textfsm=True, delay_factor=100)



net_connect.disconnect()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(show_interfaces)
