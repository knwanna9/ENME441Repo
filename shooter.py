#!/usr/bin/python37all

import cgi, json
from urllib.request import urlopen
from urllib.parse import urlencode
api = "3A8R6VUORY9JIE8N"
data = cgi.FieldStorage()

# set up new data from POST:
slider_val1 = data.getvalue('slider1')
slider_val2 = data.getvalue('slider2')
launched = 1 if data.getvalue('launch') == 'Launch!' else 0

# form new dictionary with user data:
fileData = {
1:slider_val1,
2:slider_val2,
3:launched,
'api_key': api}

# write all data to the file:
data = urlencode(fileData)
url = "https://api.thingspeak.com/update?" + data
print(url)
response = urlopen(url)
# generate new web page:
print("Content-type: text/html\n\n")
print('<html>')
print('<body>')
print('<form action="/cgi-bin/shooter.py" method="POST">')
print('<input type="range" name="slider1" min ="3" max="12" value ="%s"><br>' % slider_val1)
print('<input type="range" name="slider2" min ="3" max="12" value ="%s"><br>' % slider_val2)
print('<input type="submit" name="angle" value="Set angle">')
print('<input type="submit" name="launch" value="Launch!">')
print('</form>')
print('</body>')
print('</html>')
