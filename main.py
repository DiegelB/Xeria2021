


def mainLoop(userInput):
	print("<br></br>")
	print("<p>You said: "+userInput+"</p>") 
	if userInput == 'test':
		botOutput = "Hello there"
	else: botOutput = "Howdy!"
	print("<p>Xeria Says:" +botOutput+"</p>")




#for testing only. this needs to be removed when sent to
#/usr/lib/cgi-bin/Xeria since it uses htmlScript.py for
#input
while True:
	userInput = input(">>")
	mainLoop(userInput)
