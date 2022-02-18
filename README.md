# PDE-2400-PROJECT, YOU CAN FIND THE FINAL PROJECT PYTHON FILE INSIDE THE FOLDER CALLED PROJECT WORK ANIMATIONS AND IT IS CALLED Final_Project_PDE2400. For easier use, open the file called 'Using Tkinter' and run it.

****************
This project was done during the period from 4 January 2022 to 17 February 2022. My consistency is documented through Github, although I have changed my python file name several times so it might not show all commits on the same name. I have been able to constantly update my repository more than 3-4 times a week for the past 4 weeks.
*****************
#####Libraries used
****************
1## simulator:
The simulator has 360 built in leds in 6 rows and each row contains 60 leds.
LEDs.
2##import opc:
Calls out the simulator
3##from time import sleep:
Imports sleep from time because we dont need the whole library
4##import colorsys:
Used to integrate hsv value and saturation to some animations
5##import random:
Used to shuffle random colors or colors between a specified range, eg: random.radint(0,255)
6##import numpy:
used to roll and shift in weather animations
7##import os:
used to input an option for exit 
8##import sys
used to input an option for exit 
*******************
#####functions used
Each function of a country is named for drawing up the flag of it.
Function 1 is named Palestine, and it displays the flag of palestine
Function 2 is the flag of England and it uses an animation to draw up the flag.
Function 3 is the flag of Ireland.
Function 4 is the flag of Ukraine.
Function 5 is the flag of Germany.
Function 6 is the flag of Armenia.
Function 7 is the flag of Brazil.
There are 9 inputs in the flag animations, the first 7 are for the flags mentioned above,
input 8 is the exit if the user wishes to leave, and input 9 is the restart option where the user wishes to restart.

*********************
Function 8 is the options function. In here, the UI is implemented so that 
the user has 9 choices to pick between using numbers. If the user inputs an 
invalid character or a number, the ui reports an error and asks the user to input a valid number between 1 and 9. There are some exeptions however. For example,
if a user enters a word that corresponds to a number listed the in the except ValueError, it will return the flag of this corresponding value. For example, 1=one, 2=two etc..
*********************
Function 9 is the user function. This is the second part of the animation and it is a simple one. The code asks the user 
to input the country they are in. After that, it asks for the weather in this country using 4 choices and displays an animation based on the input. The same error handling is applied as mentioned above.
*********************
Function 10 is the More Animations function and in here there are 3 nice animations for the user to pick from. The 4th option is to exit, and the 5th is to restart. I tried my best to make the animations good and creative and different. Just like functions 8 and 9, the UI implemented is the same and accumulates to all possible encounters and inputs.



********************
UI implemented

The UI I implemented is extremely efficient as it helps with every possible answer the user may input such as a word, number or character. The UI asks the user to input their chosen number, the user can either input it as a number or as a word. In either way, the UI will know what the input is and see if it is in the exception list in try and except ValueError. If not, the UI will print("Please enter a value between x and y").
********************
Animations Explanation

Animation 1 is the flag of palestine and all the leds turn to the flag of Palestine, then the UI will print the capital of this country. The same goes for the other 6 countries.
Weather animations are all the same at the moment with one difference, which is the color. For instance, if the user choses rainy as the weather, the screen will light with blue colors, if weather==sunny, then the screen will light with yellow.
The last 4 animations are the most creative. The first animation is called the fading animation. Here, 3 colors fade consecutively after each other resulting in a nice pattern. The second one is the netherlands flag wher it splits the flag in half and each part goes in a corner(either left or right). The third one is the police animation and it flashes the colors of the siren repeatedly. The 4th one is 6 different colors scrolling making a beautiful animation.
********************
Instructions on how to start. PS:all numbers entered using a word should be enetered by lower case, eg: 1 is 'one' and 7 is 'seven'.

1-Open the file, and the opc simulator. Make sure the python file is in the same folder as the opc, or else it will tell you 'opc module not found'.
2-Run the idle.
3-Tkinter will appear asking you to press on the button of the project.(This is done for easier use for the user)
4-Idle will appear.Choose from the first list of animations either by entering the number or the word number, eg: if you want the 3rd flag, either enter three or 3. Enter 8 or eight if you wish to leave.Enter 9 or nineif you wish to restart.
5-Enjoy the animation.
6-The second input pops in the idle, asking you which country are you currently in.
7-Enter the country you are in by typing the word, if the input entered is a number, an rror will pop asking for a word not a number.
8-Then choose the weather your country is experiencing by entering the number or the word number, eg: if you want the 2nd weather animation, either enter two or 2. Enter 5 or five if you wish to leave.
9- Enjoy the animation.
10- The third input pops in the idle, asking you to choose between the last 3 animations.
11-Chose from the last list of animations either by entering the number or the word number, eg: if you want the 1st animation, either enter one or 1. Enter 4 or four if you wish to leave.Enter 5 or fiveif you wish to restart.
12- That is the end, Thank you.












My Timeline: #week end date
Week 12: (09-01-22)
-Created github account and made a new repository.
Week 13:(16-01-22)
-Started researching fadecandy and trying out some simple examples to see how it works
Week 14:(23-01-22)
-Started working on my first project trial with basic functions and animations, and received feedback from Denis regarding that.
-Made some changes to function names and removing the 'return' in each function as it was not necessary.
-Submitted several commits and changes over the week.
WEEK15:(30-01-22)
-Made some animations of flags and decided I will do Flags animation
-Made more advanced animation and tried to minimize code

Week 16:(06-02-22)
-continued with adding Flags
-Debugging code
-Added more creative animations to my code .

WEEK17:(13-02-22)
- Addded 2 final flags to the animation list.
-Improve code reusability and add more comments
Week 18:(17-02-22)
-Finalise code and submit .