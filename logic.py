
class Logic:

    def __init__(self, questionClassList):
        self.qNumber = 0
        self.score = 0
        self.questionClassList = questionClassList
        self.currentQuestion = None
    
    def questionExists(self):
        return self.qNumber < len(self.questionClassList)   
    
    def nextQuestion(self):
        if self.questionExists():
            self.currentQuestion = self.questionClassList[self.qNumber]
        self.qNumber += 1
        return f"{self.qNumber}. {self.currentQuestion.q_text} (True/False) : "
    
