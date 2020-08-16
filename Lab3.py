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
    turtle.color('yellow')
    turtle.down()
    turtle.begin_fill()
    turtle.end_fill()

#to draw the basic case of triangle
def drawTriangle(LENGTH,fill):
    sum=0
    if fill =="fill":
#fill the color of the basic case of triangle
        turtle.fillcolor("blue")
        turtle.begin_fill()
        for y in range(3):
            turtle.forward(LENGTH)
            turtle.left(120)
            sum=sum+LENGTH
        turtle.end_fill()
    else:
        for y in range(3):
            turtle.forward(LENGTH)
            turtle.left(120)
            sum=sum+LENGTH
    return sum
#the second layer of the recursive,there are three parameters to execute the method
def drawPolygon(LENGTH ,m,fill):
    SUM=0
    assert m >= 0
    if m == 1:
        sum=drawTriangle(LENGTH,fill)
        SUM=SUM+sum
    elif m == 0:
        pass
    elif m > 1:
        sum1=0
        for x in range (6):
            turtle.forward(LENGTH/2)
#call the drawPolygon method itself
            s1=drawPolygon(LENGTH/2,m-1,fill)
            turtle.forward(LENGTH / 2)
            turtle.left(60)
#calculate the sum of the polygon
            sum1=sum1+LENGTH+s1
        SUM=SUM+sum1
    return SUM

#the first layer of the recursive,there are five parameters left
def draw_rec(LENGTH , n, m,sides,fill):
    SUM1=0
    assert n >=0
    if n == 1:
        SUM=drawPolygon(LENGTH,m,fill)
        SUM1=SUM1+SUM
    elif n == 0:
        pass
    elif n > 1:
        sum2=0
        for y in range(sides):
            turtle.forward(LENGTH/2)
#call the draw_rec method itself
            s = draw_rec(LENGTH/2 , n-1,m,sides,fill)
            turtle.forward(LENGTH / 2)
            turtle.left(180-(sides-2)*180/sides)
#calculate the sum of the sides
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
    ## The first element which should be input is the length of the polygon
    ## and the second element which shoud be input is the times of recursion
    ## and the third element which should be input is the sides of the polygon
    ## and the fourth element which should be input is the fill or unfill string
    ## whether the picture should be fill color or not.
    LENGTH = int(sys.argv[1])
    depth = int(sys.argv[2])
    sides = int(sys.argv[3])
    fill = sys.argv[4]

    SUM1=draw_rec(LENGTH,depth,2,sides,fill)
    turtle.up()
    turtle.done()
    print("The sum is = " + str(SUM1) )



if __name__ == "__main__":
    main()
