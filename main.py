import turtle as t
import pandas
score = 0 
image = "./blank_states_img.gif"
screen = t.Screen()
turtle = t.Turtle()
output_list = []

def checker(guess):
    global score, states
    data = pandas.read_csv("./50_states.csv")
    states = data.state.to_list()
    if guess in states:
        score+=1
        file_opener(guess,data)


def file_opener(guess,data):
    
    required_row = data[data["state"]==guess]
    s = required_row["state"]
    state = s.to_string(index= False)
    x = int(required_row["x"])
    y = int(required_row["y"])
    name_writer(state,x,y)


def name_writer(state,x,y):
    new_turtle= t.Turtle()
    new_turtle.ht()
    new_turtle.penup()
    new_turtle.goto(x,y)
    new_turtle.write(state, align= 'center', font= ("Arial", 4, 'normal'))
    

screen.addshape(image)
turtle.shape(image)
uses_guessed = []
while score <=50:
    guess = screen.textinput(title=f"Name a state {score}/50", prompt="Enter a name of the state").title()
    if guess == "Exit":
        break
    else:
        checker(guess)
        uses_guessed.append(guess)

for i in states:
    if i not in uses_guessed:
        output_list.append(i)

x = pandas.DataFrame(output_list)
x.to_csv("learn-these.csv")