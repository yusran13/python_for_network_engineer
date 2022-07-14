from pprint import pprint

#CARA 1
with open('config_acl_nso.txt') as f:
    nso_acl_config = f.read().splitlines()

pprint(nso_acl_config)


#CARA 2
# config_acl_nso = open('config_acl_nso.txt', 'r+')
# # success_list = [line.strip() for line in success_list_obj.readlines()]
# for line in config_acl_nso.readlines():
#     print(line)
#     # print(line.strip())

# config_acl_nso.close()