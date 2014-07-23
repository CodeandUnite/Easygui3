


Easygui2
==============

Further development and maintenance for the Easygui project which has been shut down in 2010.
--------------

*To get the best idea of how easygui2 is different from easygui is to check example.py file.
Uncomment and comment out the lines as necessary.*

**Basic use of Easygui2**

    import easygui

	choice = easygui.buttonbox("body","title",["Yes","No"])
	if choice == "Yes":
		...
	
**Using callback**
If you ever needed to get sequential inputs from a user with it, you have probably noticed this problem by yourself.
I'll explain the problem with an example. Let's say we have an external device we want to control, a robot. We want to be able to move it in all directions and to switch it on and off.
You're probably thinking of something like this:

	import easygui

	choices = ["on", "off", "forward", "backward", "right", "left"] 
	input= '' 
	while input != "None": #happens when the user presses ESC  
		input = easygui.buttonbox("controller","robot", choices)
		if input == "forward":   
			...
		elif input == "backward":
		   ...  
		...  
		...  
		elif input == "off":   
			break
