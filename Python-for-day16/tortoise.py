from turtle import Turtle, Screen

t = Turtle()
my_screen = Screen()


print(t)
t.shape("turtle")
t.color("orchid")
t.width(3)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.home()
for step in range(30):
    for c in ('orchid', 'blue', 'red', 'green', 'pink', 'purple'):
        t.color(c)
        t.forward(step)
        t.right(30)

my_screen.exitonclick()


# https://docs.python.org/3/library/turtle.html#turtle.listen
# https://cs111.wellesley.edu/reference/colors
