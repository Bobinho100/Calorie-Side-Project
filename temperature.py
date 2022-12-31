class Temperature:

    """
    A scrapper that uses an yml file to read the xpath of a value it needs to extract from the timeanddate.com/weather/url


    """

    headers = {}
    base_url = "https://www.timeanddate.com/weather"
    yml_path = "temperature.yaml"

    def __init__(self,country,city):
        self.country = country.replace(" ","-")
        self.city = city.replace(" ","-")

    def _build_url(self):
        """
        Builds the url string adding country and city
        """

        url = self._base_url + self.country + "/" + self.city
        return url


    def scrape(self):
        """
        Extracts a value as instructed by the yaml file and returns a dictionary
        """

        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers = self.headers)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):

        """
        Cleans the output of _scrape
        """

        scrapped_content = self._scrape()
        return float(scrapped_content['temp'].replace("C","").strip())
        


    if __name__ == "__main__":
        
