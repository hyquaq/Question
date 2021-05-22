import random


def mySort(e):
    a = e.cRight - e.cWrong
    if (a < 0):
        return 0

    return a


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
            # ques = random.choice(self.list)
            self.list.sort(key=mySort)
            # print(self.list)
            ques = self.list[0]
            print(ques)

            userChoose = str(input("enter a(1) b(2) c(3) or d(4): "))
            print(userChoose)
            if (ques.check(userChoose)):
                print("right")
                ques.right()
            else:
                print("wrong. right ans is {}".format(ques.getAnswer()))
                ques.wrong()

            try:
                print("enter continute or cancel(c): ")
                isExit = input()
                if (isExit == 'c'):
                    print("see yah")
                    break
            except Exception as e:
                print('error' + str(e))
                pass

    def save(self):
        with open('studyed.txt', mode='w') as fo:
            for e in self.list:
                # print(e.getInformation())
                fo.write("{}\n".format(e.getInformation()))

    def __str__(self):
        return str(self.count)
