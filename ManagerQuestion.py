import random


def mySort(e):
    a = int(e.cRight) - int(e.cWrong)
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
        # title game
        print("==>Welcome to my Study<==")
        print('Please enter if you can continue')

        while True:
            self.list.sort(key=mySort)
            # random choice in 1/3 question first in list
            # because they are question you is wrong
            ques = random.choice(self.list[0:int(self.count / 3)])
            print(ques)

            userChoose = str(
                input("enter 1 2 3 4 or cancel(c) offer(o): "))
            while (userChoose == ''
                   or not (userChoose == '1' or userChoose == '2'
                           or userChoose == '3' or userChoose == '4' or userChoose == 'c' or userChoose == 'o')):
                userChoose = str(input("enter again:"))

            if (userChoose == 'c'):
                print("see yah")
                break

            if (userChoose == 'o'):
                print('developing... coming soon')
                continue

            if (ques.check(userChoose)):
                print("congratulations")
                ques.right()
            else:
                print("you choose {} is not answer, right answer is {}".format(
                    userChoose, ques.getInfoAnswer()))
                input()
                ques.wrong()

    def save(self, path='studyed.txt'):
        with open(path, mode='w') as fo:
            for e in self.list:
                fo.write("{}\n".format(e.getInformation()))

    def __str__(self):
        return "managerQuestion have {} questions".format(str(self.count))
