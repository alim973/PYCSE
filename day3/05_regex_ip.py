import re
from collections import Counter


with open("Linux_2k.log", 'r') as file:
        log_data = file.read()
        
        ip_addresses = re.findall(r'\d+\.\d+\.\d+\.\d+',log_data)
        
        
# print("Extracted IP Addresses:")
# for ip in ip_addresses:
#     print(ip)
    
#     print (ip_addresses )
    
ip_counts=Counter(ip_addresses)

# for ip,count in ip_counts.items():
#     print(f'ip address {ip} - accurred {count} times.')
    
# sorted(ip_counts.items)
    
print ((ip_counts.most_common(10)))
    