import re
from collections import Counter


with open("Linux_2k.log", 'r') as file:
        log_data = file.read()
        
        users = re.findall(r' user.\w+',log_data)
        
        
# print("Extracted IP Addresses:")
# for ip in ip_addresses:
#     print(ip)
    
#     print (ip_addresses )
    
print (users)
users_counts=Counter(users)

# for ip,count in ip_counts.items():
#     print(f'ip address {ip} - accurred {count} times.')
    
# sorted(ip_counts.items)
    
print ((users_counts.most_common(10)))
    