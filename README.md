


Easygui2
==============

Further development and maintenance for the Easygui project which was shut down in 2010
--------------

*To get the best idea of how easygui2 is different from Easygui please check example.py file.<br>
Uncomment and comment out the lines as necessary.*

**Basic use of Easygui2**

    import easygui2

	choice = easygui2.buttonbox("Would you like some coffee?","Restaurant",["Yes","No"])
	if choice == "Yes":
		...
	
**Using callback**<br>
If you ever needed to get sequential inputs from a user with Easygui, you have probably noticed this problem by yourself.
Let's say we have an robot we want to control. We want to be able to move it in all directions and to switch it on and off.
(Exit on "OFF")
You're probably thinking of something like this:

	import easygui2

	choices = ["ON", "OFF", "forward", "backward", "right", "left"] 
	input= '' 
	while input != "None": #happens when the user presses ESC  
		input = easygui2.buttonbox("controller","robot", choices)
		if input == "forward":   
			...
		elif input == "backward":
		   ...  
		...  
		...  
		elif input == "off":   
			break
			
Problems:<br>
- User can't move the GUI around the screen because after every input, the window closes and a new one appears in the original place.
- Flickering happens after every choice, till the next window opens.
- Every different window gets a new task-number or pid. This makes it harder to follow the window instances 


**Using callback with Easygui2**<br>
Just create a callback function 
	import easygui2

	def controller(user_input):
	 if user_input == "forward":
		 ...
	 elif user_input == "backward":
		 ...
	 ...
	 ...
	 elif user_input == "off":
	  return "terminate" #this terminates the callback loop
	  
	choices = ["on", "off", "forward", "backward", "right", "left"]
	easygui2.buttonbox("controller","robot", choices, callback=controller)
	
