#030102 second variation
# If two expressions are 35-11 and 12 x 2, will they form equation
import random as rd
from coep_package.csv_module import database_fn,putInCsv
from coep_package.latex import latex

def generate_expression():
    key = rd.randint(0,1)
    #return equal expressions if key == 1 or unequal expressions if key == 0
    if (key):
        exp1,exp2,exp3 = '0','1','3'
        while((eval(exp1) != eval(exp2)) or (eval(exp2) != eval(exp3))):
            exp1 = '{} + {}'.format(rd.randint(0,25),rd.randint(0,25))
            exp2 = '{} - {}'.format(rd.randint(0,25),rd.randint(0,25))
            exp3 = '{} * {}'.format(rd.randint(1,10),rd.randint(1,10))
            #exp3 = '{} / {}'.format(rd.randint(1,10),rd.randint(1,10))
        #print(eval(exp1),eval(exp2),eval(exp3))
        key = True
    else:
        exp1,exp2,exp3 = '0','0','0'
        while((eval(exp1) == eval(exp2)) or (eval(exp2) == eval(exp3))):
            exp1 = '{} + {}'.format(rd.randint(0,25),rd.randint(0,25))
            exp2 = '{} - {}'.format(rd.randint(0,25),rd.randint(0,25))
            exp3 = '{} * {}'.format(rd.randint(1,10),rd.randint(1,10))
        #print(eval(exp1),eval(exp2),eval(exp3))
        key = False
    return [exp1,exp2,exp3,key]

def print_questions(exp=[]):
    rd.shuffle(exp)
    #print(exp)
    question = '\n <br> {} and {}, do they represent two sides of an equation ?'.format(latex(exp[0]),latex(exp[1]))
    print(question)
    return exp,question

def print_options():
    print('''\n1) True
             \n2) False''')

def take_input(corr_op):
    ans = None
    while(ans == None or ans>4 or ans<1):
        ans = input('\n--------------------------------\nEnter your answer - \n')
        if(ans.isnumeric()):
            ans = int(ans)
        else:
            ans = None
            continue

    if(ans-1 == corr_op):
        print('--------------------------------\nYour answer is right')
    else:
        print('--------------------------------\nWrong answer!!\n')


def print_solution(exp):
    section1='''<br>
            \nTo check equality of expressions we will check if both of them give same result or not'''
    print(section1)

    expression1 = '{} = {}'.format(exp[0],eval(exp[0]))
    section2 = '''\n <br>First expression {}'''.format(latex(expression1))
    print(section2)

    expression2 = '{} = {}'.format(exp[1],eval(exp[1]))
    section3 =  '''\n <br>Second expression {}'''.format(latex(expression2))
    print(section3)

    if(eval(exp[0]) == eval(exp[1])):
        section4='''\n<br>Since both expression give same values i.e. {}, answer is True'''.format(latex(eval(exp[0])))
        print(section4)
    else:
        section4 = '''\n<br>Since both expressions give different values, the answer is False'''
        print(section4)
    solution = section1 + section2 + section3 + section4
    return solution


def main():
    e0,e1,e2,corr_op = generate_expression()
    #print([e0,e1,e2])
    exp,Question = print_questions([e0,e1,e2])
    print_options()
    #take_input(not(corr_op))
    wrong_op = not(corr_op)
    Solution = print_solution(exp)

    database_dict= database_fn(
        Answer_Type='4',
        Topic_Number='030102',
        Variation='v8_1',
        Question=Question,
        Correct_Answer_1=corr_op,
        Wrong_Answer_1=wrong_op,
        Solution_text=Solution,
        ContributorMail="2018.rohan.pol@ves.ac.in"
    )
    return database_dict

putInCsv(
    Topic_Number='030102',
    Number_Of_Iterations=10,
    Main_Function=main,
    Filename=__file__
)