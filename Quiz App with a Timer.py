#By Felin
import time

starttime=time.time()
correctanswer=0
print('Question No.1')                                                      
print('What is the national animal of india?')                                    
print('A.Tiger')                                                                      
print('B.Cheetah') 
print('C.Leopard')
print('D.Lion')
Correct='A'
Answer=input('Enter the option of the answer:')
endtime=time.time()
t=endtime-starttime
if t>=30:
    print('Time Up')
    print('RESULT')
    print('You scored',correctanswer,'out of 5')
    exit()
if Answer==Correct:
    correctanswer=correctanswer+1
print('Question No.2')
print('What is the national flower of India?')
print('A.Jasmine')
print('B.Lily')
print('C.Lotus')
print('D.Daffodil')
Correct='C'
Answer=input('Enter the option of the answer:')
endtime=time.time()
t=endtime-starttime
if t>=30:
    print('Time Up')
    print('RESULT')
    print('You scored',correctanswer,'out of 5')
    exit()
if Answer==Correct:
    correctanswer=correctanswer+1
print('Question No.3')
print('Who was the first president of India?')
print('A.Mahatma Gandhi')
print('B.Dr.Rajendra Prasad')
print('C.Dr.B.R. Ambedkar')
print('D.Jawaharlal Nehru')
Correct='B'
Answer=input('Enter the option of the answer:')
endtime=time.time()
t=endtime-starttime
if t>=30:
    print('Time Up')
    print('RESULT')
    print('You scored',correctanswer,'out of 5')
    exit()
if Answer==Correct:
    correctanswer=correctanswer+1
print('Question No.4')
print('Who was the first vice president of India?')
print('A.Indira Gandhi')
print('B.Dr.S.Radhakrishnan')
print('C.Dr.B.R.Ambedkar')
print('D.Morarji Desai')
Correct='B'
Answer=input('Enter the option of the answer:')
endtime=time.time()
t=endtime-starttime
if t>=30:
    print('Time Up')
    print('RESULT')
    print('You scored',correctanswer,'out of 5')
    exit()
if Answer==Correct:
    correctanswer=correctanswer+1
print('Question No.5')
print('Where was the first post office opened?')
print('A.Bombay')
print('B.Bangalore')
print('C.Jaipur')
print('D.Kolkata')
Correct='D'
Answer=input('Enter the option of the answer:')
endtime=time.time()
t=endtime-starttime
if t>=30:
    print('Time Up')
    print('RESULT')
    print('You scored',correctanswer,'out of 5')
    exit()
if Answer==Correct:
    correctanswer=correctanswer+1
print('Quiz is over')
print('RESULT')
print('You scored',correctanswer,'out of 5')

