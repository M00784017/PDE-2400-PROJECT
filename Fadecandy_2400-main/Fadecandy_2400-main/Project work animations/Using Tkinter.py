import tkinter as tk #tk for easier use

root = tk.Tk()
root.title('PDE 2400') #title for the block

Input = tk.Label(root, text = "Welcome, press on the animation you would like to see" , foreground = 'white',
                background = 'blue', width = 50, height = 2).grid(row = 1, column = 0)#asks the user to press on the animation, the width and height were to match the length of the text


def Final_Project_PDE2400():
    import Final_Project_PDE2400 #import this file when button is pressed
    

Final = tk.Button(root, text = 'Final Project', command = Final_Project_PDE2400).grid(row = 4, column = 0)

root.mainloop()

