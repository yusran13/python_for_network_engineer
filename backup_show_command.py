import pprint, time
from netmiko import ConnectHandler
from list_target_ip import *

device_conn = {
    'device_type': 'cisco_xr',
    'username': 'XXXXXX',
    'password': "XXXXXX",
    'conn_timeout': 40,
    'banner_timeout': 40,
    'fast_cli': False,
    'ssh_config_file': '/home/yusran/.ssh/proxy_epnm',
    # 'session_log': 'backup_show_command/tets_backup_show_command.txt'
}

with open('show_command_list.txt') as f:
    show_command_list = f.read().splitlines()

for ip in list_ip:
    print(f"Processing IP Address {ip}")
    device_conn['host'] = ip
    net_connect = ConnectHandler(**device_conn)
    print("Connected")
    filename = f"backup_show_command/{ip}.txt"
    with open(filename, "w") as f:
        for command in show_command_list:
            f.write("=" * 20)
            f.write(command)
            f.write("=" * (80 - len(command)))
            f.write("\n" * 2)
            cmd_output = net_connect.send_command(command, read_timeout=20)
            # time.sleep(5)
            f.write(cmd_output + "\n" *2)
