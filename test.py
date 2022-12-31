import requests
from selectorlib import Extractor






headers = { 

        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,image/web,image/apng,application',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}

base_url = "https://www.timeanddate.com/weather"
yml_path = "temperature.yaml"
url = 'https://www.timeanddate.com/weather/usa/san-francisco'



extractor = Extractor.from_yaml_file(yml_path)
r = requests.get(url, headers=headers)
full_content = r.text
raw_content = extractor.extract(full_content)
scrapped_content =  raw_content
result = scrapped_content['temp'].replace("°C","").strip()
print(result)