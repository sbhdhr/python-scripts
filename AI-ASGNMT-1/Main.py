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


def main():
    n = 10
    length = 40
    dotSize = 20
    root = tk.Tk(className="AI Demo sbhdhr")
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    vc = VaccumCleaner(canvas,n,length,dotSize)
    vc.drawGrid()

    goalState = Environment(None, n, 0, 0)

    initState = Environment(None, n, 0, 0)
    initState.generateDirt(10)

    vc.showState(initState)

    #node2 = Node(goalState,[])

    #time.sleep(10)

    rootNode = Node(initState, [])

    # visitedNodes.append(rootNode)
    # visitedNodes.append(node2)

    # print(visited(rootNode))
    # print(visited(node2))

    #print(node2.env.goalTest(goalState))

    q = []

    q.append(rootNode)

    while(len(q) != 0):
        n = q.pop(0)
        # print(n)
        if (not visited(n)):
            visitedNodes.append(n)
            #vc.showState(n.env)
            #time.sleep(0.05)
            #print("Cleaner visiting : {} {} {}".format(
            #    n.env.vacCleanerX, n.env.vacCleanerY, n.env.action))

            if(n.env.goalTest(goalState)):
                print("Goal state reached")
                vc.showState(n.env)
                #vc.goHome()
                break

            for x in Actions:
                state = Environment.nextState(n.env, x)
                nextNode = Node(state, [])
                n.children.append(nextNode)
                q.append(nextNode)
        # else:
        #     print("Duplicate state. Ignored!")
        print("Queue Size: {}".format(len(q)))

        # for x in q:
        #     print(x.env.action, end="  ")
        # print(" ")

    root.mainloop()


if __name__ == "__main__":
    main()
