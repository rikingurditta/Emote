import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
master = Tk()

"""
=== VARIABLES ===
emotions_list: a list of string emotions from the face API
check_def_for: a string variable, used to determine which definition to display
"""
emotions_list = ["happy","sad", "mad"]
check_def_for = StringVar()
check_def_for.set('Happy')
status = IntVar()

class Emotions(tk.Tk):

    def __init__(self, *args, **kwargs):

        # Format screens
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (EmotionsList, DefinitionsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
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
        label = tk.Label(self, text=emotions_list, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        # BUTTONS
        button0 = tk.Button(self, text="Definition0", command=self.change_current_emotion0(controller))
        button0.pack()
        button1 = tk.Button(self, text="Definition1", command=self.change_current_emotion1(controller))
        button1.pack()
        button2 = tk.Button(self, text="Definition2", command=self.change_current_emotion2(controller))
        button2.pack()

    def change_current_emotion0(self, controller):
        self.controller = controller
        check_def_for.set(emotions_list[0])

    def change_current_emotion1(self, controller):
        self.controller = controller
        check_def_for.set(emotions_list[1])

    def change_current_emotion2(self, controller):
        self.controller = controller
        check_def_for.set(emotions_list[2])

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
                           command=lambda: controller.show_frame("EmotionsList"))

        # Display Definition
        emotion = "contempt"
        emotion_def = emotional_meaning[emotion]
        label = tk.Label(self, text=emotion_def)
        label.pack(side="top", fill="x", pady=20)

        # Display Back Button
        button.pack()

    def display_def(self, emotion: str):
        """ Based on data given by _____ display the definitions corresponding to
        the emotion

        """
        emotion_def = emotional_meaning[emotion]
        label = tk.Label(self, text=emotion_def)
        label.pack(side="bottom", fill="x", pady=20)
        pass



if __name__ == "__main__":
    app = Emotions()
    app.mainloop()
