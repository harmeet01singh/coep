#030102 second variation
# If two expressions are 35-11 and 12 x 2, will they form equation
import random as rd
from coep_package.csv_module import database_fn,putInCsv
from coep_package.latex import latex

def generate_expression(key):
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
    exps = [exp1,exp2,exp3]
    rd.shuffle(exps)
    return exps[0:2]

def print_questions():
    #print(exp)
    question = '\n <br> Which of the following pairs will not form a balanced equation ?'
    print(question)
    return question

def format_options(exp):
    return latex(exp[0]+","+exp[1])

def print_options(exp):
    op1 = format_options(exp)
    op2 = format_options(generate_expression(1))
    op3 = format_options(generate_expression(1))
    op4 = format_options(generate_expression(1))
    option_str = f'''\n1) {op1} \n2) {op2} \n3) {op3} \n4) {op4}'''
    print(option_str)
    return [op1,op2,op3,op4]

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
    section1='''<br> \nTo check equality of expressions we will check if both of them give same result or not'''
    print(section1)

    expression1 = '{} = {}'.format(exp[0],eval(exp[0]))
    section2 = '''\n <br>First expression {}'''.format(latex(expression1))
    print(section2)

    expression2 = '{} = {}'.format(exp[1],eval(exp[1]))
    section3 =  '''\n <br>Second expression {}'''.format(latex(expression2))
    print(section3)

    section4 = '''\n<br>Since both expressions give different values, they do not form a balanced equation'''
    if(eval(exp[0]) == eval(exp[1])):
        section4='''\n<br>Since both expression give same values i.e. {}, answer is True'''.format(latex(eval(exp[0])))
        print(section4)
    else:
        
        print(section4)
    solution = section1 + section2 + section3 + section4
    return solution


def main():
    e0,e1 = generate_expression(0)
    exp=[e0,e1]
    #print([e0,e1,e2])
    Question = print_questions()
    corr_op,wrong_op1,wrong_op2,wrong_op3 = print_options(exp)
    #take_input(not(corr_op))
    wrong_op = not(corr_op)
    Solution = print_solution(exp)

    database_dict= database_fn(
        Answer_Type='1',
        Topic_Number='030201',
        Variation='v3_1',
        Question=Question,
        Correct_Answer_1=corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        Solution_text=Solution,
        ContributorMail="2018.rohan.pol@ves.ac.in"
    )
    return database_dict

putInCsv(
    Topic_Number='030201',
    Number_Of_Iterations=10,
    Main_Function=main,
    Filename=__file__,
    Remove_Duplicates=False
)