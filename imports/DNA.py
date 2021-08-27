import requests

response = requests.get("https://sandboxdnac2.cisco.com/", auth=('devnetuser', 'Cisco123!'))



responseAuth = requests.post("https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token", auth=('devnetuser', 'Cisco123!'), )



apiToken = 'fd0c3aba-c4f7-4629-a296-3544e109f73a'

print(response)
print(responseAuth)
