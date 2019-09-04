import turtle


class VaccumCleaner:

    l = [x-4.5 for x in range(10)]
    l2 = [4.5-x for x in range(10)]

    def __init__(self, canvas):
        self.vc = turtle.RawTurtle(canvas)

    def forward(self, steps=100):
        self.vc.forward(steps)

    def backward(self, steps=100):
        self.vc.backward(steps)

    def left(self, angle=90):
        self.vc.left(angle)

    def right(self, angle=90):
        self.vc.right(angle)

    def moveToXY(self, x, y, n, length=60, drawPath=False):
        if(not drawPath):
            self.vc.penup()

        self.vc.goto(VaccumCleaner.l[y]*length, VaccumCleaner.l2[x]*length)
        self.vc.setheading(90)
        self.vc.pendown()

    def paintDot(self, color, dotSize=35):
        self.vc.dot(dotSize, color)

    def goHome(self, n, length=60, corner=3, drawPath=False):
        if(not drawPath):
            self.vc.penup()
        self.vc.goto(-length*n / 2+(length/2), length*n/2-(length/2))
        self.vc.setheading(90)
        self.vc.pendown()

    def drawGrid(self, n, length=60):
        self.vc.speed(0)
        self.vc.penup()
        self.vc.goto(-n * length/2, -n * length/2)
        self.vc.pendown()
        sign = 1
        for _ in range(2):
            for _ in range(n):
                self.vc.forward(length * n)
                self.vc.left(sign * 90)
                self.vc.forward(length)
                self.vc.left(sign * 90)
                sign = 0 - sign

            self.vc.forward(length * n)
            [self.vc.right,  self.vc.left][n % 2](90)
            sign = 0 - sign

    def showState(self, env, length=60, dotSize=35):
            # self.drawGrid(env.n,length)
        self.reset(env.n)
        for r in range(env.n):
            for c in range(env.n):
                self.moveToXY(r, c, env.n)
                if env.board[r][c] == 0:
                    self.paintDot("white", dotSize)
                else:
                    self.paintDot("red", dotSize)

        self.moveToXY(env.vacCleanerX, env.vacCleanerY, env.n)

    def reset(self, n):
        self.vc.turtlesize(2, 2, None)
        self.goHome(n)

    