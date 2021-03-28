import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.honda.com.br/')
except:
    print('Error in Access')
else:
    print('Success')
