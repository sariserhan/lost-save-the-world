from tkinter import *
from tkinter import ttk
import simpleaudio as sa

# NOTE:
# alarm 4 dakkika kalinca calsin
# start button olmasin
# 108:00
# 107:00
# ...
# 5:00
# 4:00 - alarms start
# 3:59
# 3:58
# ----------------


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)

        self.pack()
        self.createWidgets()
        self._alarm_id = None
        self._paused = False
        self._starttime = 10 * 60 + 8
        self._code = "4 8 15 16 23 42"
        self._wave_obj = sa.WaveObject.from_wave_file("alarm.wav")

    def createWidgets(self):
        self.someFrame = Frame(self)
        self.startButton = Button(
            self.someFrame, text="Start", command=self.startTime)
        self.startButton.pack(side=LEFT)
        self.someFrame.pack(side=TOP)

        self.labelvariable = StringVar()
        self.labelvariable.set("10:08")
        self.thelabel = Label(
            self, textvariable=self.labelvariable, font=('Helvetica', 50))
        self.thelabel.pack(side=TOP)

        self.entry = Entry(self, width=40)
        self.entry.pack()
        ttk.Button(self, text="Okay", width=20,
                   command=self.printInput).pack(pady=20)

    def resetTime(self):
        if self._alarm_id is not None:
            self.master.after_cancel(self._alarm_id)
            self._alarm_id = None
            self._paused = False
            self.countdown(6080)

    def startTime(self):
        """ Resume """
        self._paused = False
        if self._alarm_id is None:
            self.countdown(self._starttime)

    def stopTime(self):
        """ Pause """
        if self._alarm_id is not None:
            self._paused = True

    def countdown(self, timeInSeconds, start=True):
        if start:
            self._starttime = timeInSeconds
        if self._paused:
            self._alarm_id = self.master.after(
                1000, self.countdown, timeInSeconds, False)
        else:
            mins, secs = divmod(timeInSeconds, 60)
            timeformat = "{0:02d}:{1:02d}".format(mins, secs)
            app.labelvariable.set(timeformat)
            self._alarm_id = self.master.after(
                1000, self.countdown, timeInSeconds - 1, False)

        if mins < 10 and secs % 5 == 0:
            print(mins, secs)
            play_obj = self._wave_obj.play()

        elif mins < 8 and secs % 2 == 0:
            play_obj = self._wave_obj.play()

    def printInput(self):

        z = self.entry.get()
        if self._code == z:
            self.master.after_cancel(self._alarm_id)
            self._alarm_id = None
            self._paused = False
            self.countdown(self._starttime)

    def retrieve_input(self):
        global z
        z = self.entry.get()
        print('Input value => %s' % z)


if __name__ == '__main__':
    root = Tk()
    root.title("Timer")
    app = Application(root)
    root.mainloop()
