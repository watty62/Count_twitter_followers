#import locale
import re
from lxml import html
import requests

twitterAccounts = ['DanceAberdeen','Aberdeencc','mjs_abc','AbdnArtMuseums','AberdeenCSP','LordProvostAbdn','Acc_Jobs','NESPF','AbdnArchives','AberdeenILV','AberdeenLDP','TSAPAberdeen','Seventeen_AB','ACSEF_NESTRANS','AbLearnFest','abernet','SilverCityLibs','OCEACC']

#locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def getFollower(accURL):
	page = requests.get(accURL)
	tree = html.fromstring(page.text)

	followers = tree.xpath('//a[@data-nav="followers"]/@title')[0]
	followers = re.match(r'^([0-9,]+)\sFollowers$', followers).group(1)
	# followers = locale.atoi(followers)

	return followers

for twAccount in twitterAccounts:
	twURL = 'http://twitter.com/' + twAccount
	print twAccount + ": " +  str(getFollower(twURL))
	



#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
