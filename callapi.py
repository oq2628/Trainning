import requests

url = 'https://sitetest06.myshopify.com'
customer_url = url + "/admin/api/2020-10/customers.json"
response = \
    requests.get(url=customer_url, headers=
    {'X-Shopify-Access-Token': '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'})
header = [k for k in response.json()["customers"][1] if k != 'default_address' and k != 'addresses']
data = ','.join(header)
for customer in response.json()["customers"]:
    row = []
    for i in header:
        row.append(str(customer[i]))
    data += "\n" + ",".join(row)
with open(file="customer.csv", mode='w') as csv_file:
    csv_file.write(data)
