#!/usr/bin/python37all

import cgi
import json

data = cgi.FieldStorage()
button = data.getvalue('buttons')
angle = data.getvalue('angle')
data = {"buttons":button, "angle":angle} #Dictionary of selections

# Write selections into text file
with open('LAB5.txt', 'w') as f:  
  json.dump(data,f)

print('Content-type: text/html\n\n')
print('<html>')
print('<head>')
print('<title>LED switch</title>')
print('</head>')
print('<body>
print('<h1>LAB 5</h1>')
print('<form action="/cgi-bin/stepper_control.cgi" method="POST">')
print('Angle:<br>')
print('<input type="text" name="angle"><br>')
print('<input type="submit" name = "buttons" value="Submit">')
print('<br>')
print('<input type="submit" name= "buttons" value="Zero Angle">')

print('</form>')

print('</body>')
print('</html>')