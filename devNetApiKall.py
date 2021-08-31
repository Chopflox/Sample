import requests
import json


url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Auth-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI2MTIzZGEzMTdiM2FhOTA2ZWQwYjJiMzIiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI2NzUxNjEyMDBjYzRhYzk2MyJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTYzMDQwNzc4MywiaWF0IjoxNjMwNDA0MTgzLCJqdGkiOiI4MzQzYTY4OC00YzhhLTQ0NjItYTA5OC04NjFmYzkyN2Y3N2YiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.CIRwVHlSXUHvnFZq-BVp7DnEpxbLUYHWIXSRErs5ORwVGsJrDKUd2ptQJJqqLxNBZeZiAjiGacLCO6NuqWqUf1zttLFEstUs9TlOoCGs9AsebqXC2WaX5dhMTWm_Glq3X73r1r3NfZsdT1oRCUoXpqzU3FcTxdfyK0A9QQI2QIY2Ata5VVwyc4GRUREtsfG_OJ3i7opMccOaA4wlMY9MFx0gHYDN0CMIG7ZPvRSrwa7E4H4SrrTbJwuC13updFB4KXpU9jCsLHBEZJ85tnx7d6FRkX8X8gffZTsg5iZaFYKhHOm76MoPZvGM6mM1e2pPgXXwH7a_tY8smF1fPJEkVA"
}

response = requests.request('GET', url, headers=headers, data = payload)


print(response.json())