import socket
import urllib2
from BeautifulSoup import BeautifulSoup

timeout=10
socket.setdefaulttimeout(timeout)

# this call to urllib2.urlopen now uses the default timeout
# we have set in the socket module
req = urllib2.Request('http://www.google.com/')
response = urllib2.urlopen(req)

soup = BeautifulSoup(response)
print soup.prettify()