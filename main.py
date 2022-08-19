import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = ("D:\\Portfolio\\US states game\\us_states.gif")
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("D:\\Portfolio\\US states game\\50_states.csv")
state_list = data["state"].tolist()
guessed_states = []
correct_answers = 0
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{correct_answers}/50 states guessed", prompt=("What's another states's name?")).title()

    if answer == "Exit":
        state_to_learn = []
        for states in state_list:
            if states not in guessed_states:
                state_to_learn.append(states)
        pandas.DataFrame(state_to_learn).to_csv("states_to_learn.csv")
        break

    if answer in state_list:
        correct_answers += 1
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))   
        t.write(answer)
            


