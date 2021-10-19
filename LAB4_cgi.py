#!/usr/bin/python37all

import cgi
import json
data = cgi.FieldStorage()
color = data.getvalue('led')
brightness = data.getvalue('slider1')
data = {"led":color, "slider1":brightness}
with open('LAB4.txt', 'w') as f:  
  json.dump(data,f)

print('Content-type: text/html\n\n')
print('<html>')
print('<head>')
print('<title>LED switch</title>')
print('</head>')
print('<body>')
print('<h1>LAB 4</h1>')
print('<form action="/cgi-bin/LAB4_cgi.py" method="POST">')
print('<p>Please select an LED:</p>')
print('<input type="radio" name="led" value="red"> RED LED <br>')
print('<input type="radio" name="led" value="blue"> BLUE LED <br>')
print('<input type="radio" name="led" value="green"> GREEN LED <br>')

print('<p>Choose brightness (duty cycle):</p>')
print('<input type="range" name="slider1" min ="0" max="100" value ="0"><br>')
print('<input type="submit" value="Submit">')
print('</form>')

print('</body>')
print('</html>')
print('</body>')
print('</html>')

'''
print("""
Content-type: text/html\n\n
<html>
<head>
<title>LED switch</title>
</head>
<body>
<h1>LAB 4</h1>
<form action="/cgi-bin/LAB4_cgi.py" method="POST">
<p>Please select an LED:</p>
<input type="radio" name="led" value="red"> RED LED <br>
<input type="radio" name="led" value="blue"> BLUE LED <br>
<input type="radio" name="led" value="green"> GREEN LED <br>

<p>Choose brightness (duty cycle):</p>
<input type="range" name="slider1" min ="0" max="100" value ="0"><br>
<input type="submit" value="Submit">
</form>

</body>
</html>
</body>
</html>

""")
'''
