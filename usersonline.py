from lxml import html
import requests
import time
import csv


subreddit = 'funny'
url = 'http://www.reddit.com/r/' + subreddit

def getNumUsers(subreddit):
	page = requests.get(url)
	html = page.text

	beforestr = '<p class="users-online " title="logged-in users viewing this subreddit in the past 15 minutes"><span class=\'number\'>'
	before = html.index('<p class="users-online " title="logged-in users viewing this subreddit in the past 15 minutes"><span class=\'number\'>')
	after = html.index('<', before + len(beforestr))
	numusers = html[before + len(beforestr): after]
	return numusers

with open('numusers.csv', 'wb') as csvfile:
	
	labels = (["Subreddit Name", "Users Online"])
	
	writer = csv.writer(csvfile)
	writer.writerow(labels)

	for num in range(0, 5):
		if(num > 0):
			#seconds
			time.sleep(5)

		numusers = getNumUsers(subreddit)
		info = (subreddit, numusers)
		writer.writerow(info)
		print numusers


