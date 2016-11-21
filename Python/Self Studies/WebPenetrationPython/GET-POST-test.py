#!/usr/bin/env
import requests

"""
Why would we want to mess with HEADER?
1) Fake user-agent (pretend to be mobile, another browser or platform)
2) Custom header
3) Change host header
4) Bruteforce or tamper any header
"""
URL = "http://httpbin.org/"
# payload = {'url': 'http://www.edge-security.com'}
# this can be changed in order to save bandwidth or just cut off
# unnecessary data noise
# r = requests.get(URL, params=payload)
# r = requests.get(URL + 'headers')
my_headers = {'user-agent': 'Iphone 7000000000000'}  # faked user-agent
p = requests.post(URL + 'post', data={'fuck': 'you'}, headers=my_headers)  # modified data on server,custom field
print p.url
print "Status code:" + str(p.status_code)
print '*****************************************'
print 'Modified server headers'
print '*****************************************'
for e in p.headers:
    print '\t' + e + ':' + p.headers[e]
print '*****************************************\n'
print p.content
