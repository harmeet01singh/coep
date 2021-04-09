import random as rd
from coep_package.latex import latex
from coep_package.csv import database_fn,putInCsv


def generate_expression():
    variable_list = ['a','b','c','m','n','p','q','x','y','z']
    key = rd.randint(0,len(variable_list) -1)
    variable = variable_list[key]
    objectList = ['pedas','jalebi','modak','ladoo','chocolate','toys','pencils','pens','lollipops','icecreams','samosa','mangoes','apples','minutes','hours','juice','oil','milk','honey','shampoo','sanitizer']
    key = rd.randint(0,len(objectList) -1)
    object = objectList[key]
    if(key < 13):
        question_key = 1    
    elif(key < 15):
        question_key = 2
    else:
        question_key = 3
    namelist = ['Reema','Seema','Rohan','Rahul','Arun','Sam']
    key = rd.randint(0,len(namelist) -1)
    name = namelist[key]
    var1 = rd.randint(2,15)
    var2 = rd.randint(2,15)
    return [var1,var2,object,name,variable,question_key]

#print(generate_xpression())
def print_expression(var1,var2,object,name,variable,key):
    if(key == 1):
        return 'Let {} have \'{}\' {} . {} distributed {} among {} students and each student got {} {}. Select correct operation to solve for \'{}\'.'.format(name,latex(variable),object,name,object,latex(var1),latex(var2),object,latex(variable))
    elif(key == 2):
        return 'Let {} have \'{}\' {} time to complete {} tasks. If {} decides to give equal time for each task, then each task has to done in {} {}. Select correct operation to solve for \'{}\'.'.format(name,latex(variable),object,latex(var1),name,latex(var2),object,latex(variable))
    elif(key == 3):
        return 'Let {} have \'{}\' litres of {}. {} fills {} in {} bottles of {} litre volume. Select correct operation to solve for \'{}\'. '.format(name,latex(variable),object,name,object,latex(var1),latex(var2),latex(variable))
def generate_options():
    wrong_option_list = [['+','+'],['+','-'],['-','+'],['-','-'],['\\times','\\times'],['\\times','\\div'],['\\div','\\div']]
    rd.shuffle(wrong_option_list)
    option_list = wrong_option_list[:3]
    option_list.insert(0,['\\div','\\times'])
    #rd.shuffle(option_list)
    return option_list

def print_option(option1,option2,option3,option4,var1,var2,variable):
    return latex(' ( {} {} {} ) {} {} = {} {} {} '.format(variable,option1[0],var1,option1[1],var1,var2,option1[1],var1)), latex(' ( {} {} {} ) {} {} = {} {} {} '.format(variable,option2[0],var1,option2[1],var1,var2,option2[1],var1)), latex( ' ( {} {} {} ) {} {} = {} {} {} '.format(variable,option3[0],var1,option3[1],var1,var2,option3[1],var1)), latex(' ( {} {} {} ) {} {} = {} {} {} '.format(variable,option4[0],var1,option4[1],var1,var2,option4[1],var1))
#def check_answer(ans_key):
#    inp = 0
#    while(inp == None or inp < 1 or inp > 4):
#        inp = input('\n---------------------------\nEnter your answer : ')
#
#        if(inp.isnumeric()):
#            inp = int(inp)
#        else:
#            inp = None
#    
#    if (inp == ans_key):
#        print('\n-----------Your answer is correct.')
#    else:
#        print('\n-----------Your answer is incorrect.')

def generate_solution(var1,var2,object,name,variable,key):
    if(key == 1):
        return '''
        {} had \'${}$\' {} which was distributed to ${}$ students. Each student recieves ${}$ {}.
        <br>We want to find \'${}$\'
        
        <br> Therefore we write ,
        <br> $( {} \\div {} )  =  {} $
        <br> $( {} \\div {} ) \\times {} = {} \\times {}$   ,by multiplying ${}$ on both sides '''.format(name,variable,object,var1,var2,object,variable,variable,var1,var2,variable,var1,var1,var2,var1,var1)
    elif(key == 2):
         return '''
        {} had \'${}$\' {} to perform ${}$ tasks. Each task has to be done in  ${}$ {}.
        <br> We want to find \'${}$\'
        
        <br> Therefore we write ,
        <br> $( {} \\div {} )  =  {} $
        <br> $( {} \\div {} ) \\times {} = {} \\times {}$   ,by multiplying ${}$ on both sides '''.format(name,variable,object,var1,var2,object,variable,variable,var1,var2,variable,var1,var1,var2,var1,var1)
    elif(key == 3):
        return '''
        {} had $\'{}\'$ litres of {} which will fill<br>  into ${}$ bottles of ${}$ litre volume.
       <br>  We want to find \'${}$\'
        
        <br> Therefore we write ,
        <br> $( {} \\div {} )  =  {} $
        <br> $( {} \\div {} ) \\times {} = {} \\times {}$   ,by multiplying ${}$ on both sides '''.format(name,variable,object,var1,var2,variable,variable,var1,var2,variable,var1,var1,var2,var1,var1)
def main():
    var1,var2,object,name,variable,key = generate_expression()
    print_expression(var1,var2,object,name,variable,key)
    option,ans_key = generate_options()
    print_option(option[0],option[1],option[2],option[3],var1,var2,variable)
    #print(ans_key)
    #check_answer(ans_key)
    generate_solution(var1,var2,object,name,variable,key)

#main()
def newMain():
    var1,var2,object,name,variable,key = generate_expression()
    question = print_expression(var1,var2,object,name,variable,key)
    option = generate_options()
    #print(option)
    c_ans,w_ans1, w_ans2,w_ans3 = print_option(option[0],option[1],option[2],option[3],var1,var2,variable)
    solution = generate_solution(var1,var2,object,name,variable,key)
   # print(solution)

    database_dict = database_fn( Answer_Type='text', Topic_Number='030202',Variation='v1',Question=question,Correct_Answer_1= c_ans,Wrong_Answer_1=w_ans1,Wrong_Answer_2=w_ans2,Wrong_Answer_3=w_ans2,ContributorMail='2019suraj.moolya@ves.ac.in',Solution_text=solution)
    return database_dict


putInCsv('030202',5,newMain,'v1_3')