import turtle
import pandas as pd

myScreen = turtle.Screen()
myScreen.title("US State Game")
image = "blank_states_img.gif"
myScreen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df["state"].to_list()
correct_guess_list = []

while len(correct_guess_list) < 50:
    user_ans = myScreen.textinput(title=f"{len(correct_guess_list)}/50 States Correct", prompt="What's another states name?")
    # Check if the user wants to exit
    if user_ans is None or user_ans.lower() == "exit":
        break  # Exit the loop
    if user_ans:
        # Convert to title case
        title_case_input = user_ans.title()
        if title_case_input in all_states:
            row = df[df["state"] == title_case_input]
            x_value = row["x"].values[0]
            y_value = row["y"].values[0]
            correct_guess_list.append(row["state"].values[0])

            # Create a turtle object
            writer = turtle.Turtle()
            writer.penup()  # Lift the pen so it doesn't draw a line
            writer.hideturtle()  # Hide the turtle cursor

            # Move the turtle to the specified coordinates and write the name
            writer.goto(x_value, y_value)
            writer.write(row["state"].values[0], align="center", font=("Arial", 12, "normal"))

states_to_learn = [name for name in all_states if name not in correct_guess_list]

# Convert to DataFrame
new_df = pd.DataFrame(states_to_learn, columns=["States"])

# Save to CSV
new_df.to_csv("states_to_learn.csv", index=False)