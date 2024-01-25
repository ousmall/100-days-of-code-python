from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain  # import it so that the program knows what you want

THEME_COLOR = "#375362"
LABEL_FONT = ('Ariel', 12, 'bold')
TEXT_FONT = ('Ariel', 18, 'bold')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # type hints, describes the expected type of parameter quiz_brain
        # create a parameter which refer to QuizBrain class in this initial
        self.quiz = quiz_brain
        # Create a property named quiz to receive information from the quiz_brain module
        self.window = Tk()
        self.window.title("Fast Quiz")
        self.window.config(padx=50, pady=20, bg=THEME_COLOR)

        self.label = Label(text=f"Score: 0 ", font=LABEL_FONT)
        self.label.config(bg=THEME_COLOR, fg="white")
        self.label.grid(column=2, row=1)

        self.canvas = Canvas(width=300, height=300)
        self.question_text = self.canvas.create_text(150, 150,
                                                     width=280,
                                                     text="",
                                                     font=TEXT_FONT,
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

        yes_img = PhotoImage(file="images/true.png", )
        self.yes_button = Button(image=yes_img, highlightthickness=0, command=self.guess_true)
        self.yes_button.grid(column=1, row=3)

        no_img = PhotoImage(file="images/false.png")
        self.no_button = Button(image=no_img, highlightthickness=0, command=self.guess_false)
        self.no_button.grid(column=2, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):  # create a function to call another function elsewhere
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            yes = messagebox.askyesno(title="Notification",
                                      message="You have finished all the questions!"
                                              "\nWould you like to start a new around?")

            if yes:
                self.window.after(1000, self.quiz.reset_quiz())
                self.get_next_question()
            else:
                self.yes_button.config(state="disabled")  # disable the buttons
                self.no_button.config(state="disabled")
                return

    def guess_true(self):
        right = self.quiz.check_answer("True")
        self.screen_feedback(right)

    def guess_false(self):
        right = self.quiz.check_answer("False")
        self.screen_feedback(right)

    def screen_feedback(self, right):
        if right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        # white screen is not belongs to here, so I should paste it in 'get_next_question()'
        self.label.config(text=f"Score: {self.quiz.score} ")
