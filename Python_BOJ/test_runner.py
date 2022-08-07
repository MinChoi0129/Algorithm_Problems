import urllib.request
import time
a= urllib.request.urlopen('http://www.google.com').headers['Date']
print(time.strptime(a, '%a, %d %b %Y %H:%M:%S %Z'))