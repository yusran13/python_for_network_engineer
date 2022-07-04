from pprint import pprint
# hostname  = "BDG-SWNT-EN1-C506Z"

# if "BDG-" in hostname:
#     print(f"{hostname} ada di kota bandung")
# else:
#     print(f"{hostname} bukan di kota Bandung")

router = {
        "reachability": "REACHABLE",
        "admin_status": "Managed",
        "hostname": "BDG-SWNT-EN1-C506Z",
        "loopback": "114.1.188.41",
        "Creation Timestamp": "June 20, 2022 4:47:41 PM UTC",
        "DNS Name": "114.1.188.41",
        "device_type": "Cisco NCS 540X-6Z18G-SYS-D Router",
        "Last Inventory Collection Status": "Completed",
        "Last Successful Collection Time": "June 20, 2022 8:14:03 PM UTC",
        "software_type": "IOS XR",
        "software_version": "7.5.2",
        "location": "03SRN666 SOMAWINATA_SRN_PL BANDUNG WJRO",
        "serial_number": "FOC2545N7UF"
    }

if 'BDG-' in router['hostname']:
    city = 'BANDUNG'
    router['city'] =city

elif 'PWT-' in router['hostname']:
    city = 'PURWEKERTO'
    router['city'] =city

elif 'TGL-' in router['hostname']:
    city = 'TEGAL'
    router['city'] =city

# if:
#     city = 'OTHERS'
#     router['city'] =city

pprint(router)




