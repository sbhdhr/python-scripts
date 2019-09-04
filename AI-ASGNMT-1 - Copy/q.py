from turtle import Screen, Turtle
import random

N = 10  # N by N grid
LENGTH = 60  # each grid element will be LENGTH x LENGTH pixels


def showMatrix(turtle_object, sparse_matrix):
    rows = len(sparse_matrix)

    if rows == 0:
        return

    columns = len(sparse_matrix[0])

    turtle_object.penup()

    for r in range(rows):
        for c in range(columns):
            if sparse_matrix[r][c] != 0:
                turtle_object.goto(-LENGTH*N/2,LENGTH*N/2)
                turtle_object.backward(r*LENGTH+(LENGTH/2))
                turtle_object.right(90)
                turtle_object.forward(c*LENGTH+(LENGTH/2))
                turtle_object.left(90)
                #turtle_object.goto()
                turtle_object.dot(40, "red")

    turtle_object.goto(-LENGTH*N/2+(LENGTH/2),-LENGTH*N/2+(LENGTH/2))

def generateDirt(board,p=50):
    dirtyTiles = int(p/100*N*N)
    # print(dirtyTiles)
    c=0
    while(c!=dirtyTiles):
        x = random.randint(0,N-1)
        y = random.randint(0,N-1)
        # print("x: "+str(x)+"  y: "+str(y))
        # print(self.board[x][y])
        if(board[x][y]!=1):
            board[x][y]=1
            c+=1

def grid(turtle, n, length):
    sign = 1
    for _ in range(2):

        for _ in range(n):
            turtle.forward(length * n)
            turtle.left(sign * 90)
            turtle.forward(length)
            turtle.left(sign * 90)
            sign = 0 - sign

        turtle.forward(length * n)
        [turtle.right, turtle.left][n % 2](90)
        sign = 0 - sign

screen = Screen()
yertle = Turtle()
yertle.speed(0)
yertle.penup()
yertle.goto(-N * LENGTH/2, -N * LENGTH/2)  # center our grid (optional)
yertle.pendown()

grid(yertle, N, LENGTH)
yertle.penup()
for i in range(2):
    yertle.right(90)
    yertle.forward(LENGTH/2)
yertle.left(90)


mat =  [[0 for x in range(N)] for j in range(N)]

showMatrix(yertle, mat)
generateDirt(mat,30)
showMatrix(yertle,mat)

screen.exitonclick()
