# move the GUI-window from its initial position to see how it stays there only with the new version easygui2
# notice also the flickering happens only in the old version
# comment out and in as necessary

################################# easygui2 (with callback)

# import easygui2

# def controller(user_input):
	# print "controller:",user_input, type(user_input)
	# if user_input == "forward":
		# pass
	# elif user_input == "backward":
		# pass
	# elif user_input == "off":
		# return "terminate" #this terminates the callback loop
		
		
# choices = ["on", "off", "forward", "backward", "right", "left"]
# easygui2.buttonbox("robot cobtroller","repeatative input", choices, callback=controller)
	
	
	
################################# easygui (the old version)
import easygui 

choices = ["on", "off", "forward", "backward", "right", "left"]
input= ''
while input != "None": #None is when user press ESC
	input = easygui.buttonbox("robot cobtroller","repeatative input", choices)
	if input == "forward":
		pass
	elif input == "backward":
		pass
	elif input == "off":
		break
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		