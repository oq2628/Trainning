import requests
from bs4 import BeautifulSoup
s = requests.session()
values = {'log': 'admin',
          'pwd': '123456aA'}
request = s.post('http://45.79.43.178/source_carts/wordpress/wp-login.php?loggedout=true&wp_lang=en_US', data=values).text
soup = BeautifulSoup(request, 'html.parser')
results = soup.find('span', class_='display-name')
print(results.text)