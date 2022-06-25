import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# get xcor and ycor by click
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        # state_to_learn.csv
        # states_to_learn = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
        states_to_learn = [state for state in all_states if state not in guessed_states]

        states_to_learn_dict = {
            "state": states_to_learn
        }

        data = pandas.DataFrame(states_to_learn_dict)
        data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        target = data[data['state'] == answer_state]
        t.goto(int(target.x), int(target.y))
        t.write(answer_state)
        # t.write(target.state.item())  获取当前单元格的值

