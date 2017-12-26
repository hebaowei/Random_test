import random
import time
from fractions import Fraction
#getsymbol����������һ���������
def getoperators():
    operatorslist=('+','-','*','/','+','-')
    operators=random.choice(operatorslist)
    if operators=='*':
        length=2
    elif operators=='/':
        length=2
    else:
        length=1
    return operators,length


#calculate���������ڼ�������ֵ����������
def calculate(n1,n2,op):
    if op=='+':
      ans=n1+n2
    elif op=='-':
      ans=n1-n2
    elif op=='*':
      ans=n1*n2
    else:
        if n2==0:
          print '��ĸ����Ϊ�㣡'
        else:
          ans=n1/n2
    return ans

#getnumber����������һ��������ʾ��������һ�����������������ʽ���ַ����͸�����
def getoperands(range):
    operandstype=random.randint(1,2)
    degree=0
    if operandstype==1:
        operands=random.randint(1,range)
        operandsvalue=Fraction(operands,1)
        operands=str(operands)
        degree=1
        #print operands
    else:
        operands1=random.randint(1,range)
        operands2=random.randint(1,range)
        degree=1.5
        if operands1<operands2:
            operands1,operands2=operands2,operands1
        if operands1==operands2:
            operandsvalue=Fraction(1,2)
            operands='(1/2)'
        else:
            operandsvalue=Fraction(operands2,operands1)
            operands=str(Fraction(operands2,operands1))
    return operands,operandsvalue,degree

#getquestion���������ַ�������ʽ����һ����Ŀ
def getquestion(ran):#range�ǲ�������ȡֵ��Χ
    symbolnumber=random.randint(1,5)
    question=''
    questionstack=[]
    ans=0
    length_ques=0

    for i in range(1,symbolnumber+1):
        (op,va,de)=getoperands(ran)
        operands=op
        value=va
        (operators,length)=getoperators()
        question=question+operands+operators
        questionstack.append(value)
        questionstack.append(operators)
        length_ques=length_ques+length+de
    (op,va,de)=getoperands(ran)
    operands=op
    value=va
    question=question+operands
    questionstack.append(value)
    length_ques=length_ques+de
    #print question
    #print questionstack
    condition=0
    while len(questionstack)>1:
        for i in range(0,len(questionstack)):
          if questionstack[i]=='*':
            questionstack[i-1]=questionstack[i-1]*questionstack[i+1]
            del questionstack[i]
            del questionstack[i]
            break
          elif questionstack[i]=='/':
            questionstack[i-1]=questionstack[i-1]/questionstack[i+1]
            del questionstack[i]
            del questionstack[i]
            break
          else:
            condition=1
        if condition==1:
            if len(questionstack)>1:
                questionstack[0]=calculate(questionstack[0],questionstack[2],questionstack[1])
                del questionstack[1]
                del questionstack[1]
        #print question
        #print questionstack
    else:
        ans=questionstack[0]       
    return question,ans,length_ques

#ȷ����Ŀ�ĸ��������㷶Χ
questionnumber=int(raw_input('��������Ŀ�ĸ�����'))
ran=int(raw_input('���������㷶Χ��'))
questionlist=[]#��Ŀ����һ���б���
anslist=[]#�𰸴���һ���б���
lengthlist=[]#Ȩ�ش���һ���б���
scorelist=[]#��������һ���б���
totalscore=0
questionfile=file('questionlist.txt','w')
#�����������Ŀ����������Ŀ�嵥��ÿһ�������ɵ��������������бȽϣ��ظ�������������
#�����ɵ���Ŀд���ļ��У����ڲ鿴���ӡ
while len(questionlist)<questionnumber:
    (question,ans,length)=getquestion(ran)
    cond=0
    for element in questionlist:
        if element==question:
            cond=1
    if cond==0:
        questionlist.append(question)
        anslist.append(ans)
        lengthlist.append(length)
        totalscore=totalscore+length
        questionfile.write(question+'\n')
questionfile.close()
print '��Ŀ�Ѿ�������ϣ�'
#����Ȩ�ط����ֵ
for i in range(0,len(lengthlist)):
    scorelist.append(round(lengthlist[i]*100/totalscore))         
grade=0
print '���δ��⿪ʼ����',questionnumber,'�⣬�ܷ�100�֣�����ʱ��45���ӣ�'
time_start=time.time()
for i in range(0,questionnumber):
    print'��',i+1,'���ǣ�'
    print questionlist[i],'='
    print'��ֵΪ',scorelist[i],'��'
    print '���ǣ�',anslist[i]
    ans_user=raw_input('��������Ĵ𰸣�')
    print '���Ĵ��ǣ�',ans_user
    if ans_user==str(anslist[i]):
        print'�ش���ȷ��'
        grade=grade+scorelist[i]
    else:
        print'�ش����'
time_end=time.time()
time_use=time_end-time_start
#��������һ����ĿȨ����ʱ�仨�ѵĹ�ϵk��Ĭ��Ϊ1
k=1
if time_use<totalscore*k:
    grade=grade
else:
    grade=round(totalscore*grade/time_use)
print '��������������εĵ÷�Ϊ��',grade,'��'

