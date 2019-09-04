from Actions import Actions
from VaccumCleaner import VaccumCleaner
from Environment import Environment
import tkinter as tk
import copy


class State:
    def __init__(self, env, cleaner, action):
        self.env = env
        self.cleaner = cleaner
        self.action = action

    

                      
       

def main():    
    env = Environment()
    env.generateDirt()


    root = tk.Tk()
    canvas = tk.Canvas(root)
    s = State(env, VaccumCleaner(canvas,0,0), None)

    for x in Actions:
        t = State.nextState(s, x)
        print("Cleaner pos {} {} in action : {}".format(t.cleaner.posx, t.cleaner.posy, t.action))

    # s.env.print()
    # print("  ")
    # s.env.generateDirt(20)
    # #s.setCleaner()
    # print("before cleaning")
    # s.env.print()
    # print("===================")

    # for x in range(12):
    #     t = s.nextState(Actions.S)
    #     t = s.nextState(Actions.ML)
    #     #print("cleaner : x : {} y: {}".format(t.cleaner.posx, t.cleaner.posy))
    #     t.env.print()
    #     print("   ")



if __name__ == "__main__":
    main()
