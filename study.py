import os
from Manager import ManagerQuestion, Question
from tkinter import *
import random


def removeNewline(sources):
    # remove line 'empty'
    for element in sources:
        if element == '\n':
            sources.remove(element)
    # remove char '\n' if it exists
    for index in range(len(sources)):
        sources[index] = sources[index].replace('\n', '')
    return sources


def inputStudyed(path='studyed.txt'):
    try:
        file = open(path, mode='r', encoding='utf8')
        lines = file.readlines()
        lines = removeNewline(lines)

        countQues = int(len(lines) / 8)
        print("we have {} question.".format(countQues))

        questions = []
        for i in range(0, 8 * (countQues - 1) + 1, 8):
            ques = Question(ques=lines[i],
                            ans1=lines[i + 1],
                            ans2=lines[i + 2],
                            ans3=lines[i + 3],
                            ans4=lines[i + 4],
                            key=lines[i+5],
                            cRight=lines[i+6],
                            cWrong=lines[i+7])
            questions.append(ques)
        file.close()
    except Exception as e:
        print(str(e))
        return None
    return questions


def clickA():
    if int(ques.key) == 1:
        print('bingo')
    else:
        print('right answer is {}'.format(ques.getKey()))
    nextQues()


def clickB():
    if int(ques.key) == 2:
        print('bingo')
    else:
        print('right answer is {}'.format(ques.getKey()))
    nextQues()


def clickC():
    if int(ques.key) == 3:
        print('bingo')
    else:
        print('right answer is {}'.format(ques.getKey()))
    nextQues()


def clickD():
    if int(ques.key) == 4:
        print('bingo')
    else:
        print('right answer is {}'.format(ques.getKey()))
    nextQues()


def changeQuestion():
    LabelQues.config(text=ques.ques, wraplength=500, height=3, bg='#fcb353', padd)
    btnA.config(text=ques.ans1,
                bd=0, bg='#45ccde', justify=LEFT)
    btnB.config(text=ques.ans2,
                bd=0, bg='#45ccde')
    btnC.config(text=ques.ans3,
                bd=0, bg='#45ccde')
    btnD.config(text=ques.ans4,
                bd=0, bg='#45ccde')


def nextQues():
    questions.sort(key=lambda e: (
        int(e.cWrong), -int(e.cRight)), reverse=True)
    global ques
    ques = random.choice(questions[0: int(len(questions) / 3)])
    changeQuestion()


window = Tk()
# title game
window.title = "==>Welcome to my Study<=="
window.config(background='#fcb353')

frame = Frame(window, width=500, height=500, bg='#fcb353')
frame.pack()

questions = inputStudyed('./out.txt')
ques = questions[0]

LabelQues = Label(frame)
LabelQues.pack()
btnA = Button(frame, command=clickA)
btnA.pack(side=TOP)

btnB = Button(frame, command=clickB)
btnB.pack(side=TOP)

btnC = Button(frame, command=clickC)
btnC.pack(side=TOP)

btnD = Button(frame, command=clickD)
btnD.pack(side=TOP)
changeQuestion()

window.mainloop()
