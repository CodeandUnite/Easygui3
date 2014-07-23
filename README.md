
Easygui2<br>
Further development and maintenance for the Easygui project which was shut down in 2010
--------------

*To get the best idea of how easygui2 is different from Easygui please check example.py file.<br>
Uncomment and comment out the lines as necessary.
-There are some minor bugs fixed as well in Easygui2*

**Basic use of Easygui2**

    import easygui2

	choice = easygui2.buttonbox("Would you like some coffee?","Restaurant",["Yes","No"])
	if choice == "Yes":
		...
	
**Getting sequential inputs**<br>
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
		elif input == "OFF":   
			break
			
Problems:<br>
- User can't move the GUI around the screen because after every input, the window closes and a new one appears in the original place.
- Flickering happens after every choice, till the next window opens.
- Every different window gets a new task-number or pid. This makes it harder to follow the window instances 


**Using callback with Easygui2 - a much better solution**<br>
Just create a callback function which handles the input and returns "terminate" when you want to break input loop
Give this function as an optional argument when invoking:
	import easygui2

	def controller(user_input):
	 if user_input == "forward":
		 ...
	 elif user_input == "backward":
		 ...
	 ...
	 ...
	 elif user_input == "OFF":
	  return "terminate" #this terminates the callback loop
	  
	choices = ["ON", "OFF", "forward", "backward", "right", "left"]
	easygui2.buttonbox("controller","robot", choices, callback=controller)
	
	
**Not all Easygui2 functions support callback option**<br>
For some of the functions, it doesn't make sense to support it.<br>
The full list of supported functions are:<br>
boolbox   <br>
buttonbox  <br>
ccbox   <br>
choicebox  <br>
enterbox  <br>
indexbox  <br>
integerbox  <br>
multchoicebox <br>
ynbox   <br>
multenterbox<br> 

