import sys
ip_info= {
    "8.8.8.8":{
        "domain":"google-public-dnsa.google.com",
        "country":"us",
    },

    "1.1.1.1": {
        "domain":"cloudflare-dn.com",
        "country":"AU"
        }
    
}

print(ip_info["1.1.1.1"])

ip=sys.argv[1]
print(ip)
#ip="1.1.1.1"
print(f"Country for provided ip {ip} is >>>",ip_info[ip]["country"])