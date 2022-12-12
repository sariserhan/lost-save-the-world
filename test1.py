# importing whole module
from tkinter import * 
from tkinter.ttk import *
  
# importing strftime function to
# retrieve system's time
from time import strftime
  
# creating tkinter window
root = Tk()
root.title('Swan Station Countdown Timer')


  
# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
  
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')

x = 0


# This function is used to 
# display time on the label
def time():        
    string = strftime('%M:%S')
    lbl.config(text = string)
    lbl.after(1000, time)

time()
  
mainloop()