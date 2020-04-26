import tkinter as tk

q_a = [
    ["label 1", [1,2,3,4]],
    ["label 2", [5,6,7,8]],
]    

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.label = tk.Label(self)
        self.label.pack()

        self.button1 = tk.Button(self, command=self.loop)
        self.button1.pack()

        self.button2 = tk.Button(self, command=self.loop)
        self.button2.pack()

        self.button3 = tk.Button(self, command=self.loop)
        self.button3.pack()

        self.button4 = tk.Button(self, command=self.loop)
        self.button4.pack()

        self.last = len(q_a)
        self.current = -1

        # set first text 
        # because `self.current = -1` then it use `self.current = 0`
        self.loop()

    def loop(self):

        # get next element from list
        self.current += 1

        if self.current == self.last:
            self.label.configure(text="The end")
            # hide buttons
            self.button1.forget()
            self.button2.forget()
            self.button3.forget()
            self.button4.forget()
        else:
            self.label['text'] = q_a[self.current][0]
            self.button1['text'] = q_a[self.current][1][0]
            self.button2['text'] = q_a[self.current][1][1]
            self.button3['text'] = q_a[self.current][1][2]
            self.button4['text'] = q_a[self.current][1][3]


if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()