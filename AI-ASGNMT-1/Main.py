from VaccumCleaner import VaccumCleaner
from Environment import Environment
from Actions import Actions
import tkinter as tk
import time


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
 
    
    
            
    # vc.moveToXY(0,0,n)
    # for i in range(n):
    #     for j in range(n):
    #         vc.moveToXY(i,j,n)
    #         time.sleep(1)

    # # for x in Actions:
    # #     t = Environment.nextState(initState, x)
    # #     print("Cleaner pos {} {} in action : {}".format(t.vacCleanerX, t.vacCleanerY, t.action))

    t = initState
    
    for _ in range(12):
        t = Environment.nextState(t,Actions.S,vc)
        t = Environment.nextState(t,Actions.MR,vc)

    root.mainloop()


if __name__ == "__main__":
    main()