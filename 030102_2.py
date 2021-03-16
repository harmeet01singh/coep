# If two expressions are 35-11 and 12 x 2, will they form equation
import random as rd


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
    else:
        exp1,exp2,exp3 = '0','0','0'
        while((eval(exp1) == eval(exp2)) or (eval(exp2) == eval(exp3))):
            exp1 = '{} + {}'.format(rd.randint(0,25),rd.randint(0,25))
            exp2 = '{} - {}'.format(rd.randint(0,25),rd.randint(0,25))
            exp3 = '{} * {}'.format(rd.randint(1,10),rd.randint(1,10))
        #print(eval(exp1),eval(exp2),eval(exp3))
    return [exp1,exp2,exp3,not(key)]

def print_questions(exp=[]):
    rd.shuffle(exp)
    #print(exp)
    print('\n====================Question====================\nIf two expressions are {} and {}, will they form equation'.format(exp[0],exp[1]))
    return exp

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
    print(
        ''' \n====================Solution====================
            \nTo check equality of expressions we will check if both of them give same result or not'''
    )
    print(
        '''\nFirst expression {} = {}'''.format(exp[0],eval(exp[0]))
    )
    print(
        '''Second expression {} = {}\n'''.format(exp[1],eval(exp[1]))
    )
    if(eval(exp[0]) == eval(exp[1])):
        print('''Since both expression give same values i.e. {}, answer is True'''.format(eval(exp[0])))
    else:
        print('''Since both expressions give different values, the answer is False''')


def main():
    e0,e1,e2,key = generate_expression()
    #print([e0,e1,e2])
    exp = print_questions([e0,e1,e2])
    print_options()
    take_input(key)
    print_solution(exp)

main()