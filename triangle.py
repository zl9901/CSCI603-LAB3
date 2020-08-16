import turtle
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

def init():
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.up()
    turtle.title('Name')
    turtle.pen()
    turtle.down()

LENGTH=200
def drawLength(LENGTH):
    for x in range (3):
        turtle.forward(LENGTH)
        turtle.left(120)

def draw_rec(LENGTH , n):
    assert n >= 0
    if n == 1:
        drawLength(LENGTH)
    elif n == 0:
        pass
    elif n > 1:
        for y in range(3):
            turtle.forward(LENGTH)
            draw_rec(LENGTH/2 , n-1)
            turtle.left(120)

def main():
    t = turtle.Turtle()
    init()
    turtle.speed(2)
    turtle.down()
    draw_rec(LENGTH , 5)
    turtle.up()
    turtle.done()

if __name__ == "__main__":
    main()
