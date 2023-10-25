import requests
url="https://www.virustotal.com/api/v3/ip_addresses/129.226.208.154"

headers={
    "accept":"application/json",
    "x-apikey": "9f9b32477f31723540c6e0cc9faebbf9c15418e1b61bececa61b46e8ec8643e3"

}

response=requests.get(url,headers=headers)
print(response.text)

