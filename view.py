from tkinter import *
from logic import Logic

THEME_COLOR = "#375362"

class View:

    def __init__(self, logicInstance : Logic):
        self.logicInstance = logicInstance
        self.window = Tk()
        self.window.title("Quizzlet")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, pady = 20)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=500, height=400)
        self.canvas.config(bg="white")
        self.canvas.grid(row=1, column=0, columnspan=3)

        self.qText = self.canvas.create_text(250, 200, text = "dummy", fill = THEME_COLOR, width = 400)

        checkImage = PhotoImage(file="images/true.png")
        self.rightButton = Button(image=checkImage, highlightthickness=0, command =lambda: self.isTrueOrFalse("True"))
        self.rightButton.grid(row=2, column=0, pady=20)

        crossImage = PhotoImage(file="images/false.png")
        self.wrongButton = Button(image=crossImage, highlightthickness=0, command =lambda: self.isTrueOrFalse("False"))
        self.wrongButton.grid(row=2, column=2, pady=20)

        self.nextQuestion()
        self.window.mainloop()

    def nextQuestion(self):
        self.canvas.config(bg="white")
        if self.logicInstance.questionExists():
            self.score.config(text=f"Score: {self.logicInstance.score}")
            textt = self.logicInstance.nextQuestion()
            self.canvas.itemconfig(self.qText, text = textt)
        else:
            self.canvas.itemconfig(self.qText, text="You've reached the end of the quiz.")
            self.rightButton.config(state="disabled")
            self.wrongButton.config(state="disabled")

    def isTrueOrFalse(self, answer):
        if answer == self.logicInstance.currentQuestion.q_answer:
            self.logicInstance.score += 1
            self.canvas.config(bg="green")
        else:
            self.logicInstance.score += 0
            self.canvas.config(bg="red")
        self.window.after(1000, self.nextQuestion)


