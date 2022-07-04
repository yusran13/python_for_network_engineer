#String
hostname = "CRB-KDGD-EN1-C506Z CRB-KDGD-EN2-C506Z CRB-KDGD-EN3-C506Z CRB-KDGD-EN4-C506Z CRB-KDGD-EN5-C506Z"
ip_address = "192.168.1.100/24"

split_ip = ip_address.split("/")

print(split_ip)

split_hostname = hostname.split(" ")
print(split_hostname)

#Split
#Length
#Replace
#Contains
#Substring
#Upper and Lower

#Integer
ospf_area = 22

a = 10
b = 5

#Math Operation

#Boolean
sync_status = True


print("-------------------LIST--------------------------")
#Array / List
device_list = [
    "114.1.201.13", "114.1.201.88", "114.1.215.16"
]
print(device_list)
device_list.append("10.10.10.1")
print(device_list)

del device_list[0]

print(device_list)

print(len(device_list))
# print(device_list[-1])

#Accessing specific index
#Append a list
#Length


#Dictionary
router = {
    "ip_address": "114.1.200.33",
    "hostname": "CRB-KDGD-EN1-C506Z",
    "role": "EN",
    "hotnews": True,
    "ospf_area": 22
}

print(router['ip_address'])
print(router['hostname'])
print(router['hotnews'])

list_of_routers = [
    {
        "ip_address": "114.1.200.33",
        "hostname": "CRB-KDGD-EN1-C506Z",
        "role": "EN",
        "hotnews": True,
        "ospf_area": 22
    },   
    {
        "ip_address": "114.1.200.33",
        "hostname": "CRB-KDGD-EN2-C506Z",
        "role": "EN",
        "hotnews": True,
        "ospf_area": 22
    },   
    {
        "ip_address": "114.1.200.33",
        "hostname": "CRB-KDGD-EN3-C506Z",
        "role": "EN",
        "hotnews": True,
        "ospf_area": 22
    },   

]

print("++++++++++++++++++++++++++++++++")
for device in list_of_routers:
    print(device['hostname'], device['ip_address'])

#list of keys




