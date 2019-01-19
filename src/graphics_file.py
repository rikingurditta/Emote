from tkinter import Tk, Label, StringVar, IntVar, Button
root = Tk()

# STRINGS DEFINED HERE!

emotion = StringVar()
emotion.set('Happy')
status = IntVar()

emotion_desc = StringVar()
emotion_desc.set('')
status = IntVar()

class EmotionDetector:
    def __init__(self, master):
        self.master = master
        master.title("Emotion Detector")
        
        # BUTTONS ARE DEFINED HERE
        self.expand_button = Button(master, text="Expand", command=self.change, anchor="nw", justify="right", padx=2, bg = "blue")
        self.expand_button.pack()

    # THIS FUNCTION CHANGES THE TEXT
    def change(self):
        if emotion.get() == 'Happy':
            emotion_desc.set('A good feeling')
        else:
            emotion_desc.set('Its not happy.')

# THESE LINES ADD THE TEXT TO A LABEL
label1 = Label(root, textvariable=emotion)
label1.pack()
label2 = Label(root, textvariable=emotion_desc)
label2.pack()

my_gui = EmotionDetector(root)
root.mainloop()

