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
emotions_list = top_3_emotions(screenshot())
svs = [StringVar(), StringVar(), StringVar()]
for i in range(3):
    svs[i].set(emotions_list[i])
check_def_for = StringVar()
check_def_for.set('Happy')
status = IntVar()
LABEL_WIDTH = 30
labels = []
texts = []


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
        """ Initiaizes frames, layers and general page layout"""
        tk.Frame.__init__(self, parent)
        self.draw_rectangle(controller)
        """
        # Draw Buttons
        for j in range(len(emotions_list)):
            # Initialize background based on colour
            print(emotion_colour[emotions_list[j]])
            colour = emotion_colour[emotions_list[j]]
            self.text = tk.Text(self, bg=colour, width=30, height=10) #emotion_colour[emotions_list[j]])
            self.text.grid(row=2, column=j, rowspan=1)

            # Find emotion in list
            label = Label(self.text, text=emotions_list[j],
                            font=controller.title_font, bg=colour)
            label.place(relx=0.35, rely=0.4)
            labels.append(label)

            # Display button with corresponding emotion
            button = tk.Button(self.text, text="Define", command=lambda:self.change_current_emotion(
                controller, j))
            button.place(relx=(0.35), rely=0.6)
        """

    def draw_rectangle(self, controller):
        """ Draw Buttons and Widgets"""
        for j in range(len(emotions_list)):
            # Initialize background based on colour
            colour = emotion_colour[emotions_list[j]]
            self.text = tk.Text(self, bg=colour, width=LABEL_WIDTH, height=10)
            texts.append(self.text)
            self.text.grid(row=2, column=j, rowspan=1)

            # Find emotion in list
            label = Label(self.text, text=emotions_list[j],
                            font=controller.title_font, bg=colour)
            label.place(relx=0, rely=0.4)
            labels.append(label)

            # Display button with corresponding emotion
            button = tk.Button(self.text, text="Define", command=lambda:self.change_current_emotion(
                controller, j))
            button.place(relx=(0.35), rely=0.6)


        '''
        rec = Canvas(controller)
        rec.create_rectangle(0, 0, 50, 50, fill="blue")
        rec.pack()

        rec = Canvas(controller)
        rec.create_rectangle(0, 0, 50, 50, fill="blue")
        rec.pack()

        rec = Canvas(controller)
        rec.create_rectangle(0, 0, 50, 50, fill="blue")
        rec.pack()
        '''

        # # BUTTONS
        # buttons = []
        # for i in range(3):
        #     buttons.append(tk.Button(self, text="Definition0",
        #                    command=self.change_current_emotion(controller, i)))
        #     buttons[i].pack()

    def change_current_emotion(self, controller, num):
        self.controller = controller
        check_def_for.set(emotions_list[num])
        controller.show_frame("DefinitionsPage")

    def change_current_colour(self, controller, num):
        pass

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
    thresh = 0.2
    emotions_list = screenshot()
    top_3_list = top_3_emotions(emotion_threshold(emotions_list, thresh))
    top_ws_list = top_3_widths(emotion_threshold(emotions_list, thresh), LABEL_WIDTH)
    print(emotions_list)
    print(len(labels))
    for i in range(len(labels)):
        print(i)
        colour = emotion_colour[top_3_list[i]]
        labels[i].configure(text=top_3_list[i], bg=colour, width=top_ws_list[i])
        texts[i].configure(bg=colour, width=top_ws_list[i])
    print()
    print()
    app.after(4000, func=facestuff)


if __name__ == "__main__":
    app = Emotions()  # THIS IS THE CONTROLLER
    app.after(500, func=facestuff)
    app.mainloop()
