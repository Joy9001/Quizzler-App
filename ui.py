from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=500)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=40)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Courier", 12, "bold"))
        self.score_label.grid(row=0, column=1)

        self.ques_text = self.canvas.create_text(150, 110, text="Questions", width=280, fill=THEME_COLOR,
                                                 font=("Courier", 20, "italic"), anchor="n")

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_image, highlightthickness=0, bd=0, command=self.true_pressed)
        self.false_button = Button(image=self.false_image, highlightthickness=0, bd=0, command=self.false_pressed)

        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_ques()
        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            ques_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=ques_text)
        else:
            self.canvas.itemconfig(self.ques_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.quiz.score += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_ques)
