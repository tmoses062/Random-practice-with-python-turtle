import turtle as t
import random

mine = t.Turtle()
screen = t.Screen()

# Practice
screen.title("I love you")
screen.bgcolor('red')
mine.color('pink')
mine.begin_fill()
mine.back(80)
mine.left(130)
mine.circle(-50, 180)
mine.left(100)
mine.circle(-50, 180)
mine.right(7)
mine.forward(110)
mine.right(90)
mine.goto(-80, 0)
mine.hideturtle()
mine.end_fill()

# Challenge 1       Draw a square
for _ in range(4):
    mine.forward(100)
    mine.right(90)

# Challenge 2       Draw a dashed line
screen.bgcolor("#800080")
mine.back(300)
screen.clear()
for num in range(50):
    mine.pendown()
    mine.forward(10)
    mine.penup()
    mine.forward(10)
screen.write("Home = ", True, align="centre")

# Challenge 3       Draw Polygons
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"
                                                       "", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
screen.title('Polygons')
mine.pensize(7)


def draw_polygon(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        mine.right(angle)
        mine.forward(100)


for num in range(3, 11):
    mine.color(random.choice(colors))
    draw_polygon(num)

mine.hideturtle()

# Challenge 4       Generate a Random Walk
screen.title('Random Walk')
direction = [0, 90, 180, 270]
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "Deep"
                                                       "SkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
mine.pensize(7)
mine.speed(0)
for _ in range(200):
    mine.right(random.choice(direction))     # OR mine.setheading(random.choice(direction))
    mine.color(random.choice(colors))
    mine.forward(20)

# Challenge 5         Generate a Random Walk with random colors
screen.title('Random Walk')
direction = [0, 90, 180, 270]
t.colormode(255)
mine.pensize(7)
mine.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


while True:
    mine.right(random.choice(direction))     # OR mine.setheading(random.choice(direction))
    mine.color(random_color())
    mine.forward(20)

# Challenge 6         Draw a Spirograph
mine.speed(0)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


for _ in range(90):
    mine.color(random_color())
    mine.right(-4)
    mine.circle(100)

screen.exitonclick()
