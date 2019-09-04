
import tkinter as tk

class EnvFrame(tk.Frame):
    def __init__(self, env, title='AIMA GUI', cellwidth=50, n=10):
        #update(self, cellwidth = cellwidth, running=False, delay=1.0)
        self.n = n
        self.running = 0
        self.delay = 1.0
        self.env = env
        tk.Frame.__init__(self, None, width=(cellwidth+2)*n, height=(cellwidth+2)*n)
        #self.title(title)
        # Toolbar
        toolbar = tk.Frame(self, relief='raised', bd=2)
        toolbar.pack(side='top', fill='x')
        #for txt, cmd in [('Step >', self.env.step), ('Run >>', self.run),
        #                 ('Stop [ ]', self.stop)]:
        tk.Button(toolbar, text=txt, command=cmd).pack(side='left')
        tk.Label(toolbar, text='Delay').pack(side='left')
        scale = tk.Scale(toolbar, orient='h', from_=0.0, to=10, resolution=0.5,
                         command=lambda d: setattr(self, 'delay', d))
        scale.set(self.delay)
        scale.pack(side='left')
        # Canvas for drawing on
        self.canvas = tk.Canvas(self, width=(cellwidth+1)*n,
                                height=(cellwidth+1)*n, background="white")
        self.canvas.bind('<Button-1>', self.left) ## What should this do?
        self.canvas.bind('<Button-2>', self.edit_objects)
        self.canvas.bind('<Button-3>', self.add_object)
        if cellwidth:
            c = self.canvas
            for i in range(1, n+1):
                c.create_line(0, i*cellwidth, n*cellwidth, i*cellwidth)
                c.create_line(i*cellwidth, 0, i*cellwidth, n*cellwidth)
                c.pack(expand=1, fill='both')
        self.pack()


    def background_run(self):
        if self.running:
            #self.env.step()
            ms = int(1000 * max(float(self.delay), 0.5))
            self.after(ms, self.background_run)

    def run(self):
        #print 'run'
        self.running = 1
        self.background_run()

    def stop(self):
        #print 'stop'
        self.running = 0

    def left(self, event):
        #print 'left at ', event.x/50, event.y/50
        pass

    def edit_objects(self, event):
        """Choose an object within radius and edit its fields."""
        pass

    def add_object(self, event):
        ## This is supposed to pop up a menu of Object classes; you choose the one
        ## You want to put in this square.  Not working yet.
        menu = tk.Menu(self, title='Edit (%d, %d)' % (event.x/50, event.y/50))
        for (txt, cmd) in [('Wumpus', self.run), ('Pit', self.run)]:
            menu.add_command(label=txt, command=cmd)
        menu.tk_popup(event.x + self.winfo_rootx(),
                      event.y + self.winfo_rooty())

        #image=PhotoImage(file=r"C:\Documents and Settings\pnorvig\Desktop\wumpus.gif")
        #self.images = []
        #self.images.append(image)
        #c.create_image(200,200,anchor=NW,image=image)

#v = VacuumEnvironment(); 
# 
w = EnvFrame(None)
w.mainloop()