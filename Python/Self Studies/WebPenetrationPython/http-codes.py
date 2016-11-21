# Will be useful for any interview
# 1XX - Informational
# 2XX - Success
# 3XX - Redirection
# 4XX - Client-side error
# 5XX - Server-side error
import requests

url_invalid = 'http://httpbin.org/failhtml'
url_valid = 'http://httpbin.org/html'
url_redirect = 'http://httpbin.org/redirect-to'
payload = {'url': "http://bing.com"}
req = requests.get(url_valid)
print "For this url {} ".format(req.url) + "Response code is : " + str(req.status_code) + "\n"
req = requests.get(url_invalid)
print "For this url {}".format(req.url) + "Response code is: " + str(req.status_code) + "\n"
req = requests.get(url_redirect, params=payload)
print "For this url {}".format(req.url) + "Response code is: " + str(req.status_code) + "\n"
print "We have used redirection to bing.com instead of HackYourBank.com, that can be reflected in the request"
for element in req.history:
    print ("History code: " + str(element.status_code)+ ' : ' + element.url)
