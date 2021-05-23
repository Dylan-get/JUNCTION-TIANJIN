
from types import prepare_class
import numpy as np
import math
import os
import pandas as pd
class GradeClass():
    def __init__(self,classID,sIds,subIds,tIds,headId,friendLevel,cleanLevel,activeLevel):
        self.classID=classID
        self.sIds=sIds
        self.subIds=subIds
        self.tIds=tIds
        self.headId=headId
        self.friendLevel=friendLevel
        self.cleanLevel=cleanLevel
        self.activeLevel=activeLevel
    def getInfo(self):
        print("classID\t",self.classID)
        print("student number\t",len(self.sIds))
class Teacher():
    def __init__(self,tId,tAge,workAge,commi,subject,tdegree,hardValue):
        self.tId=tId   #职工号
        self.tAge=tAge #年龄
        self.workAge=workAge #工龄
        self.commi=commi     #党员
        self.subject=subject #教学科
        self.tdegree=tdegree #职称
        self.hardValue=hardValue #对每个章节难度的评估

    def getInfo(self):
        print("classID\t",self.classID)
        print("student number\t",len(self.studentIDs))

class Student():
    def __init__(self,classID,sId,cadres,sAge):
        self.classID=classID    #班级号
        self.sId=sId            #学生ID
        self.cadres=cadres      #学生职位
        self.sAge=sAge          #年龄
        tmp=np.random.rand(1)
        if tmp > 0.9:
            self.status=90+(2*np.random.normal(0,1))
            #比例1
        elif tmp>0.2:
            self.status=80+(2*np.random.normal(0,1))
            #比例7
        else:
            self.status=50+(2*np.random.normal(0,1))
            #比例2
    def getInfo(self):
        print("classID\t",self.classID)
        print("student ID\t",self.sId)
        print("student cadres\t",self.cadres)
        print("student sAge\t",self.sAge)
def create_hardValue():
    a = list()
    sum=0
    for i in range(40):
        b = np.random.rand()
        sum+=b
        a.append(b)
    a=np.array(a)
    a=a/sum
    print(a)
    print(np.sum(a))
    return a
#学科评估
class SubValue():
    def __init__(self,grade,chapterLevele):
        self.grade=grade   
        self.chapterLevele=chapterLevele
    def getInfo(self):
        print("classID\t",self.classID)
        print("student ID\t",self.sId)
    def getGrade(self):
        return self.grade
    def chapterLevele(self):
        return self.chapterLevele
def createChapterLevele(TeacherList):
    hards=np.zeros((12,40))
    for i,teacher in enumerate(TeacherList):
        hards[i]=teacher.hardValue
    return hards
def createStudents(classID=0,number=50,age=15):
    StudentList=[]
    sIds=np.arange(0, 50, 1)
    for i in sIds:
        sAge=np.round(age+(np.random.normal(0,1)))
        if i==14:
            cadres='monitor'
        elif i==27:
            cadres='secretary'
        elif i==31:
            cadres='learn'
        elif i==41:
            cadres='sport'
        else:
            cadres='common'
        tmp=Student(classID,i,cadres,sAge)
        StudentList.append(tmp)
    return StudentList,sIds
def createTeachers(number=12,age=35):
    TeacherList=[]
    tIds=np.arange(0, number, 1)
    #0-11
    subjects=["yuwen","shuxue","yingyu","wuli","huaxue","shengwu","zhengzhi","lishi","dili","tiyu","yinyue","xinxi"]
    for i in tIds:
        tAge=np.round(age+7*(np.random.normal(0,1)))
        workAge=(tAge-25)+3*(np.random.normal(0,1))
        if np.random.rand(1)>0.5:
            commi=1
        else :
            commi=0
        subject=subjects[i]
        tmp=np.random.rand(1)
        if tmp>0.8:
            tdegree='high'
        elif tmp>0.5:
            tdegree='medium'
        else:
            tdegree='low'
        hardValue=create_hardValue()
        tmp=Teacher(i,tAge=tAge,workAge=workAge,commi=commi,subject=subject,tdegree=tdegree,hardValue=hardValue)
        print(tmp.hardValue)
        TeacherList.append(tmp)
    return TeacherList,tIds
