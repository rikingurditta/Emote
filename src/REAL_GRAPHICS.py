import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from face import *
from emotions_dict import emotional_meaning
master = Tk()

"""
=== VARIABLES ===
emotions_list: a list of string emotions from the face API
check_def_for: a string variable, used to determine which definition to display
"""
emotions_list = top_3_emotions(screenshot())
svs = [StringVar(), StringVar(), StringVar()]
for i in range(3):
    svs[i].set(emotions_list[i])
check_def_for = StringVar()
check_def_for.set('Happy')
status = IntVar()
labels = []


# TODO: REMOVE THIS WHEN SHANNON IS DONE
emotional_meaning = {'anger': 0.0, 'contempt': 0.002, 'disgust': 0.0,
                     'fear': 0.0, 'happiness': 0.707, 'neutral': 0.276,
                     'sadness': 0.015, 'surprise': 0.0}


class Emotions(tk.Tk):  # THIS IS A CONTROLLER

    def __init__(self, *args, **kwargs):

        # Format screens
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18,
                                      weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # for loop constructing EmotionsList and DefinitionsPage frames,
        # putting them into the frames dict, making them children of container,
        # making the Emotions object their controller
        self.frames = {}
        for F in (EmotionsList, DefinitionsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # frame.pack()
        self.show_frame("EmotionsList")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


class EmotionsList(tk.Frame):
    """
    Initial page that shows the top 3 emotions detected by the API.
    Three buttons:
    button0 => change_current_emotion0
    button1 => change_current_emotion1
    button2 => change_current_emotion2
    Each button corresponds to the index of the emotions_list.
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        for j in range(len(emotions_list)):
            label = Label(self, text=emotions_list[j],
                          font=controller.title_font)
            label.grid(row=0, column=j)
            labels.append(label)
            tk.Button(self, text="Define", command=self.change_current_emotion(
                controller, j)).grid(row=1, column=j)

        rec = Canvas(controller)
        rec.create_rectangle(0, 0, 50, 50, fill="blue")
        rec.pack()

        rec = Canvas(controller)
        rec.create_rectangle(0, 0, 50, 50, fill="blue")
        rec.pack()

        rec = Canvas(controller)
        rec.create_rectangle(0, 0, 50, 50, fill="blue")
        rec.pack()

        # # BUTTONS
        # buttons = []
        # for i in range(3):
        #     buttons.append(tk.Button(self, text="Definition0",
        #                    command=self.change_current_emotion(controller, i)))
        #     buttons[i].pack()

    def change_current_emotion(self, controller, num):
        self.controller = controller
        check_def_for.set(emotions_list[num])

        # MAKING RECTANGLES


"""
        canvas_width = 80
        canvas_height = 40
        w = Canvas(master,
                   width=canvas_width,
                   height=canvas_height)
        w.pack()
        w.create_rectangle(0, 0, 50, 50, fill="blue")
        mainloop()
"""


class DefinitionsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=emotions_list, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame(
                               "EmotionsList"))

        # Display Definition
        emotion = "contempt"
        emotion_def = "hi"
        label = tk.Label(self, text=emotion_def)
        label.pack(side="top", fill="x", pady=20)

        # Display Back Button
        button.pack()

    def display_def(self, emotion: str):
        """Based on data given by _____ display the definitions corresponding
        to the emotion
        """
        emotion_def = emotional_meaning[emotion]
        label = tk.Label(self, text=emotion_def)
        label.pack(side="bottom", fill="x", pady=20)
        pass


def facestuff():
    emotions_list = top_3_emotions(screenshot())
    print(emotions_list)
    print(len(labels))
    for i in range(len(labels)):
        print(i)
        labels[i].configure(text=emotions_list[i])
    print()
    print()
    app.after(3000, func=facestuff)


if __name__ == "__main__":
    app = Emotions()  # THIS IS THE CONTROLLER
    app.after(500, func=facestuff)
    app.mainloop()
