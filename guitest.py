import tkinter as tk


class testProgram():
    def __init__(self):
        self.r_root = tk.Tk()
        self.t_text = tk.StringVar()
        self.t_text.set("Tkinter Change Label Text")
        self.l_label = tk.Label(self.r_root, textvariable=self.t_text)
        self.b_button = tk.Button(self.r_root,
                                  text="Click here to change text written below",
                                  command=self.changeText)
        self.b_button.pack()
        self.l_label.pack()
        self.r_root.mainloop()

    def changeText(self):
        self.t_text.set("Tkinter Change Label Text Example")


app = testProgram()
