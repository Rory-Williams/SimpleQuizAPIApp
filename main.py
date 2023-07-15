from question_model import Question
from data import generate_questions
from quiz_brain import QuizBrain
from ui import UserInterface

question_data = generate_questions()
question_bank = []
for question in question_data:
    # print(question)
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = UserInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
