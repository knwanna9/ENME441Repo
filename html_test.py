#!/usr/bin/python37all
# Save file as /usr/lib/cgi-bin/html_test.python37all

print("""

Content-type: text/html \n\n
<html>
<body>
<form action = '/cgi-bin/html-test.py' method = 'POST'>
<input type = 'Submit' value = 'create a new page'>
</form>
</body>
</html>

""")