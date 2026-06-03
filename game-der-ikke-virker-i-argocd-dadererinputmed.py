def ask_question():
    """This function asks a quiz question and returns 1 if the answer is correct, otherwise 0."""
    pass


print("Welcome to my game")

playing = input("Do you want to play: ")

while playing.lower() != "yes" and playing.lower() != "no":
    print("Please answer yes or no")
    playing = input("Do you want to play: ")

if playing.lower() == "no":
    quit()
elif playing.lower() == "yes":
    print("Okay lets go")
    score = 0

    answer = input("What does CPU stand for?: ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

    answer = input("What does GPU stand for?: ")
    if answer.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

    answer = input("What does RAM stand for?: ")
    if answer.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

    answer = input("What does PSU stand for?: ")
    if answer.lower() == "power supply":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

    answer = input("Is this a boring quiz?: ")
    if answer.lower() == "no":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 5) * 100) + "%")

    playing = input("Do you want to play again?: ")

print("Thanks for playing!")

