from curl_cffi import requests
from lxml.html import fromstring
import json

class Crowling:
    def __init__(self,url) -> None:
        self.url = url
    
    def get_price(self):
        response = fromstring(self.__get_request())
        json_data = response.xpath('//script[contains(@type,"application/ld+json")][3]/text()')
        json_data = json.loads(json_data[0])
        sale_price = json_data.get('offers').get('price')
        name =  json_data.get('name')
        orginal_price = json_data['hasVariant'][0]['offers']['highPrice']
        data = {
            'name':name, 'orginal_price':orginal_price, 'sale_price':sale_price
        }
        return data

    def __get_request(self):
        r = requests.get(self.url, impersonate="chrome110")
        return r.text



        

a = Crowling('https://www.ajio.com/random-colourblock-plastic-wall-clock/p/467194982_multi')

print(a.get_price())