from dnacentersdk import DNACenterAPI
import urllib3


api = DNACenterAPI(username='devnetuser', password='Cisco123!', base_url="https://sandboxdnac.cisco.com:443", version='2.2.2.3')

urllib3.disable_warnings()


clients = api.clients.get_overall_client_health()

print(clients)