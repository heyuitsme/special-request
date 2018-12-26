import requests
import json
import os
import random
import string

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'insert request url here'

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    #depending on number of fields, may require more
    username = name.lower() + name_extra + '@yahoo.ca'
    password = ''.join(random.choice(chars) for i in range(10))

    requests.post(url, allow_redirects=False, data={
        #this can be a variety of different keys depending on fields on scam page
        'insertkeyhere': username
        'insertkeyhere': password
    })

    print 'sending username %s and password %s' % (username, password)

