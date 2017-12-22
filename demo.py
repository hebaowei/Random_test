#!/usr/bin/python
#Filename:helloworld.py

import random
from fractions import Fraction
#getsymbol����������һ���������
def getoperators():
    operatorslist=('+','-','*','/','+','-')#����������ŵı���
    operators=random.choice(operatorslist)
    return operators


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

#getnumber��������������������operands���ַ�����value������ֵ����Fraction���ʾ
def getoperands(range):
    operandstype=random.randint(1,2)
    if operandstype==1:
        operands=random.randint(1,range)
        operandsvalue=Fraction(operands,1)
        operands=str(operands)
        #print operands
    else:
        operands1=random.randint(1,range)
        operands2=random.randint(1,range)
        if operands1<operands2:
            operands1,operands2=operands2,operands1
        if operands1==operands2:
            operandsvalue=Fraction(1,2)
            operands='(1/2)'
        else:
            operandsvalue=Fraction(operands2,operands1)
            operands=str(Fraction(operands2,operands1))
    return operands,operandsvalue

'''
#for i in range(1,11):
    #operators=getoperators()
    #print operators
for i in range(1,200):
    (operands,value)=getoperands(200)
    print operands,value
    '''
#getquestion�����������������������ַ�������ʽ����һ����Ŀ����fraction�෵�ش�
def getquestion(ran):#range�ǲ�������ȡֵ��Χ
    symbolnumber=random.randint(1,10)#������ɲ���������
    question=''
    questionstack=[]
    ans=0

    for i in range(1,symbolnumber+1):
        (op,va)=getoperands(ran)
        operands=op
        value=va
        operators=getoperators()
        question=question+operands+operators
        questionstack.append(value)
        questionstack.append(operators)
    (op,va)=getoperands(ran)
    operands=op
    value=va
    question=question+operands
    questionstack.append(value)
    #print question
    #print questionstack
    condition=0
    while len(questionstack)>1:#�Զ���Ĳ��漰���ŵ�����
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
    return question,ans

#ȷ����Ŀ�ĸ��������㷶Χ
questionnumber=int(raw_input('��������Ŀ�ĸ�����'))
ran=int(raw_input('���������㷶Χ��'))
questionlist=[]#��Ŀ����һ���б���
anslist=[]#�𰸴���һ���б���

while len(questionlist)<questionnumber:
    (question,ans)=getquestion(ran)
    cond=0
    for element in questionlist:
        if element==question:
            cond=1
    if cond==0:
        questionlist.append(question)
        anslist.append(ans)
print '��Ŀ�Ѿ�������ϣ�'
#print questionlist
correct_number=0
total_number=questionnumber
print '���δ��⿪ʼ����',questionnumber,'�⣬�ܷ�100�֣�����ʱ��45���ӣ�'
#time_start=time.time()
for i in range(0,questionnumber):
    print'��',i+1,'���ǣ�'
    print questionlist[i],'='
    #ans_user=raw_input('��������Ĵ𰸣�')
    print '���ǣ�',anslist[i]
    #time_end=time.time()
    #if time_end-time_start>10:
    #    print 'ʱ�䵽����ֹͣ���⣡'
    #    break
    ans_user=raw_input('��������Ĵ𰸣�')
    #if time_end-time_start>10:
    #    print 'ʱ�䵽����ֹͣ���⣡'
    #    break
    print '���Ĵ��ǣ�',ans_user
    if ans_user==str(anslist[i]):
        print'�ش���ȷ��'
        correct_number=correct_number+1
    else:
        print'�ش����'
#time_end=time.time()
correct_rate=correct_number*100.0/total_number
print '��������������εĵ÷�Ϊ��',round(correct_rate,1),'��'
