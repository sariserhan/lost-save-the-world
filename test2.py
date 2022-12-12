import time
import simpleaudio as sa

from tkinter import *
from tkinter import messagebox


# creating Tk window
root = Tk()

# setting geometry of tk window
root.geometry("300x250")

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Time Counter")

# Declaration of variables
minute=StringVar()
second=StringVar()

# setting the default value as 0
minute.set("108")
second.set("00")

# Use of Entry class to take input from the user
minuteEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=minute)
minuteEntry.place(x=130,y=20)

secondEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=second)
secondEntry.place(x=180,y=20)



def input_thread():
    user_input = input('>:')
    return user_input


def submit():
    wave_obj = sa.WaveObject.from_wave_file("alarm.wav")
    minute = 5 - 1
    second = 60 - 1
    code = '4 8 15 16 23 42'
    while True:
        # 4 minute check
        if minute == 4 and second == 0:        
            play_obj = wave_obj.play()
            code_by_user = input_thread()
            if code_by_user == code:
                minute = 108
                second = 60
		
        if minute <= 3:
            pass
            # countdown_timer()
            # print(f"{minute:02}:{second:02}")
            
        # 0 time check
        if minute == 0 and second == 0:
            break
        
        # minute check
        if second == 0:                
            minute -= 1
            second = 59
            # countdown_timer()
            # print(f'{minute:02}:{second:02}')

        second -= 1

		# updating the GUI window after decrementing the
		# temp value every time
        root.update()
        time.sleep(1)

		# when temp value = 0; then a messagebox pop's up
		# with a message:"Time's up"
		# if (temp == 0):
		# 	messagebox.showinfo("Time Countdown", "Time's up ")

# button widget
btn = Button(root, text='Set Time Countdown', bd='5',
			command= submit)
btn.place(x = 70,y = 120)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()
