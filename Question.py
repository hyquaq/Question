class Question:
    def __init__(self, ques, ans1, ans2, ans3, ans4, right):
        self.ques = ques
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.right = right

    def showTitle(self):
        print("Cau hoi: {}\n".format(self.ques))

    def check(self, e):
        if (str(self.right).__eq__(str(e))):
            return True
        return False

    def getAnswer(self):
        return self.right

    def __repr__(self):
        return "\nCau hoi la: {}\nA. {}\nB. {}\nC. {}\nD. {}\n".format(
            self.ques, self.ans1, self.ans2, self.ans3, self.ans4)

    def __str__(self):
        return "\nCau hoi la: {}\nA. {}\nB. {}\nC. {}\nD. {}\n".format(
            self.ques, self.ans1, self.ans2, self.ans3, self.ans4)
