import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from face import *
from emotions_dict import emotional_meaning
from colour_scheme import emotion_colour

master = Tk()

"""
=== VARIABLES ===
emotions_list: a list of string emotions from the face API
check_def_for: a string variable, used to determine which definition to display
"""
THRESHOLD = 0.1
LABEL_WIDTH = 30

emotions_list = emotion_threshold(screenshot(), THRESHOLD)
top_3_list = top_3_emotions(emotions_list)
top_ws_list = top_3_widths(emotion_threshold(emotions_list, THRESHOLD), LABEL_WIDTH)

check_def_for = StringVar()
status = IntVar()

labels = []
texts = []
title_label = []
emotion_text_label = None
clicked_on = 'fear'


class Emotions(tk.Tk):  # THIS IS A CONTROLLER

    def __init__(self, *args, **kwargs):

        # Format screens
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=30,
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
        """ Initiaizes frames, layers and general page layout"""
        tk.Frame.__init__(self, parent)
        self.draw_rectangle(controller)


    def draw_rectangle(self, controller):
        """ Draw Buttons and Widgets """
        font = tkfont.Font(family='Helvetica', size=30,
                                      weight="bold", slant="italic")
        # ++++++ BUTTON 0 ++++++
        # Initialize background based on colour
        colour = emotion_colour[top_3_list[0]]
        self.text = tk.Text(self, bg=colour, width=LABEL_WIDTH, height=10)
        texts.append(self.text)
        self.text.grid(row=2, column=0, rowspan=1)

        # Find emotion in list
        label = Label(self.text, text=top_3_list[0],
                        font=font, bg=colour, anchor="w")
        label.config(font=("Helvetica", 44))
        label.place(relx=0.3, rely=0.2)
        labels.append(label)

        # Display button with corresponding emotion
        button0 = tk.Button(self.text, text="Define", command=lambda:self.change_current_emotion0(
            controller))
        button0.place(relx=(0.35), rely=0.6)

        # ++++++ BUTTON 1 ++++++
        # Initialize background based on colour
        colour = emotion_colour[top_3_list[1]]
        self.text = tk.Text(self, bg=colour, width=LABEL_WIDTH, height=10)
        texts.append(self.text)
        self.text.grid(row=2, column=1, rowspan=1)

        # Find emotion in list
        label = Label(self.text, text=top_3_list[1],
                        font=controller.title_font, bg=colour)
        label.config(font=("Helvetica", 44))
        label.place(relx=0, rely=0.2)
        labels.append(label)

        # Display button with corresponding emotion
        button1 = tk.Button(self.text, text="Define", command=lambda:self.change_current_emotion1(
             controller))
        button1.place(relx=(0.35), rely=0.6)

        # ++++++ BUTTON 2 ++++++
        # Initialize background based on colour
        colour = emotion_colour[top_3_list[2]]
        self.text = tk.Text(self, bg=colour, width=LABEL_WIDTH, height=10)
        texts.append(self.text)
        self.text.grid(row=2, column=2, rowspan=1)

        # Find emotion in list
        label = Label(self.text, text=top_3_list[2],
                            font=controller.title_font, bg=colour)
        label.config(font=("Helvetica", 44))
        label.place(relx=0, rely=0.2)
        labels.append(label)

        # Display button with corresponding emotion
        button2 = tk.Button(self.text, text="Define", command=lambda:self.change_current_emotion2(
            controller))
        button2.place(relx=(0.35), rely=0.6)

    def change_current_emotion0(self, controller):
        global emotion_text_label
        self.controller = controller
        controller.show_frame("DefinitionsPage")
        colour = emotion_colour[top_3_list[0]]
        title_label[0].configure(text=top_3_list[0], fg=colour)
        emotion_text_label.configure(text=emotional_meaning[top_3_list[0]])

    def change_current_emotion1(self, controller):
        global emotion_text_label
        self.controller = controller
        controller.show_frame("DefinitionsPage")
        title_label[0].configure(text=top_3_list[1])
        emotion_text_label.configure(text=emotional_meaning[top_3_list[1]])

    def change_current_emotion2(self, controller):
        global emotion_text_label
        self.controller = controller
        controller.show_frame("DefinitionsPage")
        title_label[0].configure(text=top_3_list[2])
        emotion_text_label.configure(text=emotional_meaning[top_3_list[2]])


class DefinitionsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text=emotions_list)
        label.config(font=("Helvetica", 44))
        label.pack(side="top", fill="x", pady=10)
        title_label.append(label)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame(
                               "EmotionsList"))

        # Display Definition
        emotion_def = emotional_meaning[clicked_on]
        label = tk.Label(self, text=emotion_def)
        global emotion_text_label
        emotion_text_label = label
        label.pack(side="top", fill="x", pady=20)

        # Display Back Button
        button.pack()


def facestuff():
    global emotions_list
    global top_3_list
    global top_ws_list
    emotions_list = emotion_threshold(screenshot(), THRESHOLD)
    top_3_list = top_3_emotions(emotion_threshold(emotions_list, THRESHOLD))
    top_ws_list = top_3_widths(emotion_threshold(emotions_list, THRESHOLD), LABEL_WIDTH)
    for i in range(len(labels)):
        colour = emotion_colour[top_3_list[i]]
        labels[i].configure(text=top_3_list[i], bg=colour, width=top_ws_list[i])
        texts[i].configure(bg=colour, width=top_ws_list[i])
    app.after(4000, func=facestuff)

if __name__ == "__main__":
    app = Emotions()  # THIS IS THE CONTROLLER
    app.after(500, func=facestuff)
    app.mainloop()
