from Question import Question


def mySort(e):
    return e.cWrong


ques1 = Question("a", "a", "a", "a", "a", 1, 0, 10)
ques2 = Question("b", "b", "b", "b", "b", 1, 0, 3)
ques3 = Question("c", "c", "c", "c", "c", 1, 0, 5)

list = []
list.append(ques1)
list.append(ques2)
list.append(ques3)
list.sort(reverse=True, key=mySort)
print(list)