def createGrade(StudentList,sIds,subjects,process):
    
    grades=np.zeros((50,len(subjects),process))
    print(grades.shape)
    for i in sIds:
        print(StudentList[i].status)
        if StudentList[i].status>90:
            for id,sub in enumerate(subjects):
                for subprocess in range(process):
                    # print(i,id,subprocess)
                    if id==0:
                        grades[i][id][subprocess]=90+18*(np.random.random(1)-0.5)
                    elif id==1:
                        grades[i][id][subprocess]=92+16*(np.random.random(1)-0.5)
                    elif id==2:
                        grades[i][id][subprocess]=90+18*(np.random.random(1)-0.5)
                    elif id==3:
                        grades[i][id][subprocess]=90+16*(np.random.random(1)-0.5)
                    elif id==4:
                        grades[i][id][subprocess]=90+18*(np.random.random(1)-0.5)
                    elif id==5:
                        grades[i][id][subprocess]=90+10*(np.random.random(1)-0.5)
                    elif id==6:
                        grades[i][id][subprocess]=90+12*(np.random.random(1)-0.5)
                    elif id==7:
                        grades[i][id][subprocess]=90+14*(np.random.random(1)-0.5)
                    elif id==8:
                        grades[i][id][subprocess]=90+20*(np.random.random(1)-0.5)
                    elif id==9:
                        grades[i][id][subprocess]=80+14*(np.random.random(1)-0.5)
                    elif id==10:
                        grades[i][id][subprocess]=90+20*(np.random.random(1)-0.5)
                    else:
                        grades[i][id][subprocess]=90+20*(np.random.random(1)-0.5)
        elif StudentList[i].status>80:
            for id,sub in enumerate(subjects):
                for subprocess in range(process):
                    # print(i,id,subprocess)
                    if id==0:
                        grades[i][id][subprocess]=80+10*(np.random.random(1)-0.5)
                    elif id==1:
                        grades[i][id][subprocess]=80+20*(np.random.random(1)-0.5)
                    elif id==2:
                        grades[i][id][subprocess]=75+10*(np.random.random(1)-0.5)
                    elif id==3:
                        grades[i][id][subprocess]=70+10*(np.random.random(1)-0.5)
                    elif id==4:
                        grades[i][id][subprocess]=75+10*(np.random.random(1)-0.5)
                    elif id==5:
                        grades[i][id][subprocess]=80+10*(np.random.random(1)-0.5)
                    elif id==6:
                        grades[i][id][subprocess]=75+14*(np.random.random(1)-0.5)
                    elif id==7:
                        grades[i][id][subprocess]=80+10*(np.random.random(1)-0.5)
                    elif id==8:
                        grades[i][id][subprocess]=80+10*(np.random.random(1)-0.5)
                    elif id==9:
                        grades[i][id][subprocess]=85+30*(np.random.random(1)-0.5)
                    elif id==10:
                        grades[i][id][subprocess]=85+20*(np.random.random(1)-0.5)
                    else:
                        grades[i][id][subprocess]=85+20*(np.random.random(1)-0.5)
        else :
            for id,sub in enumerate(subjects):
                for subprocess in range(process):
                    # print(i,id,subprocess)
                    if id==0:
                        grades[i][id][subprocess]=65+30*(np.random.random(1)-0.5)
                    elif id==1:
                        grades[i][id][subprocess]=65+30*(np.random.random(1)-0.5)
                    elif id==2:
                        grades[i][id][subprocess]=70+20*(np.random.random(1)-0.5)
                    elif id==3:
                        grades[i][id][subprocess]=60+20*(np.random.random(1)-0.5)
                    elif id==4:
                        grades[i][id][subprocess]=68+20*(np.random.random(1)-0.5)
                    elif id==5:
                        grades[i][id][subprocess]=70+20*(np.random.random(1)-0.5)
                    elif id==6:
                        grades[i][id][subprocess]=60+20*(np.random.random(1)-0.5)
                    elif id==7:
                        grades[i][id][subprocess]=70+10*(np.random.random(1)-0.5)
                    elif id==8:
                        grades[i][id][subprocess]=70+10*(np.random.random(1)-0.5)
                    elif id==9:
                        grades[i][id][subprocess]=85+30*(np.random.random(1)-0.5)
                    elif id==10:
                        grades[i][id][subprocess]=85+20*(np.random.random(1)-0.5)
                    else:
                        grades[i][id][subprocess]=75+20*(np.random.random(1)-0.5)
        
    return grades.astype(np.int16)
