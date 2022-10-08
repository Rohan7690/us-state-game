# FOR GETTING THE COORDINATES OF STATES
# import turtle
# def get_mouse_click_coor(x,y):
#     print(x,y)
# screen = turtle.Screen()
# screen.title("Indian Map")
# image = "India_outline_map_img.gif"
# screen.addshape(image)
# turtle.shape(image)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

import turtle
import pandas
ALIGNMENT = "center"
FONT = ("courier", 10, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:

    answer_states = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                     prompt="What's another state's name").title()

    coordinates = data[data.state == answer_states]
    if answer_states == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        print(missing_states)


    if answer_states in all_states:
        guessed_states.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(coordinates.x), int(coordinates.y))
        t.write(answer_states)

# states to learn.csv
