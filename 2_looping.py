from importlib.resources import contents
from pprint import pprint
from sample_data import *

list_ip = [
    "114.1.201.13",
    "114.1.201.88",
    "114.1.215.16",
]

# for ip in list_device:
#     print(f"{ip['hostname']} - {ip['loopback']}")


# for ip in list_ip:
#     print(ip)

for index, content in enumerate(list_device):
    print(index, content['hostname'])

# for i in range(5):
#     print("Hello world")

# for i in range(1, 6):
#     print(i)