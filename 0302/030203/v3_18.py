from os import truncate
import random
from IndianNameGenerator import *
from coep_package.latex import latex
from coep_package.csv_module import database_fn, putInCsv

p1 = random.randint(2,20) #p1 is the no. of years
p2 = random.randint(2,5) #p2 is no. of times Kanwar was elder.
p3 = random.randint(1,20) #p3 is no. of years before

def getwronganswers():
    c = round(((p2*p3)+p1)/(p2+1)) #option 1
    e = round(((p2*p3)-p1)/(p2+1))#option 3
    f = round(((p2*p3)-p1)/(p2-1)) #option 4
    options= [c,e,f]
    return random.shuffle(options)




#     print(f'After {p1} years, {n1}  shall be {p3}  times as old as he was {p3} years ago. Find {mapping[name]} present age. ')


def main_function():
    n1 = maleMarathi()
    n2 = femaleMarathi()
    mapping = {n1: 'his', n2: 'her'}
    name = random.choice([n2, n1])
    
    p1 = random.randint(1,20) #p1 is the no. of years
    p2 = random.randint(2,5) #p2 is no. of times Kanwar was elder.
    p3 = random.randint(1,20) #p3 is no. of years before
    c = round(((p2*p3)+p1)/(p2+1)) #option 1
    e = round(((p2*p3)-p1)/(p2+1))#option 3
    f = round(((p2*p3)-p1)/(p2-1)) #option 4
  
#ranges for the variables  
    p1 = random.randint(1,20) #p1 is the no. of years
    p2 = random.randint(2,5) #p2 is no. of times Kanwar was elder.
    p3 = random.randint(1,20) #p3 is no. of years before

    while (p2*p3+p1)%(p2-1):
        p1 = random.randint(1,20) #p1 is the no. of years
        p2 = random.randint(2,10) #p2 is no. of times Kanwar was elder.
        p3 = random.randint(1,20) #p3 is no. of years before
   
    
    
    def getquestion():
        ques="After "+latex(str(p1))+" years, "+ str(n1)+"  shall be "+latex(str(p3))+"  times as old as he was "+latex(str(p3))+" years ago. Find "+ mapping[name]+" present age. "
        return ques

    question= getquestion()
    corr=round(((p2*p3)+p1)/(p2-1))
    correctanswer1= corr
    wrong_answer_1, wrong_answer_2, wrong_answer_3= [c,e,f]
    
    def getsol():
        sol= 'Let '+ str(n1) + '\'s' + ' current age be ' + latex('x') + '.<br>' 
        sol = sol + 'Hence, ' + latex('x') + '+' + latex(str(p1)) + ' = ' + latex(str(p2)) + '*' + latex(str('(x-'+ str(p3)+')\n')) + '<br>' 
        sol = sol + latex('x') + '+' + latex(str(p1)) +' = '+ latex(str(p2)) + latex('x') + '-' + latex(str(p2*p3)) + ".<br>" 
        sol = sol + latex(str((p2-1)))+ latex('x') +' = ' + latex(str((p2*p3)+p1)) +'\n<br>' 
        sol = sol + latex('x') + ' = ' + latex(str(((p2*p3)+p1)/(p2-1)))+ '\n<br>'
        sol = sol + 'Hence, ' + str(n1)+ ' is ' + latex(str(round(((p2*p3)+p1)/(p2-1)))) + ' years old presently.'
        return sol
    # elif choice in [1,2,3,4]:
    #     print('Your answer is incorrect!')
    #     print('The correct answer is option', corr)
    #     print('\n-------- SOLUTION----------\n')
    #     sol()
    # else:
    #     print("Invalid input")


    
    database_dict = database_fn(Answer_Type= 'text',
                                Topic_Number= '0302',
                                Variation= 18,
                                Question=question,
                                Correct_Answer_1=correctanswer1,
                                Wrong_Answer_1=wrong_answer_1,
                                Wrong_Answer_2=wrong_answer_2,
                                Wrong_Answer_3=wrong_answer_3,
                                ContributorMail= '2019aarushi.sharma@ves.ac.in',
                                Solution_text= getsol()
                                )
    return database_dict
    

putInCsv('030203',10, main_function, 'v18_1', Remove_Duplicates=True, Create_Textfile=True)
