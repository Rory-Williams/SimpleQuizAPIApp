from tkinter import *
from quiz_brain import QuizBrain
# from main import q_list_gen

THEME_COLOR = "#375362"

class UserInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = 'Quiz App'
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='#FFFFFF')
        self.canvas.grid(column=1, row=2, columnspan=2, pady=20, padx=20)
        self.q_text = self.canvas.create_text(150, 125,
                                              text='Question',
                                              fill=THEME_COLOR,
                                              font=('Arial', 16, 'italic'),
                                              width=280)

        self.score_val = 0
        self.score_txt = f'Score: {self.score_val}'
        self.score = Label(text=self.score_txt,
                           font=('Arial', 12, 'bold'),
                           fg='#FFFFFF',
                           bg=THEME_COLOR)
        self.score.grid(column=2, row=1, pady=20, padx=20)

        true_image = PhotoImage(file="images/true.png")
        self.true_butt = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR)
        self.true_butt.grid(column=1, row=3, pady=20, padx=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_butt = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR)
        self.false_butt.grid(column=2, row=3, pady=20, padx=20)
        self.config_quiz_buttons()

        self.next_question()
        self.window.mainloop()

    def true_ans(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_ans(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def inc_score(self):
        self.score_val += 1

    def next_question(self):
        self.canvas.config(bg='#FFFFFF')
        self.qs = self.quiz.question_number
        self.score['text'] = f'Score: {self.score_val}/{self.qs}'
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)

        else:
            self.canvas.itemconfig(self.q_text, text='End of quiz, try another?')
            # self.true_butt.config(command=self.reset_quiz)
            # self.false_butt.config(command=self.end_quiz)
            self.end_quiz()

    def give_feedback(self, is_right):
        if is_right:
            self.inc_score()
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(500, self.next_question)

    def config_quiz_buttons(self):
        self.true_butt.config(command=self.true_ans)
        self.false_butt.config(command=self.false_ans)

    # def reset_quiz(self):
    #     self.config_quiz_buttons()
    #     self.score_val = 0
    #     self.next_question()
    #     self.quiz = QuizBrain(q_list_gen())

    def end_quiz(self):
        self.true_butt.config(state='disabled')
        self.false_butt.config(state='disabled')
        self.canvas.itemconfig(self.q_text, text='End of quiz, please close window')


