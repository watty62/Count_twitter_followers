#!/usr/bin/python
import re
from lxml import html
import requests
import scraperwiki
import datetime


'''
# Begin Section A
# this section sets up the DB, reads in existing followers, writes values to the database
# it needs to be uncommented to set up then commented out again before having the live scraper run


#import sqlite3
import scraperwiki

header =['Date','ACC_Business','DanceAberdeen','Aberdeencc','mjs_abc','EventsAberdeen','AbdnArtMuseums','AberdeenCSP','LordProvostAbdn','Acc_Jobs','NESPF','AbdnArchives','AberdeenILV','AberdeenLDP','TSAPAberdeen','Seventeen_AB','ACSEF_NESTRANS','AbLearnFest','abernet','SilverCityLibs','OCEACC']
list_of_lists = [[20090701,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[20090801,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [20090901,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20091001,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20091101,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20091201,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20100101,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20100201,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20100301,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20100401,0,0,52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20100501,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20100601,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[20100701,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20100801,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20100901,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20101001,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20101101,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20101201,0,0,554,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[20110101,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20110201,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20110301,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20110401,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20110501,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[20110601,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20110701,0,0,1258,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20110801,0,0,1377,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20110901,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[20111001,0,0,1635,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20111101,0,0,1855,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20111201,0,0,2197,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],[20120101,0,0,2325,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20120201,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20120301,0,0,2739,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20120401,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], [20120501,0,0,3073,0,0,0,0,0,0,0,26,1,0,0,0,0,0,0,0,0], [20120601,0,0,3391,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20120701,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [20120801,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[20120901,648,346,4025,0,0,1661,215,369,81,0,142,42,0,0,0,0,0,0,0,0],[20121001,660,368,4151,0,0,1856,216,380,89,0,148,53,1,0,0,0,0,0,0,0],
[20121101,688,395,4436,0,0,2923,234,442,98,0,219,65,22,0,0,0,0,0,0,0], [20121201,711,419,4925,0,0,3808,243,508,108,0,239,132,45,0,0,0,0,0,0,0],[20130101,717,434,5262,180,306,4732,248,544,116,0,257,167,66,1,0,0,0,0,0,0],[20130201,721,456,5761,184,0,6023,258,606,125,28,292,203,88,7,1,0,0,0,0,0],[20130301,0,476,5969,196,0,7097,264,655,129,28,307,215,116,18,215,0,0,0,0,0],[20130401,0,499,6267,204,0,8312,291,698,142,29,326,246,137,39,508,0,0,0,0,0],[20130501,0,510,6466,215,0,9478,326,728,155,31,365,265,158,46,715,0,0,0,0,0],[20130601,0,532,6745,226,0,10824,339,797,157,31,402,271,173,49,870,0,0,0,0,0],[20130701,0,537,6978,231,0,11481,351,840,170,34,432,282,177,55,981,0,0,0,0,0],[20130801,0,552,7212,241,0,12083,361,877,173,36,475,301,193,56,1015,1,0,0,0,0],[20130901,0,568,7424,251,0,12752,384,908,182,35,554,324,204,64,1037,48,0,0,0,0],[20131001,0,576,7653,263,0,13382,397,949,191,36,596,401,217,66,1074,68,0,0,0,0],[20131101,0,586,7894,276,0,14225,410,1003,194,38,630,482,236,71,1109,93,0,0,0,0],[20131201,0,590,8118,283,0,14572,432,1057,205,37,652,597,248,74,1136,105,1,0,0,0],[20140101,0,599,8344,288,0,15000,447,1112,210,38,676,664,261,74,1159,117,10,110,0,0],[20140201,0,620,8634,296,0,15700,456,1162,213,40,698,729,283,74,1192,133,53,0,0,0],[20140301,0,630,8996,310,0,16548,459,1197,220,40,716,892,304,74,1201,144,68,114,0,0], [20140401,0,641,9261,325,0,17123,463,1282,225,42,736,1205,325,72,1290,157,83,118,0,0],[20140501,0,665,9527,334,0,17975,462,1328,225,43,768,1662,342,78,1328,177,85,122,0,0],[20140601,0,675,9824,348,0,18860,465,1399,231,46,792,2125,348,80,1402,185,86,121,1,0],[20140701,0,689,10157,354,0,19429,468,1446,238,54,829,2515,354,80,1455,195,86,127,140,1],[20140801,0,696,10364,357,0,20051,470,1477,239,56,848,2534,357,84,1508,201,85,125,160,9]]

#Open the database
scraperwiki.sqlite.execute("drop table if exists data")
scraperwiki.sqlite.execute("create table data (DATE string, TWITTERAC string, FCOUNT int)")


for inner_l in list_of_lists:
    lp_count = 0
    while lp_count<21:
        if lp_count == 0:
            twdate = inner_l[lp_count]
            #print twdate

        else:
            tw_followers = inner_l[lp_count]
            #if there are some followers write out the date, ac, and follwers to the DB
            if tw_followers <> 0:
                twitter_ac = header[lp_count]
                #print twitter_ac
                scraperwiki.sqlite.execute("insert into data values (?,?,?)", (twdate, twitter_ac,tw_followers)) 
                scraperwiki.sqlite.commit()
  
        
        lp_count =lp_count +1
        #print "end of list"

print "Ended"

# End Section A
'''
# Begin Section B
# Section B is the main scraper. It checks if the date is teh 1st of the month. If so, it scrapes the number of twitter followers for active accounts in the 
# TiwtterAccounts list, and writes these with the current date in YYYMMDD format to the 'data' table in the database

twitterAccounts = ['DanceAberdeen','Aberdeencc','mjs_abc','AbdnArtMuseums','AberdeenCSP','LordProvostAbdn','Acc_Jobs','NESPF','AbdnArchives','AberdeenILV','AberdeenLDP','TSAPAberdeen','Seventeen_AB','ACSEF_NESTRANS','AbLearnFest','abernet','SilverCityLibs','OCEACC']

#locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def getFollower(accURL):
	page = requests.get(accURL)
	tree = html.fromstring(page.text)
	#scrape the number of followers from the bit of the page that hides that number (whcih actually appears in a mouseover!

	followers = tree.xpath('//a[@data-nav="followers"]/@title')[0]
	followers = re.match(r'^([0-9,]+)\sFollowers$', followers).group(1)
	# followers = locale.atoi(followers)
	return followers

def get_date_str():
	i = datetime.datetime.now()
	str_day = str(i.day)
	str_month = str(i.month)
	str_year = str(i.year)

	if len(str_day) < 2:
		str_day = "0"+str_day

	if len(str_month) < 2:
		str_month = "0"+str_month

	str_date = str_year + str_month + str_day

	return str_date

n = datetime.datetime.now()
 
#check that it is the 1st of the month
if n.day == 1:
	#get a full date string formatted YYYYMMDD
	twdate = get_date_str()
	#Loop through all the active twitter accounts we want to monitor, forming full URLS and pass them to the getFollowers function
	for twitter_ac in twitterAccounts:
	    twURL = 'http://twitter.com/' + twAccount
	    #test print those for now - then change to SQL writes
	    print twdate + ": " + twitter_ac + ": " +  str(getFollower(twURL))
	    #scraperwiki.sqlite.execute("insert into data values (?,?,?)", (twitter_ac,twdate,tw_followers)) 
        #scraperwiki.sqlite.commit()
else:
	print "Not today"	
