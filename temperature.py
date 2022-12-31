from selectorlib import Extractor

import requests


class Temperature:

    """
    A scrapper that uses an yml file to read the xpath of a value it needs to extract from the timeanddate.com/weather/url


    """

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

    def __init__(self,country,city):
        self.country = country.replace(" ","-")
        self.city = city.replace(" ","-")

    def build_url(self):
        """
        Builds the url string adding country and city
        """

        url = self.base_url + "/" + self.country + "/" + self.city
        return url


    def scrape(self):
        """
        Extracts a value as instructed by the yaml file and returns a dictionary
        """
        url = self.build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers=self.headers)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content
        

    def get(self):

        """
        Cleans the output of _scrape
        """

        scrapped_content = self.scrape()
        
    
        return float(scrapped_content['temp'].replace("°C","").strip())
        

if __name__ == "__main__":

    temperature = Temperature(country = 'usa', city= 'san-francisco')
    print(temperature.get())
    

