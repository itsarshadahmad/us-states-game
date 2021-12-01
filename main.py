import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 the State",
                                    prompt="What's another state's name?").title()
    # print(answer_state)

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()

    if answer_state == "Exit":
        state_pending = [state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         state_pending.append(state)
        new_data = pandas.DataFrame(state_pending)
        new_data.to_csv("states_pending.csv")
        print(state_pending)
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# To get coordinates on mouse click
# def get_mouse_click_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

screen.exitonclick()
