class Question:
    def __init__(self, ques, ans1, ans2, ans3, ans4, key, cRight=0, cWrong=0):
        self.ques = ques
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.key = key
        self.cRight = cRight
        self.cWrong = cWrong

    def showTitle(self):
        print("Cau hoi: {}\n".format(self.ques))

    def check(self, e):
        if (str(self.key).__eq__(str(e))):
            return True
        return False

    def right(self):
        self.cRight += 1

    def wrong(self):
        self.cWrong += 1

    def getAnswer(self):
        return self.key

    def getInformation(self):
        return repr(self) + str(self.cRight) + "\n" + str(self.cWrong)

    def __repr__(self):
        return "\n{}\n{}\n{}\n{}\n{}\n{}\n".format(self.ques, self.ans1,
                                                   self.ans2, self.ans3,
                                                   self.ans4, self.key)

    def __str__(self):
        return "\nCau hoi la({}/{}): {}\nA. {}\nB. {}\nC. {}\nD. {}\n".format(self.cRight, self.cWrong,
                                                                              self.ques, self.ans1, self.ans2, self.ans3, self.ans4)
