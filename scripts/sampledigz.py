#! /usr/bin/env python
import requests
import collections
import json
import datetime
import time
import praw


now = datetime.datetime.now()
username = ""


class SampleDigz():

	def isYTLink(self, url):
		return "youtube" in url or "youtu.be" in url

	def getID(self, url):
		if len(url) == 101:
			return url[72:83]
		elif len(url) >= 57:
			return url[32:43]
		elif len(url) <= 35 and len(url) >= 33:
			return url[17:28]
		else:
			return url[-11:]

		return url

	def getData(self, genre):
		reddit = praw.Reddit(client_id='-DQdBaK1erEVWw',
	                   	client_secret="1f5TjkaWfIaOtkNyIzGXaov5BZ0", password='',
	                    user_agent='textscript by /u/' + username, username=username)
		
		reddit.read_only = True

		subreddit = reddit.subreddit('ListenToThis')

		global linkIDs
		linkIDs = []
		titles = []
		tempLinks = []

		for link in subreddit.search(genre, sort='top', time_filter='week'):
			titles.append(link.title)
			tempLinks.append(link.url)
			if self.isYTLink(link.url):
				linkIDs.append(self.getID(link.url))


		# For Book keeping
		date = "%d" % now.month + "-" + "%d" % now.day + "-" + "%d" % now.year
		filename = "../data/" + genre + "/" + date + ".txt"
		file = open(filename, "w+")

			
		file.write(date + '\n')

		cnt = 1
		while len(titles) > 0 and len(tempLinks) > 0:
			output = (str(cnt) + ".) " + "title: " + titles.pop() + '\n' + "\t url: " + tempLinks.pop() + '\n' + '\n').encode('utf-8')
			cnt+=1
			file.write(output)

		return linkIDs





