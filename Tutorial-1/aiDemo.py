import turtle
import tkinter as tk


class VaccumCleaner:
    def __init__(self, canvas):
        self.cleaner = turtle.RawTurtle(canvas)
        self.cleaner.pencolor("#ff0000")  # Red

    def forward(self, steps=100):
        self.cleaner.forward(steps)

    def backward(self, steps=100):
        self.cleaner.backward(steps)

    def left(self, angle=90):
        self.cleaner.left(angle)

    def right(self, angle=90):
        self.cleaner.right(angle)


class GUI:
    def __init__(self, name, width, height):
        self.cleaner = 0

        self.root = tk.Tk(className=name)
        self.root.geometry(str(width)+"x"+str(height))
        self.root.resizable(0, 0)

        self.canvas = tk.Canvas(master=self.root,width=width/5*4,highlightthickness=0,bg="#c9c9c9")
        #self.canvas.grid(row=0, column=0) , ,height=height
        self.canvas.pack(side=tk.LEFT,fill=tk.BOTH)

        self.frame = tk.Frame(master=self.root,width=width/5*1,bg="#2b2b2b")
        #self.frame.grid(row=0, column=1) width=width/5*1,height=height
        self.frame.pack(side=tk.RIGHT,fill=tk.BOTH)
        # 

    def setCleaner(self, cleaner):
        self.cleaner = cleaner

    def setup(self,width):
        tk.Button(master = self.frame, text = "Forward", command = self.cleaner.forward,padx = width/5*1,pady=100).pack(side=tk.TOP)
        tk.Button(master = self.frame, text = "Backward", command = self.cleaner.backward,padx = width/5*1).pack(side=tk.TOP)
        tk.Button(master = self.frame, text = "Left", command = self.cleaner.left,padx = width/5*1).pack(side=tk.TOP)
        tk.Button(master = self.frame, text = "Right", command = self.cleaner.right,padx = width/5*1).pack(side=tk.TOP)
        

    def run(self):
        self.root.mainloop()


def main():
    root = GUI("AI Demo", 900, 600)
    vacCleaner = VaccumCleaner(root.canvas)
    root.setCleaner(vacCleaner)
    root.setup(900)
    root.run()


if __name__ == "__main__":
    main()
