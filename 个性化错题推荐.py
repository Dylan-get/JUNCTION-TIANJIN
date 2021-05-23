from data import *
import difflib


class errorQuestion:
    def __init__(self, Qid, subject, chapter):
        self.Qid = Qid
        self.subject = subject
        self.chapter = chapter

    def getQid(self):
        return self.Qid

    def getSubject(self):
        return self.subject

    def getChapter(self):
        return self.chapter


class errorBook:
    def __init__(self, Sid, errorlist):
        self.Sid = Sid
        self.errorlist = errorlist

    def PrintBook(self):
        print(self.errorlist)


class question:
    def __init__(self, Qid, subject, chapter, stem):
        self.Qid = Qid
        self.subject = subject
        self.chapter = chapter
        self.stem = stem

    def getQid(self):
        return self.Qid

    def getSubject(self):
        return self.subject

    def getChapter(self):
        return self.chapter

    def getStem(self):
        return self.stem


class questionBook:
    def __init__(self, Sid, questionlist):
        self.Sid = Sid
        self.questionlist = questionlist

    def PrintBook(self):
        print(self.questionlist)


def CreateErrorBook(Sid, errorlist):
    yourBook = errorBook(Sid=Sid, errorlist=errorlist)
    return yourBook


def CreateQuestionBook(Sid, questionlist):  # list 是class的集合
    yourBook = questionBook(Sid=Sid, questionlist=questionlist)
    return yourBook


def PushQus(errorbook):
    for i in errorbook.errorlist:
        Recommend(errorbook.Sid, i)


def getStem(id, questionlist):
    str1 = ''
    for question in questionlist:
        if id == question.getQid():
            str1 = question.getStem()
            break
    return str1


def getQus(id, questionlist):
    for question in questionlist:
        if id == question.getQid():
            return question


def similarity(str1, str2):  # 计算相似度
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()


def analyse_get_else(id, questionlist, errorlist):
    id_questionlist = list()
    for question in questionlist:
        id_questionlist.append(question.getQid())

    if id not in id_questionlist:
        print('该习题集无该题')
    else:
        print('该习题集存在该题，类似错题有：\n')
        str1 = getStem(id, questionlist)

        for errorQuestion in errorlist:
            str2 = getStem(errorQuestion.getQid(), errorlist)
            num = similarity(str1, str2)
            # 设定阈值0.6
            if num >= 0.6:
                print(str2 + '\n')

    id_errorlist = list()
    for errorQuestion in errorlist:
        id_errorlist.append(errorQuestion.getQid())
    if id not in id_errorlist:
        errorlist.append(getQus(id, questionlist))


def Suggestion(SId, errorlist, Student):
    for i in errorlist:
        i = i.getQid()
        if 0 < i < 4 and Student.getValuebyId(SId) > 80 or 3 < i < 9 and Student.getValuebyId(SId) > 90:
            print("马虎了，继续加油哇,下次一定行！")
        elif 0 < i < 4 and 80 >= Student.getValuebyId(SId) > 60 or 3 < i < 9 and 90 >= Student.getValuebyId(
                SId) > 80 or 8 < i < 13 and 100 >= Student.getValuebyId(SId) > 90:
            print("你有能力做得出来，下次尽力做一定可以成功！")
        else:
            print("这类题可以先空着，先做自己会做的题目！")


# 依据不同档次水平的学生，通过判断分析学生所做错的题目，分别给出这类题目的建议，这里是根据题号，一般为前面的题目简单，后面的题目较难

if __name__ == '__main__':
    StudentList, sIds = createStudents(classID=0, number=50, age=15)

    q1 = question(0, '00', '00', 'yes,we are friend.')
    q2 = question(1, '01', '01', 'i am ok , thanks.')
    q3 = question(2, '10', '10', 'let us walk.')
    q4 = question(3, '11', '11', 'yes,we are family')
    questionlist = list()

    print('-----建立 -----')
    questionlist.append(q1)
    questionlist.append(q2)
    questionlist.append(q3)
    questionlist.append(q4)

    errorlist = list()
    analyse_get_else(0, questionlist, errorlist)
    print(errorlist)
    analyse_get_else(3, questionlist, errorlist)
    print(errorlist)

    Suggestion(0, errorlist, StudentList[0])
