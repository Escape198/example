import requests
from requests.exceptions import RequestException
from requests_socks import Socks5ProxyManager

proxy = "socks5://111.12.13.14:9283"
proxy_manager = Socks5ProxyManager(proxy)

url = "https://domain.com"

try:
    response = proxy_manager.get(url)
    response.raise_for_status()
    print(response.text)
except RequestException as e:
    print(f"Request failed: {e}")
