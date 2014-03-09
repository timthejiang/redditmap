from geopy import geocoders
from lxml import html
import requests

DEV_KEY = 'AuUEH5_gfZnuBaPCRAtWt49COZa3yIuzvjNjqH5JDa2WqGIPkBmIi3ZX6IfTzwhX'
bing = geocoders.Bing(DEV_KEY)

citiesPage = requests.get('http://www.insidervlv.com/citylargestUSA.html')
citiesHTML = html.fromstring(citiesPage.text)
cities = citiesHTML.xpath('//tr/td[@width="143"]/font/text()')
states = citiesHTML.xpath('//tr/td[@width="129"]/font/text()')

address = 'Seattle, Washington'


for cityNum in range(0, 3):
	for place, (lat, lng) in bing.geocode(cities[cityNum] + ", " + states[cityNum], exactly_one=False):
		print "%s: %.9f, %.9f \n" % (cities[cityNum] + ", " + states[cityNum], lat, lng)
		#print cities[cityNum] + ", " + states[cityNum]