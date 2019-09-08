from VaccumCleaner import VaccumCleaner
from Environment import Environment
from Actions import Actions
import tkinter as tk
import time
from Node import Node
from BFS import BFS, getQueueSize
import threading
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.style as style
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

finalState = None
queueSize = []
signal = True
second = 0
seconds = []
initState = None


def BFSThread(rootNode, goalState, path):
    global finalState
    global signal
    global queueSize
    global seconds
    finalState = BFS(rootNode, goalState, path, queueSize)
    signal = False

    #print("Queue Size: {}".format(len(queueSize)))


def AnalysisThread(root):

    global second
    global signal

    while(signal == True):
        queueSize.append(getQueueSize())
        second += 1
        seconds.append(second)


def generateDirtBtn(n, vc):
    global initState

    vc.vc.reset()
    vc.drawGrid()
    initState = Environment(None, n, 0, 0)

    initState.generateDirt(10)
    vc.showState(initState)


def doBFS(n, a, root, vc, canvas2):
    global initState

    goalState = Environment(None, n, 0, 0)
    rootNode = Node(initState, None)

    path = []

    t1 = threading.Thread(target=BFSThread, args=(rootNode, goalState, path,))
    t2 = threading.Thread(target=AnalysisThread, args=(root,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    tk.messagebox.showinfo("Title", "Got action path")

    a.plot(queueSize)
    canvas2.draw()

    if len(path) > 0:
        for x, y, z in path[::-1]:
            vc.moveToXY(x, y, True)
            if(z == Actions.S):
                vc.paintDot("white")
            time.sleep(0.5)

    if finalState != None:
        vc.goHomeAftCleaning(finalState.env.vacCleanerX,
                             finalState.env.vacCleanerY)
        tk.messagebox.showinfo("Title", "Reached Home")


def main():
    n = 8
    length = 40
    dotSize = 20

    plt.style.use("fivethirtyeight")
    matplotlib.use("TkAgg")
    root = tk.Tk(className="AI Demo sbhdhr")
    root.geometry("1280x720")
    canvas = tk.Canvas(root, width=1280/2, height=720/2)
    canvas.grid(row=0, column=0, sticky=tk.W+tk.N)

    f = plt.Figure(figsize=(8, 4.5), dpi=80)
    a = f.add_subplot(111)

    canvas2 = FigureCanvasTkAgg(f, master=root)
    # canvas2.figure.set_figwidth(200)
    canvas2.draw()
    canvas2.get_tk_widget().grid(row=0, column=1, sticky=tk.E+tk.N)

    frame1 = tk.Frame(root, bg="grey", width=1280*2/3, height=720/2)
    frame1.grid(row=1, column=0, sticky=tk.W+tk.N,
                columnspan=2, padx=0, pady=0, ipadx=0, ipady=0)

    frame2 = tk.Frame(root, width=1280/3, height=720/2)
    frame2.grid(row=1, column=1, padx=0, pady=0, ipadx=0, ipady=0)

    btn1 = tk.Button(frame2, text="Generate Dirt",
                     command=lambda: generateDirtBtn(n, vc))
    btn1.grid(row=0, padx=30, pady=30)

    btn2 = tk.Button(frame2, text="Start BFS",
                     command=lambda: doBFS(n, a, root, vc, canvas2))
    btn2.grid(row=3)

    vc = VaccumCleaner(canvas, n, length, dotSize)
    vc.drawGrid()

    root.mainloop()


if __name__ == "__main__":
    main()
