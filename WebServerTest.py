import urllib2
import socket
import sys


#check for successful http request
def check_url(url, timeout=5):

    try:
        return urllib2.urlopen(url,timeout=timeout).getcode() == 200
    except urllib2.URLError as e:
        return False
    except socket.timeout as e:
        print False

#list of sites to check 
def CheckSites():

	sites = ["https://google.com"]

	for sites in sites:
		print (sites), 'is available: ', check_url(sites)

def Main():

	CheckSites()

Main()
