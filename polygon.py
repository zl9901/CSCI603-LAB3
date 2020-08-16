import turtle
import sys
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000


def init():
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.up()
    turtle.title('Name')
    turtle.pen()
    turtle.color()
    turtle.down()
    turtle.begin_fill()
    turtle.end_fill()


def drawTriangle(LENGTH):
    sum=0
    turtle.fillcolor("blue")
    turtle.begin_fill()
    for y in range(3):
        turtle.forward(LENGTH)
        turtle.left(120)
        sum=sum+LENGTH
    turtle.end_fill()
    return sum

def drawPolygon(LENGTH ,m):
    SUM=0
    assert m >= 0
    if m == 1:
        sum=drawTriangle(LENGTH)
        SUM=SUM+sum
    elif m == 0:
        pass
    elif m > 1:
        sum1=0
        for x in range (6):
            turtle.forward(LENGTH/2)
            s1=drawPolygon(LENGTH/2,m-1)
            turtle.forward(LENGTH / 2)
            turtle.left(60)
            sum1=sum1+LENGTH+s1
        SUM=SUM+sum1
    return SUM


def draw_rec(LENGTH , n, m,sides):
    SUM1=0
    assert n >=0
    if n == 1:
        SUM=drawPolygon(LENGTH,m)
        SUM1=SUM1+SUM
    elif n == 0:
        pass
    elif n > 1:
        sum2=0
        for y in range(sides):
            turtle.forward(LENGTH/2)
            s = draw_rec(LENGTH/2 , n-1,m,sides)
            turtle.forward(LENGTH / 2)
            turtle.left(180-(sides-2)*180/sides)
            sum2=sum2+LENGTH + s
        SUM1=SUM1+sum2
    return SUM1


def main():
    t = turtle.Turtle()
    init()
    turtle.speed(10)
    turtle.down()
    print(sys.argv)
    len(sys.argv)
    LENGTH = int(sys.argv[1])
    depth = int(sys.argv[2])
    sides = int(sys.argv[3])


    # hp1 = input("please input the depth you want")
    # depth = int(hp1)
    # hp= input("please input the sides you want")
    # sides=int(hp)
    SUM1=draw_rec(LENGTH,depth,2,sides)
    turtle.up()
    turtle.done()
    print("The sum is = " + str(SUM1) )



if __name__ == "__main__":
    main()
