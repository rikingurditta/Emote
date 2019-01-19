import tkinter as tk
from tkinter import font  as tkfont
from emotions_dict import emotional_meaning


class Emotions(tk.Tk):

    def __init__(self, *args, **kwargs):
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
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class EmotionsList(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the EmotionsList", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to DefinitionsPage",
                            command=lambda: controller.show_frame("DefinitionsPage"))
        button1.pack()


class DefinitionsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is DefinitionsPage", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the EmotionsList",
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
