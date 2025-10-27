from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain):
        self.counter = 0
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_word = Label(text=f"Score: {self.score}", bg=THEME_COLOR)
        self.score_word.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="White", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=280, text="Question Test",
                                                font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        true_btn = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_btn, bg=THEME_COLOR, borderwidth=0, highlightthickness=0,
                                  command=lambda: self.check_ans("True"))
        self.true_button.grid(row=2, column=0)

        false_btn = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_btn, bg=THEME_COLOR, borderwidth=0, highlightthickness=0,
                                   command=lambda: self.check_ans("False"))
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text=f"You've reached end of the quiz. Your final score is "
                                                       f"{self.score}/{self.quiz.question_number}")

    def check_ans(self, user_ans):
        self.counter += 1
        if self.counter <= len(self.quiz.question_list):
            is_correct = self.quiz.check_answer(user_answer=user_ans)
            if is_correct:
                self.score += 1
                self.canvas.config(bg="green")
                self.window.after(1000, self.get_next_question)
            else:
                self.canvas.config(bg="red")
                self.window.after(1000, self.get_next_question)
            self.score_word.config(text=f"Score: {self.score}")
