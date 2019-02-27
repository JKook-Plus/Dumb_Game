from tkinter import *
from PIL import Image, ImageTk
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
        self.prevpage = None

    def append(self, arg):
        self.windows.append(arg)
        return arg

    def next(self):
        self.current += 1
    def back(self):
        self.current -= 1

    def show(self):
        if not self.current == self.prevpage:
            self.windows[self.current].pack_forget()
        self.windows[self.current].show()
        self.prevpage = self.current


class window(Frame):
    def __init__(self, root, *args, **kwords):
        super().__init__(root, *args, **kwords)
        self.menubar = Menu(root)
        self.menubar.add_command(label="Hello!", command=lambda : print("Hello!"))
        self.menubar.add_command(label="Quit!")

        self.menubar.add_command(label="Next", command=root.next)
        self.menubar.add_command(label="Back", command=root.back)

    def show(self):
        root.config(menu=self.menubar)



class code_interpreter(window):
    def _submit(self, text):
        print(text.get("1.0",END)) #prints "text"

    def __init__(self, *args, **kwords):
        super().__init__(self, *args, **kwords)
        self.main = Text(self, fg=fg,bg=bg)
        self.submit = Button(self, text="Submit", fg=button_fg, bg=button_bg, pady=2, borderwidth=0, height=1, command=lambda : self._submit(self.main))
        self.label = Label(self, fg=fg, bg=bg, text="\n\n\n", height = 3)
        a = (PhotoImage("adventure-aerial-beautiful-351448.png"))
        self.image = Label(self, image=(a))

    def show(self):
        super().show()
        self.image.pack(fill=BOTH)
        self.label.pack(fill=BOTH)
        self.submit.pack(fill=X)
        self.main.pack(fill=BOTH, expand=True)
        self.label.pack(fill=BOTH)

class test(window):
    def __init__(self, root, *args, **kwords):
        super().__init__(root, *args, **kwords)
        self.main = Label(root, fg=fg,bg=bg, text = "test")

    def show(self):
        super().show()

        self.main.pack(fill=BOTH, expand=True)



if __name__ == "__main__":
    root = Root()

    def loop():
        root.show()
        root.after(1000, loop)

    root.bind("<F11>", lambda x : root.attributes("-fullscreen", True))

    coder = root.append(code_interpreter(root))
    ts = root.append(test(root))



    loop()
    mainloop()
