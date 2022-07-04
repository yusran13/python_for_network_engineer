from importlib.resources import contents
from sample_data import list_device
from pprint import pprint

list_ip = [
    "114.1.201.13",
    "114.1.201.88",
    "114.1.215.16",
]

for d in list_device:
    pprint(d)
# for ip in list_ip:
#     print(ip)

# for index, content in enumerate(list_ip):
#     print(index, content)

# for i in range(5):
#     print(i)

# for i in range(1, 6):
#     print(i)