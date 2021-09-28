#!/usr/bin/python3
import cgi
from main import mainLoop

print("Content-type: text/html\n\n")
print("<html><body>")

print("<form method='post' action='htmlScript.py'>")
print("<p>User Input: <input type='text' name='userInput'/></p>")
print("<input type='submit' name='submit' value='Submit'/>")
print("</form>")

form = cgi.FieldStorage()
if form.getvalue("userInput"):
	userInput = form.getvalue("userInput")
	mainLoop(userInput)


print("</body></html>")
