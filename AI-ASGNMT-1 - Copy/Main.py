from VaccumCleaner import VaccumCleaner
from Environment import Environment
from Actions import Actions
import tkinter as tk


def main():
    n = 10
    root = tk.Tk(className="AI Demo sbhdhr")
    canvas = tk.Canvas(root,width=1280, height=720)
    canvas.pack()

    vc = VaccumCleaner(canvas)
    
    vc.drawGrid(n)

    initState = Environment(None,n,0,0)
    
    initState.generateDirt()
    vc.showState(initState)

    # for x in Actions:
    #     t = Environment.nextState(initState, x)
    #     print("Cleaner pos {} {} in action : {}".format(t.vacCleanerX, t.vacCleanerY, t.action))

    t = initState
    
    for x in range(12):
        t = Environment.nextState(t,Actions.S)
        t = Environment.nextState(t,Actions.MR)
        
    vc.showState(t)

    root.mainloop()


if __name__ == "__main__":
    main()