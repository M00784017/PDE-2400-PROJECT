import tkinter as tk

root = tk.Tk()
root.title('PDE 2400')

Input = tk.Label(root, text = "Welcome, press on the animation you would like to see" , foreground = 'white',
                background = 'blue', width = 50, height = 2).grid(row = 1, column = 0)


def Project_Trial_2():
    import Project_Trial_2
    

PT2 = tk.Button(root, text = 'PT2', command = Project_Trial_2).grid(row = 4, column = 0)

root.mainloop()
