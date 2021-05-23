from Question import Question
from ManagerQuestion import ManagerQuestion


def removeNewline(sources):
    for e in sources:
        if e == '\n':
            sources.remove(e)

    for i in range(len(sources)):
        sources[i] = sources[i].replace('\n', '')

    return sources


def inputAndHanding(path, pathSave='studyed.txt'):
    try:
        file = open(path, mode='r')
        lines = file.readlines()
        lines = removeNewline(lines)
        countQues = int(len(lines) / 5)
        input("we have {} question.".format(countQues))
        managerQuestion = ManagerQuestion()
        for i in range(0, 5 * (countQues - 1) + 1, 5):
            # remove 'x' and get right answer
            ans = 0
            ans = 1 if lines[i + 1][0] == 'x' else ans
            ans = 2 if lines[i + 2][0] == 'x' else ans
            ans = 3 if lines[i + 3][0] == 'x' else ans
            ans = 4 if lines[i + 4][0] == 'x' else ans
            lines[i + ans] = str(lines[i + ans])[1:]
            ques = Question(ques=lines[i],
                            ans1=lines[i + 1],
                            ans2=lines[i + 2],
                            ans3=lines[i + 3],
                            ans4=lines[i + 4],
                            key=ans)
            managerQuestion.addQuestion(ques)
        file.close()

        managerQuestion.save(pathSave)
    except Exception as e:
        print(str(e))

    return managerQuestion


def inputStudyed(path='studyed.txt'):
    try:
        file = open(path, mode='r')
        lines = file.readlines()
        lines = removeNewline(lines)

        countQues = int(len(lines) / 8)
        input("we have {} question.".format(countQues))
        managerQuestion = ManagerQuestion()
        for i in range(0, 8 * (countQues - 1) + 1, 8):
            # remove 'x' and get right answer
            ques = Question(ques=lines[i],
                            ans1=lines[i + 1],
                            ans2=lines[i + 2],
                            ans3=lines[i + 3],
                            ans4=lines[i + 4],
                            key=lines[i+5],
                            cRight=lines[i+6],
                            cWrong=lines[i+7])
            managerQuestion.addQuestion(ques)
        file.close()

        # managerQuestion.save(path)
    except Exception as e:
        print(str(e))

    return managerQuestion


if __name__ == "__main__":
    # manager = inputAndHanding('questionBasic.txt')
    manager = inputStudyed()
    manager.study()
    manager.save()
