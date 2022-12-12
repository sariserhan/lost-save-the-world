import time
import simpleaudio as sa

from tkinter import *
from tkinter.ttk import *


def push_button():
    pass


def input_thread():
    user_input = input('>:')
    return user_input

def main(minute, second, code, wave_obj):
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
            
        time.sleep(1)
        
        
        
def countdown_timer():
    string = f'{minute:02}:{second:02}'
    lbl.config(text = string)
    lbl.after(1000, countdown_timer)
        
        
if __name__ == '__main__':
    wave_obj = sa.WaveObject.from_wave_file("alarm.wav")
    minute = 5 - 1
    second = 60 - 1
    code = '4 8 15 16 23 42'
    
    # creating tkinter window
    root = Tk()
    root.title('Swan Station Countdown Timer')
    
    # Styling the label widget so that clock
    # will look more attractive
    lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
    
    
    countdown_timer()
    # print(f'{minute+1:02}:00')
    
    
    main(minute, second, code, wave_obj)
    mainloop()

