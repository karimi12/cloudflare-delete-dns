import requests
import json


EMAIL="me@gmail.com"
ZONE_ID="111111111111"
KEY="2222222222222222"
header={
    "X-Auth-Email": EMAIL,
    "Authorization":"Bearer {}".format(KEY)
}
x = requests.get('https://api.cloudflare.com/client/v4/zones/{}/dns_records?per_page=500'.format(ZONE_ID) ,headers=header)
# print(x.json())
for t in x.json()['result']:
    print (t)
    x = requests.delete('https://api.cloudflare.com/client/v4/zones/{}/dns_records/{}'.format(ZONE_ID,t['id']),headers=header)
    print(x.json())