def improve(weight,hards,processedHards):
    for id,hard in enumerate(processedHards):
        if id!=39:
            #设置阈值
            deltx=abs(processedHards[id+1]-processedHards[id])
            if deltx>1:
                print("---------------")
                print("可以优化第%d阶段任务安排"%(id+1))
                if processedHards[id]-processedHards[id+1]<0:
                    provex=100*(processedHards[id]-processedHards[id+1])/(2*processedHards[id])
                    provex=-provex
                    print("当前阶段任务较少，可以将下一阶段安排往前排,当前总任务应该增加%f"%provex,'%')
                    print("语文学科应该增加%f"%(weight[0]*provex/100),'%')
                    print('...')
                else :
                    provex=100*(processedHards[id]-processedHards[id+1])/(2*processedHards[id])
                    
                    print("当前阶段任务较多，可以将这一阶段安排往后排,当前总任务应该减少%f"%provex,'%')
                    print("语文学科应该减少%f"%(weight[0]*provex/100),'%')
                    print('...')
            else:
                pass
                # print("无需优化第%d阶段任务安排"%id)
def getStdentGrade(grades):
    if not os.path.exists('./grade'):
        os.mkdir('./grade')
    for i in range(50):
        tmp=pd.DataFrame(grades[i])
        tmp.to_csv('./grade/'+str(i)+".csv",index=False)
def getHard(hards):
    if not os.path.exists('./hard'):
        os.mkdir('./hard')
    tmp=pd.DataFrame(hards)
    tmp.to_csv("./hard/hard.csv",index=False)

if __name__ == '__main__':
    #九年级
    StudentList,sIds=createStudents(classID=0,number=50,age=15)
    TeacherList,tIds=createTeachers(number=12,age=35)
    subIds=["yuwen","shuxue","yingyu","wuli","huaxue","shengwu","zhengzhi","lishi","dili","tiyu","yinyue","xinxi"]
    headId=0 #教语文
    #研究的是比较不和谐的班级
    friendLevel=0.1+0.01*np.random.normal(0,1)
    cleanLevel=0.5+0.01*np.random.normal(0,1)
    activeLevel=friendLevel+0.01*np.random.normal(0,1)
    class0=GradeClass(classID=0,sIds=sIds,subIds=subIds,tIds=tIds,headId=headId,friendLevel=friendLevel,cleanLevel=cleanLevel,activeLevel=activeLevel)
    grades=createGrade(StudentList,sIds,subjects=subIds,process=40)
    print('------grades------')
    print(grades)
    print('------grades------')
    hards=createChapterLevele(TeacherList=TeacherList)
    print(hards.shape)
    print(hards)
    print('-------------')
    print(np.sum(hards,axis=0))
    print(np.sum(hards,axis=0)[33])
    print(np.sum(hards,axis=0)[34])
    # getHard(hards)
    #通过课时设置各科目权重，使得每一个时间段下 各科复合形成的任务繁重程度更加合理
    weight=100*np.array([0.2,0.2,0.2,0.075,0.05,0.05,0.05,0.05,0.05,0.025,0.025,0.025])
    processedHards=np.dot(weight,hards)
    

    print('-------------')

    print(processedHards)
    improve(weight,hards,processedHards)
    
    print(type(grades[0][1][1]))
    getStdentGrade(grades)
    print(grades[0][0][1])



    weightGrades=np.zeros((50,12,40))
    #通过前阶段的学习，同时对当前阶段的难度评估，推荐
    for i in range(50):
        weightGrades[i]=grades[i].astype("float32")*hards
    print(weightGrades[i].shape)
    print(weightGrades[i])
    x1=weightGrades.reshape(50,-1)
    print(x1.shape)
    xt=np.ones((50,1))*friendLevel
    print(xt)
    x1=np.hstack((x1,xt))
    x1=np.hstack((x1,np.ones((50,1))*cleanLevel))
    x1=np.hstack((x1,np.ones((50,1))*activeLevel))
    print(x1.shape)
    y=[]
    for student in StudentList:
        tmp=student.status
        y.append(tmp)
    

    y=np.array(y)
    print(y)
    # features=[x1,,班级的一些参数]










    
    # print(StudentList[1].getInfo())
    # grade1=np.random.rand(11,3) 
    # print(grade1)
    # s1=Student(classID=1,sId=1,cadres='banzhang',sAge=11,subGrade=grade1)
    # s1.getInfo()
    # SV=SubValue(grade0,chL1)
    # grade=SV.getGrade()
    # chengji=grade[id][xueke][zhangjie]
