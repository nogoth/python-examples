import urllib
import xml.etree.ElementTree as ET
import sys

#USAGE: sudo nmap -sP -PR -oX - localdomain.0/24 | python thisfile
#RESULTS: ip_address , mac address(optional)

doc = ET.parse(sys.stdin)
uplist = [ ]
for host in doc.findall('//host'):
    uplist = uplist + [[ h.get('addr') for h in host if h.get('addr')  ]]
print uplist
