from VaccumCleaner import VaccumCleaner
from Environment import Environment
from Actions import Actions
import tkinter as tk
import time
from Node import Node


visitedNodes = []


def visited(node):
    if len(visitedNodes)==0:
        return False

    for x in visitedNodes:
        if(x.env.compare(node.env)):
            return True

    return False

def BFS(rootNode,goalState,path):
    q = []
    q.append(rootNode)

    while(len(q) != 0):
        n = q.pop(0)
        if (not visited(n)):
            visitedNodes.append(n)
            #vc.showState(n.env)

            if(n.env.goalTest(goalState)):
                print("Goal state reached")
                p=n
                while(p.parent != None):
                    path.append((p.env.vacCleanerX,p.env.vacCleanerY,p.env.action))
                    p = p.parent
                    
                return n

            for x in Actions:
                state = Environment.nextState(n.env, x)
                nextNode = Node(state, n)
                q.append(nextNode)
        # else:
        #     print("Duplicate state. Ignored!")
        print("Queue Size: {}".format(len(q)))
    return None


def main():
    n = 5
    length = 40
    dotSize = 20
    root = tk.Tk(className="AI Demo sbhdhr")
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    vc = VaccumCleaner(canvas,n,length,dotSize)
    vc.drawGrid()

    goalState = Environment(None, n, 0, 0)

    initState = Environment(None, n, 0, 0)
    initState.generateDirt(20)

    vc.showState(initState)

    rootNode = Node(initState, None)

    path = []
    finalState = BFS(rootNode,goalState,path)

    print(path)

    for x,y,z in path[::-1]:
        vc.moveToXY(x,y,True)
        if(z==Actions.S):
            vc.paintDot("white")
        time.sleep(0.5)
            

    vc.showState(finalState.env)

    root.mainloop()


if __name__ == "__main__":
    main()
