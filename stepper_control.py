#!/usr/bin/python37all

import cgi
import json
from urllib.request import urlopen
from urllib.parse import urlencode
import time

api = "3A8R6VUORY9JIE8N"

#Get form submission data
data1 = cgi.FieldStorage()
button = data1.getvalue("buttons")
b_press = 1 if button == "Submit" else 0
theta = data1.getvalue("angle")

#Create dictionary of form data
data1 = {
 1: theta,
 2: b_press,
 "api_key": api}

#Send data to Thingspeak
data1 = urlencode(data1)
url = "https://api.thingspeak.com/update?" + data1
print(url)
response = urlopen(url)

print('Content-type: text/html\n\n')
print('<html>')
print('<head>')
print('<title>LED switch</title>')
print('</head>')
print('<body>')
print('<h1>LAB 5</h1>')
print('<form action="/cgi-bin/stepper_control.py" method="POST">')
print('Angle:<br>')
print('<input type="text" name = "angle"><br>')
print('<input type="submit" name = "buttons" value="Submit">')
print('<br>')
print('<input type="submit" name= "buttons" value="Zero Angle"><br>')
print('</form>')
print('Current Angle<br>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1558420/widgets/376412"></iframe>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1558420/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15&api_key=MSQKXFOAG2UMD4NZ"></iframe>')
print('</body>')
print('</html>')

