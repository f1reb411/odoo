import requests
import json
import csv

with open('odoo.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Country', 'Leads', 'Partners', 'Customers', 'Size <5', 'Size 5-20', 'Size 20-50', 'Size 50-250', 'Size 250+'])


for country in range(1, 250):
  url = f"https://www.odoo.com/my/partner/stat_by_country/{country}"

  payload = json.dumps({
    "jsonrpc": "2.0",
    "method": "call",
    "params": {},
    "id": 554518349
  })
  headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4870.151 Safari/537.36',
    'sec-ch-ua-platform': '"Linux"',
    'Origin': 'https://www.odoo.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.odoo.com/my/partner',
    'Accept-Language': 'en-GB,en;q=0.9,es-ES;q=0.8,es;q=0.7,ru-RU;q=0.6,ru;q=0.5,mn-MN;q=0.4,mn;q=0.3,ms-MY;q=0.2,ms;q=0.1,en-US;q=0.1',
    'Cookie': 'session_id=7e79f2f94c95053de497de176f795d8ff5dd263f; _ga=GA1.2.1736774305.1650275970; frontend_lang=en_US; tz=Europe/Moscow; _gid=GA1.2.727904290.1650719936; _gat=1; im_livechat_history=["/my/partner"]; session_id=7e79f2f94c95053de497de176f795d8ff5dd263f'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  data = json.loads(response.text)
  result = data['result']
  country = data['result']['country_name']
  leads = data['result']['country_leads']
  partners = data['result']['country_partners']
  customers = data['result']['country_customers']
  size = json.loads(data['result']['company_size'])
  size_less_5 = size[0]['value']
  size_less_5_20 = size[1]['value']
  size_less_20_50 = size[2]['value']
  size_less_50_250 = size[3]['value']
  size_less_more_250 = size[4]['value']

  with open('odoo.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow([country, leads, partners, customers, size_less_5, size_less_5_20, size_less_20_50, size_less_50_250, size_less_more_250])


