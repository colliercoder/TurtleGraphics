import turtle as t
import random
import colorgram
"""
def colors_from_image(image):
    colors = colorgram.extract(image,30)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)
        rgb_colors.append(new_color)
    return rgb_colors
#print(colors_from_image('dali.jpg'))
"""
color_list = [(47, 37, 40), (134, 90, 61), (241, 232, 204), (60, 43, 36), (190, 156, 113), (130, 162, 205),
              (209, 222, 238), (225, 198, 129), (232, 238, 235), (86, 54, 47), (167, 131, 76), (189, 106, 76),
              (87, 100, 121), (234, 226, 230), (165, 189, 226), (44, 45, 53), (163, 153, 157), (104, 88, 93),
              (97, 125, 166), (86, 66, 31), (79, 53, 57), (160, 166, 162), (94, 101, 96), (202, 188, 183),
              (51, 55, 51), (57, 61, 78), (152, 108, 116), (122, 130, 127), (196, 188, 194), (186, 195, 191)]
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
def create_painting(dot_size=20,width=400,height=300,painting_dimension = 10):
    t.screensize(canvwidth=width, canvheight=height)
    for line in range(painting_dimension):
        tim.penup()
        tim.setpos(-width + (dot_size * 2), (height-(dot_size*(line*(1.5)))))
        tim.pendown()
        for dot in range(painting_dimension): # paint a line of dots
            tim.dot(dot_size,random.choice(color_list))
            tim.penup()
            tim.forward(dot_size+(dot_size*(1/2)))
            tim.pendown()



create_painting(20,400,300,20)
screen = t.Screen()
screen.exitonclick()


"""
def change_color():
    R = random.randint(0,255)
    B = random.randint(0,255)
    G = random.randint(0,255)
    color = (R,G,B)
    return color

def shape_draw(max_side_shape=10):
    for sides in range(3,max_side_shape+1):
       angle = 360/sides
       for _ in range(sides):
           #tim.forward(100)
           tim.right(angle)
           tim.forward(100)
def random_walk(paths=100,speed = 0):
    tim.speed(speed)
    turn_options = [0, 90, 180, 270]
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
               "SeaGreen"]
    tim.width(10)
    for path in range(paths):
        if (-300 < tim.xcor() < 300) and (-300 < tim.ycor() < 300):
            tim.right(random.choice(turn_options))
            tim.color(change_color())
            tim.forward(random.randint(0,101))
        else:
            tim.right(180)
            tim.forward(random.randint(0, 101))
def spirograph(size_gap):
    tim.speed("fastest")
    for _ in range(int(360/size_gap)):
            tim.color(change_color())
            tim.circle(100)
            #current_heading = tim.heading()
            tim.setheading(tim.heading()+int(size_gap))
"""



