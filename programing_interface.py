from tkinter import *

#colors
bg = "#424242"
fg = "#e5e5e5"
button_bg = "#46664f"
button_fg = "#e5e5e5"

class Root(Tk):
    def __init__(self, *args, **kwords):
        super().__init__(*args, **kwords)
        self.current = 0
        self.windows = []

    def append(self, arg):
        self.windows.append(arg)
        return arg

    def next(self):
        if self.current >= len(self.windows):
            self.current += 1
    def back(self):
        if not self.current <= 0:
            self.current -= 1


class window(Frame):
    def __init__(self, root, *args, **kwords):
        super().__init__(root, *args, **kwords)
        self.menubar = Menu(root)
        self.menubar.add_command(label="Hello!", command=lambda : print("Hello!"))
        self.menubar.add_command(label="Quit!")

    def show(self):
        root.config(menu=self.menubar)



class code_interpreter(window):
    def _submit(self, text):
        print(text.get("1.0",END)) #prints "text"

    def __init__(self, root, *args, **kwords):
        super().__init__(root, *args, **kwords)
        self.main = Text(fg=fg,bg=bg)
        self.submit = Button(text="Submit", fg=button_fg, bg=button_bg, pady=2, borderwidth=0, height=1, command=lambda : self._submit(self.main))
        self.label = Label(fg=fg,bg=bg, text="\n\n\n", height = 3)




    def show(self):
        super().show()

        self.label.pack(fill=BOTH)
        self.submit.pack(fill=X)
        self.main.pack(fill=BOTH, expand=True)
        self.label.pack(fill=BOTH)



if __name__ == "__main__":
    root = Root()

    def loop():
        root.after(1000, loop)

    root.bind("<F11>", lambda x : root.attributes("-fullscreen", True))

    window = root.append(code_interpreter(root))
    window.show()

    loop()
    mainloop()
