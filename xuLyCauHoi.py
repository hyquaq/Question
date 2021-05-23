import os
from Manager import ManagerQuestion, Question


# remove 'empty row' and '\n'
def removeNewline(sources):
    # remove line 'empty'
    for element in sources:
        if element == '\n':
            sources.remove(element)
    # remove char '\n' if it exists
    for index in range(len(sources)):
        sources[index] = sources[index].replace('\n', '')
    return sources


# read data form file, handing
# return ManagerQuestion
def inputAndHanding(path, pathSave=''):
    try:
        file = open(path, mode='r')
        lines = file.readlines()
        lines = removeNewline(lines)
        countQues = int(len(lines) / 5)
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
    except Exception as e:
        print(str(e))
        return None
    # after done
    return managerQuestion


if __name__ == '__main__':
    path = input("enter file name: ")
    if os.path.isfile(path):
        manager = inputAndHanding(path)
        print('i have {} question'.format(manager.count))
        print("i'm storing...")
        if (manager.save()):
            print('success. Now you can run "study.py"')
        else:
            print('fail. try again.')
    else:
        print("sorry i can't found file. please run again.")
