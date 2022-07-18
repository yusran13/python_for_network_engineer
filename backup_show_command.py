import pprint, time
from netmiko import ConnectHandler
from device_driver import get_device_conn
from list_target_ip import *


with open('show_command_list.txt') as f:
    show_command_list = f.read().splitlines()

for ip in list_ip:
    print(f"Processing IP Address {ip}")
    device_conn = get_device_conn(ip)
    device_conn['session_log'] = f'backup_show_command/tets_backup_show_command_{ip}.txt'
    net_connect = ConnectHandler(**device_conn)
    print("Connected")
    # filename = f"backup_show_command/backup_command_{ip}.txt"
    # with open(filename, "w") as file_obj:
    
    for command in show_command_list:
        # print(f"Command yg sedang diinput = {command}")
        # file_obj.write("=" * 20)
        # file_obj.write(command)
        # file_obj.write("=" * (80 - len(command)))
        # file_obj.write("\n" * 2)
        cmd_output = net_connect.send_command(command, read_timeout=20)
            # time.sleep(5)
            # file_obj.write(cmd_output + "\n" *2)
