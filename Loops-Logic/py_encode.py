#!/usr/bin/env python

import base64
import urllib





# Base64 Encode/Decode
######################


encoded = base64.b64encode('Top secret message')
print encoded

data = base64.b64decode(encoded)
print data




# URL Encode/Decode
#####################

url_encoded =urllib.quote("?id=' or 1=1 --")
print url_encoded

url_data = urllib.unquote(url_encoded)
print url_data



# this is basically taking a well known SQL injection attack and URL encoding it to see if we can sneak it by the filters
