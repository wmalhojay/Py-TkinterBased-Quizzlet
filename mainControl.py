from daata import *
from qClass import *
from logic import *
from view import *

class Main:
    questionClassList = []

    for q in qAndA:
        q_text = q["question"]
        q_answer = q["correct_answer"]
        ques = Question(q_text, q_answer)
        questionClassList.append(ques)

    logicInstance = Logic(questionClassList)
    uiInstance = View(logicInstance)

    logicInstance.nextQuestion()

    print("Quiz Completed!")
    print(f"Your final score is: {logicInstance.score}/{len(questionClassList)}")