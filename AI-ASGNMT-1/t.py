x=0
y=0
n=10


l = [4.5-x for x in range(10)]
print(l)

#print("X: {} Y: {}".format(q,w))


def testGui():
    n = 10
    root = tk.Tk(className="AI Demo sbhdhr")
    canvas = tk.Canvas(root,width=500, height=500)
    canvas.pack()

    vc = VaccumCleaner(canvas)    
    vc.drawGrid(n,40)

    initState = Environment(None,n,0,0)    
    initState.generateDirt()
    

    t = initState
    t.vacCleanerX=6
    t.vacCleanerY=7

    t.board[6][7]=1

    vc.showState(t,40,25)

    time.sleep(2)

    # for x in Actions:
    #     s = Environment.nextState(t, x)
    #     #print("Cleaner pos {} {} in action : {}".format(s.vacCleanerX, s.vacCleanerY, s.action))
    #     vc.showState(s,40,25)
    #     time.sleep(1)
    #     vc.showState(t,40,25)
    #     time.sleep(1)

    root.mainloop()