from tkinter import Tk, Label, StringVar, IntVar, Button

root = Tk()

text = StringVar()
text.set('Emotion')
status = IntVar()

class EmotionDetector:
    def __init__(self, master):
        self.master = master
        master.title("Emotion Detector")

        #self.label = Label(master, text="Emotions go here")
        #self.label.pack()

        self.expand_button = Button(master, text="Expand", command=self.change, anchor="nw", justify="right", padx=2)
        self.expand_button.pack()

        self.close_button = Button(master, text="Dismiss", command=master.quit)
        self.close_button.pack()

    def change(self):
        if text.get() == 'IT WORKED!':
            text.set('Again')
        else:
            text.set('IT WORKED!')


#cb = Checkbutton(root, variable=status, command=change)
lb = Label(root, textvariable=text)
#cb.pack()
lb.pack()


my_gui = EmotionDetector(root)

root.mainloop()

