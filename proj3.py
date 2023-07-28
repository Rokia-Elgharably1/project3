# ASCII
print(r"""  ______             __                  ________  __                          __ 
 /      \           |  \                |        \|  \                        |  \
|  $$$$$$\ __    __  \$$ ________        \$$$$$$$$ \$$ ______ ____    ______  | $$
| $$  | $$|  \  |  \|  \|        \         | $$   |  \|      \    \  /      \ | $$
| $$  | $$| $$  | $$| $$ \$$$$$$$$         | $$   | $$| $$$$$$\$$$$\|  $$$$$$\| $$
| $$ _| $$| $$  | $$| $$  /    $$          | $$   | $$| $$ | $$ | $$| $$    $$ \$$
| $$/ \ $$| $$__/ $$| $$ /  $$$$_          | $$   | $$| $$ | $$ | $$| $$$$$$$$ __ 
 \$$ $$ $$ \$$    $$| $$|  $$    \         | $$   | $$| $$ | $$ | $$ \$$     \|  \
  \$$$$$$\  \$$$$$$  \$$ \$$$$$$$$          \$$    \$$ \$$  \$$  \$$  \$$$$$$$ \$$
      \$$$                                                                        
                                                                                  
                                                                      """)



#welcoming statement and explanition
print(" welcome to quiz time! you will answer a few true or false question. please only enter the letter T or F when it's your turn to answer. have fun!")

print()
print()

# truple for correct answer and the question
questions = ("Q1. there are seven planets in the solar sys", "Q2. Delaware was the 1st state", "Q3. The Walt Disney company was founded in 1910")
answers = ("T", "F", "T")
sum = 0

numberOfQuestions = len(questions)
print(numberOfQuestions)

for index in range(numberOfQuestions):
  ans = ""
  print(f"{questions[index]}")
  print(index)
  while (ans != "T" and ans != "F"):
    ans = input(" please enter true or false: ")
  # grade calculation statement
  if ans == answers[index]:
    sum += 1
print(f" you got {sum} out of 3 correct! Thanks for playing!")





