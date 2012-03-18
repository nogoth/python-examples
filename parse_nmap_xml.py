import urllib
from xml.dom import minidom
import sys

#USAGE: sudo nmap -sP -PR -oX - localdomain.0/24 | ruby thisfile
#RESULTS: ip_address , mac address

dom = minidom.parse(sys.stdin)
for host in dom.getElementsByTagName('host'):
     print host.toxml()
##doc = Hpricot.XML(STDIN.readlines.join)

##uplist = doc.search(:host).select do |h| 
  #h.search("//status[@state='up']").length > 0 
 ## h.search("//status[@reason='arp-response']").length > 0 
##end

#each host has two addresses, the ip address and the mac

##uplist.each {|h| puts (h/:address).map{ |i| i[:addr]}.join(" ")}
