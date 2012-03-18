from __future__ import with_statement
import re
import feedparser

rss = feedparser.parse('http://twitter.com/statuses/user_timeline/15827231.rss') 
print rss["channel"]["title"]
for i in rss["items"]:
    (user,say) = re.split(': ', i.title)
    print say + " -%s" % user

