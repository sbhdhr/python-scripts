from VaccumCleaner import VaccumCleaner
from Environment import Environment
from Node import Node
from State import State
from Actions import Actions
import tkinter as tk
import queue


def main():

    vc = VaccumCleaner(tk.Canvas(None), 0, 0)

    initialState = State(Environment(5, 5), vc,None)
    initialState.env.generateDirt(20)

    rootNode = Node(initialState, [])

    q = []
    visited = []
   
  
    q.append(rootNode)
    #

    while(len(q)!=0):
        n = q.pop(0)
        if (n.state.cleaner.posx,n.state.cleaner.posy) not in visited:
            visited.append((n.state.cleaner.posx,n.state.cleaner.posy))
            print("Cleaner visiting : {} {} {}".format(n.state.cleaner.posx,n.state.cleaner.posy,n.state.action))
            for x in Actions:
                state = State.nextState(n.state,x)
                # print("Cleaner pos {} {} in action : {}".format(state.cleaner.posx,state.cleaner.posy,state.action))
                if(state.cleaner.posx,state.cleaner.posy) not in visited:
                    #print("adding action to queue : {}".format(x))
                    node = Node(state,[])
                    q.append(node)
        
        # for x in q:
        #     print(x.state.action ,end="  ")
        # print(" ")


if __name__ == "__main__":
    
    
