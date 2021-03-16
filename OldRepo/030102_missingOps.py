# If two expressions are 35-11 and 12 x 2, will they form equation
import random as rd

def generate_expression():
    oprt = ['*','+','-']
    exp1 = '{} {} {}'.format(rd.randint(0,15),rd.choice(oprt),rd.randint(0,15))
    exp2 = '{} {} {}'.format(rd.randint(0,15),rd.choice(oprt),rd.randint(0,15))
    return [exp1,exp2]


def generate_expression_set(mode):
    key = rd.choice([0,0,1])
    #return equal expressions if key == 1 or unequal expressions if key == 0
    if (key):
        exp1,exp2,exp3 = '0','1','3'
        while(eval(exp1) != eval(exp2)):
            exp1,exp2 = generate_expression()
        #print(eval(exp1),eval(exp2),eval(exp3))
        corr_sign='='
    else:
        exp1,exp2,exp3 = '0','0','0'
        while((eval(exp1) == eval(exp2)) or (eval(exp2) == eval(exp3))):
            exp1,exp2 = generate_expression()
        #print(eval(exp1),eval(exp2),eval(exp3))
        corr_sign = '<' if (eval(exp1)<eval(exp2)) else '>'
    return [exp1,exp2,corr_sign]

def print_questions(exp=[]):
    print('\n====================Question====================\nFill in the blank box\n ({}) {} ({})'.format(exp[0],chr(0x2610),exp[1]))
    return exp

def print_options():
    print('''\n1) =
             \n2) >
             \n3) <''')

def take_input(corr_sign):
    sign = ['=','>','<']
    ans = None
    while(ans == None or ans>3 or ans<1):
        ans = input('\n--------------------------------\nEnter your answer - \n')
        if(ans.isnumeric()):
            ans = int(ans)
        else:
            ans = None
            continue

    if(sign[ans-1] == corr_sign):
        print('--------------------------------\nYour answer is right')
    else:
        print('--------------------------------\nWrong answer!!\n')


def print_solution(exp,corr_sign):
    print(
        ''' \n====================Solution====================
            \nTo check equality of expressions we will check if both of them give same result or not'''
    )
    print(
        '''\nFirst expression {} = {}'''.format(exp[0],eval(exp[0]))
    )
    print(
        '''Second expression {} = {}'''.format(exp[1],eval(exp[1]))
    )
    print(
        '''First equation {} Second equation \n\nThus, \'{}\' is the appropriate sign'''.format(corr_sign,corr_sign)
    )


def main():
    modes = ['INTEGER','DECIMAL','FRACTIONAL']
    mode = input('How do you want to operate?\n 1)Integer\n 2)Decimal \n3)Fractional')
    e1,e2,corr_sign = generate_expression_set(modes[mode-1])
    #print([e0,e1,e2])
    exp = print_questions([e1,e2])
    print_options()
    take_input(corr_sign)
    print_solution(exp,corr_sign)

main()