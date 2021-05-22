import random


class ManagerQuestion:
    def __init__(self):
        self.count = 0
        self.list = []

    def getNumberQuestion(self):
        return self.count

    def addQuestion(self, ques):
        self.list.append(ques)
        self.count += 1

    def showQuestion(self):
        for e in self.list:
            print(e)

    def study(self):
        print("Welcome to my Study\n Please enter if you can continue")
        while True:
            ques = random.choice(self.list)
            print(ques)
            userChoose = str(input("enter a(1) b(2) c(3) or d(4): "))
            if (ques.check(userChoose)):
                print("right")
            else:
                print("wrong. right ans is {}".format(ques.getAnswer()))
            isExit = str(input("enter continute or c: "))
            if (isExit == 'c'):
                print("see yah")
                break
        save(self)

    def save(self):
        with open('studyed.txt', mode='w') as fo:
            for e in self.list:
                fo.write("{}\n".format(e))

    def __str__(self):
        return str(self.count)