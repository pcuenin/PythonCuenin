import feedparser
import urllib.parse
from dateutil.parser import parse
from datetime import datetime, timedelta
import pytz

utc=pytz.UTC


rssfeeds = ("http://www.uptowngreenwood.com/Home/Components/RssFeeds/RssFeed/View?ctID=6&cateIDs=1%2c31%2c33%2c34%2c35%2c42"
            ,"https://blogs.nasa.gov/stationreport/feed/", "https://www.wyff4.com/topstories-rss")

#Feed object class constructor

class Feed:
    def __init__(self,feedname, title, pubdate, url):
        self.feedname = feedname
        self.title = title
        self.pubdate = pubdate
        self.url = url

#Test code for feed class constructor
        
"""        
r1 = Feed("This is CNN", "Thu, 27 Apr 2006", "http://rss.cnn.com/rss/cnn_tech.rss")

print(r1.title)
print(r1.pubdate)
print(r1.url)
"""

#get number of days to filter by

mindays = input("How many days should we check for no activity? ")

datereq = datetime.today() - timedelta(days=int(mindays)) #subtract number of days from current date

#iterate through tuple of RSS Feeds and look for pubDate
datereq = utc.localize(datereq) #localize the date requirement so we can compare it with the published date

i=0; #int to name each item in list
feedList =[] #list to store all feed objects created

for x in rssfeeds:
    i=i+1
    name = "r"+str(i); #make string name
    NewsFeed = feedparser.parse(x) #parse newsfeed
    entry = NewsFeed.entries[1] #get first entry from RSS feed
    dt = parse(entry.published) #parse the date from the RSS feed pubDate format to datetime
    feedList.append( Feed(name,entry.title, dt,x)) #creat object and add to feedList

if int(mindays) <2:
    print( "\nThese feeds had no activity for " + mindays + " day :")
else:
    print( "\nThese feeds had no activity for " + mindays + " days :")

for feed in feedList:
    if feed.pubdate < datereq:  #compare published date to the required date for inactivity if before that then print info
        print("")
        print("Most Recent Article: " + feed.title)
        print("Date Published: " + str(feed.pubdate))
        print("RSS Feed URL: " + feed.url+"")
        print("")

    



