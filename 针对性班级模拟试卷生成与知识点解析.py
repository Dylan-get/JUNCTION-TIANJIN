import jieba 
import cv2
import numpy as np
class student():
    def __init__(self,sId):
        self.sId=sId

def ocr(imgPath):
    img=cv2.imread(imgPath)
    model=loding(ocr_model)
    text=model.predict(img)
    return text
def getNextQid(num):
    return int(num+10*np.random.rand())
class question:
    def __init__(self, Qid, subject, chapter,stem):
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
    def insert(self,question):
        self.questionlist.append(question)
def getfromSource(img=None,text=None):
    if img:
        questionDesp=ocr(img)
    if text:
        questionDesp=text
    return questionDesp
        
if __name__ == '__main__':
    studentList=[]
    for i in range(1,51,1):
        studentList.append(student(sId=i))
    questionList=[]
    subject='math'
    knowledgeNode=['三角函数','导数分析','线性回归','圆锥曲线']

    questionlist=[]
    myQuestionBook=questionBook(Sid=1,questionlist=questionList)
    #这样一个题目,将其插入错题集和习题集
    #questionDesp=getfromSource(img='./ti.png',text=None)#传入图片或文字
    questionDesp=getfromSource(img=None,text='线性回归分析')
    seg_list = jieba.cut(questionDesp, cut_all=True)
    qTMP=question(Qid=1,subject=subject,chapter='第一章',stem=seg_list)
    myQuestionBook.insert(qTMP)
    #数据
    knowledgeWeight=np.array([10,30,10,20])#各个知识点的总分
    knowledgeHardLevel=np.array([0.1,0.35,0.2,0.35])#各个知识点的难度
    knowledgePointAVG=np.array([6.0,15.5,7,13])#班级在各个知识点的得分

    #做残差
    deltx=knowledgeWeight-knowledgePointAVG 

    #推荐,若错的简单题多,会推荐更多简单题,在哪一个知识点失分多,则会推荐更多针对性的题目
    recommend=deltx/knowledgeHardLevel
    recommend=recommend/np.sum(recommend)
    print('-----知识点及相关推荐系数如下-----')
    print('本张试卷知识点:\t',knowledgeNode)
    print(recommend)
    num=10000
    for i,point in enumerate(recommend):
        print(knowledgeNode[i],'',point)
        #设置相关阈值
        if(point>0.3):

            print("-----推荐三道%s题-------"%(knowledgeNode[i]))
            for j in range(3):
                print('将题号为%d的关于%s知识点的题目加入模拟试卷'%(num,knowledgeNode[i]))
                num=getNextQid(num)
        elif(point>0.15):
            print("-----推荐两道%s题-------"%(knowledgeNode[i]))
            for j in range(2):
                print('将题号为%d的关于%s知识点的题目加入模拟试卷'%(num,knowledgeNode[i]))
                num=getNextQid(num)
        else:
            print("-----推荐一道%s题-------"%(knowledgeNode[i]))
            for j in range(1):
                print('将题号为%d的关于%s知识点的题目加入模拟试卷'%(num,knowledgeNode[i]))
                num=getNextQid(num)
    