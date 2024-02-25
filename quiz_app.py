# Quiz Application

import sys
import random


# Initialize a variable to keep track of the score
score = 0

# Subject 1 - Define a list of questions, options and correct answers as a dictionary
Python = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Venus", "b) Mercury", "c) Earth", "d) Mars"],
        "correct_answer": "d"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["a) Isaac Newton", "b) Albert Einstein", "c) Galileo Galilei", "d) Marie Curie"],
        "correct_answer": "b"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["a) Pacific Ocean", "b) Indian Ocean", "c) Southern Ocean", "d) Atlantic Ocean"],
        "correct_answer": "a"
    },
    {
        "question": "What is the fastest land animal on Earth?",
        "options": ["a) Cheetah", "b) Lion", "c) Elephant", "d) Giraffe"],
        "correct_answer": "a"
    },
    {
        "question": "Who is the author of the Harry Potter book series?",
        "options": ["a) J.R.R. Tolkien", "b) C.S. Lewis", "c) J.K. Rowling", "d) George R.R. Martin"],
        "correct_answer": "c"
    }
]

# Subject 1 - Define a list of questions, options and correct answers as a dictionary 
Computer_network = [
    {
        "question": "1.	What is a computer network?",
        "options": ["a) A device used to display information on a computer screen", "b) A collection of interconnected computers and devices that can communicate and share resources",
                     "c) A type of software used to create documents and presentations", "d) The physical casing that protects a computer’s internal components"],
        "correct_answer": "b"
    },
    {
        "question": "2.	Which of the following is an example of Bluetooth?",
        "options": ["a) wide area network", "b) virtual private network", "c) local area network", "d) personal area network"],
        "correct_answer": "d"
    },
    {
        "question": "3.	What is the full form of OSI?",
        "options": ["a) optical service implementation", "b) open service Internet", "c) open system interconnection", "d) operating system interface"],
        "correct_answer": "c"
    },
    {
        "question": "4.	How many layers are there in the ISO OSI reference model?",
        "options": ["a) 7", "b) 5", "c) 4", "d) 6"],
        "correct_answer": "a"
    },
    {
        "question": "5.	The term HTTP stands for?",
        "options": ["a) Hyper terminal tracing program", "b)	Hypertext tracing protocol", "c)	Hypertext transfer protocol", "d) Hypertext transfer program"],
        "correct_answer": "c"
    }
]

# chose subject of quiz

subject_names  = {"1": "Python", "2" : "Computer_network"}

print("\n")
print("*"*100)
print("Enter the topic number which you want to qiuz about?    ")
for key, value in subject_names.items():
    print("\t",key+")", value)

subject_choice = input("\nYour Choice : ")

# Continue until the user decides to quit
quit = True
while subject_choice.lower() != 'q':
    # Check if the entered task number is valid
    if subject_choice in subject_names:
        print("You have chosen:", subject_names[subject_choice])
        quit = False
        break
    else:
        print("Invalid choice. Please select a valid topic number.")

    # Prompt for the next choice
    subject_choice = input("Enter the topic number which you want to qiuz, or 'q' to quit: ")
if quit:
    print("Quitting the program. Goodbye!")
    sys.exit()


#-------------------------------------------------------------------------------------------------------


quiz_data = globals()[subject_names[subject_choice]] 
print("*"*100)
print("\n")


# Create a list of question_number from 0 to the length of quiz_data - 1
question_number = list(range(len(quiz_data)))


# to get a random order Shuffle the question_number 
random.shuffle(question_number)

# Iterate through the questions and ask the user
for i in question_number:
    current_question_no = quiz_data[i]
    
    print(f"Question : {current_question_no['question']}")
    for option in current_question_no['options']:
        print(option)
    
    user_answer = input("Your answer (a/b/c/d) : ").strip().lower()
    
    # Check if the user's answer is correct 
    if user_answer == current_question_no['correct_answer']:
        print("Correct Answer \n")
        score += 1
    else:
        print(f"Wrong Answer, The correct answer is: {current_question_no['correct_answer'].upper()}\n")

# Display the final score of user
print("*"*100)
print(f"You scored {score} out of {len(quiz_data)} questions.")

if score == len(quiz_data):
    print("Congratulations! You are the quiz champion!")
print("*"*100)
