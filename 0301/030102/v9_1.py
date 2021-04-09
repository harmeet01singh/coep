#030102 variation 9
# Match the columns values with suitable operators
#A          B
#2+2,3+3    <
#2+3,7-2    =
#4*4,1-0    >

import random as rd
from tabulate import tabulate
from coep_package.csv import database_fn,putInCsv
from coep_package.latex import latex

def mathjaxTable(rows_list):
    row1 = 'a & {} & 1 & {}'.format(rows_list[0][1],rows_list[0][3])
    row2 = 'b & {} & 2 & {}'.format(rows_list[1][1],rows_list[1][3])
    row3 = 'c & {} & 3 & {}'.format(rows_list[2][1],rows_list[2][3])
    return f'''\\[
        \\begin{'{array}'}{'{|c|c|c|c|}'}
        \\hline
        \\text{'{ }'} & \\text{'{Operations}'} & \\text{'{ }'} & \\text{'{Relations}'} \\\\ 
        \\hline
        {row1}  \\\\
        \\hline
        {row2} \\\\
        \\hline
        {row3}  \\\\ 
        \\hline
        \\end{'{array}'}
        \\]
    '''


def map_exp_to_oprt(exp_tup):
    #print(exp_tup)
    e1,e2 = eval(exp_tup[0]),eval(exp_tup[1])
    if e1 == e2:
        return '1'
    elif e1 < e2:
        return '2'
    else:
        return '3'

def get_corr_op(rows_list):
    corr_op = {}
    for tup in rows_list:
        corr_op[tup[0]] = map_exp_to_oprt(tup[1].split(","))
    return corr_op

def format_table(rows):
    ops = ['=','<','>']
    rd.shuffle(ops)
    #print(rows)
    #print(ops[0],rows.get(ops[0]),ops[1],rows.get(ops[1]),ops[2],rows.get(ops[2]))
    rows_list = [['a',rows.get(ops[0]),'1','='],['b',rows.get(ops[1]),'2','<'],['c',rows.get(ops[2]),'3','>']]
    #table = tabulate(rows_list, headers=['','Operations','','Relations'],tablefmt="pretty")
    #print(rows_list)
    table = mathjaxTable(rows_list)
    corr_op = get_corr_op(rows_list)
    return table,corr_op

def print_questions(rows):
    statement = '''\n====================Question====================
                    \nStudy the each pair of expressions given in Expressions column and match them with appropriate operator present in Relations column
                    \n'''
    table,corr_op = format_table(rows)
    Question = statement+table
    print(Question)
    return Question,corr_op

def get_shuffled_list():
    colA = ['a','b','c']
    colB = ['1','2','3']
    temp = list(zip(colA,colB))
    rd.shuffle(temp)
    return dict(temp)

def format_dict(ans_dict):
    ans_str = ''
    #print(ans_dict)
    for letter in ans_dict:
        #print(letter,ans_dict)
        ans_str += '{}-{} '.format(letter,ans_dict[letter]) 
    return ans_str

def inSequence(dict_,seq):
    for o in seq:
        #for some reason comparing dictionaries normally didn't work in this if but worked at take_input() function so I had to compare them in string format
        if(str(o) == str(dict_)):
            #print(o,dict_)
            return True
        else:
            continue
    return False

def print_options(corr_op):
    optn = [corr_op]
    opt_str = []
    while(len(optn)<4):
        temp = get_shuffled_list()
        if(inSequence(temp,optn)):
            continue
        else:
            optn.append(temp.copy())
    rd.shuffle(optn)
    for d in optn:
        opt_str.append(format_dict(d))
    Options_str = '''\n1) {} \n2) {} \n3) {} \n4) {} '''.format(opt_str[0],opt_str[1],opt_str[2],opt_str[3])
    print(Options_str)
    return [Options_str,optn]

def take_input(options,corr_op):
    ans = None
    while(ans == None or ans>4 or ans<1):
        ans = input('\n--------------------------------\nEnter your answer - \n')
        if(ans.isnumeric()):
            ans = int(ans)
        else:
            ans = None
            continue
    if(options[ans-1] == corr_op):
        print('--------------------------------\nYour answer is right')
    else:
        print('--------------------------------\nWrong answer!!\n')

def print_eval_exp(oprt,exps):
    exp1,exp2 = exps.split(',')
    sol_sec='''\n$LHS = {} = {}$'''.format(exp1,eval(exp1))
    sol_sec+='''\n<br> $RHS = {} = {}$'''.format(exp2,eval(exp2))
    sol_sec+= '''\n<br> $LHS {} RHS$\n <br>'''.format(oprt)
    return sol_sec

def print_solution(rows,corr_op):
    sol = 'Evaluate each pair of equation and compare it by doing so you will get solution for each pair as follows-\n <br>'
    for oprt,exps in rows.items():
        sol+='In expressions - {} <br>'.format(latex(exps))
        sol+= print_eval_exp(oprt,exps)
    sol = sol + '''\n <br> Thus the correct option is - {}'''.format(format_dict(corr_op))
    print(sol)
    return sol

def generate_expressions():
    operators=['+','-','*']
    o = rd.choice(operators)
    a,b = rd.randint(0,15),rd.randint(0,15)
    return str(a)+o+str(b)

def generate_table():
    rows={}
    e1,e2 = '',''
    while(e1=='' or e2=='' or eval(e1)!=eval(e2) or e1==e2):
        e1,e2 = generate_expressions(),generate_expressions()
    rows['='] = e1+','+e2
    while(e1=='' or e2=='' or eval(e1)>=eval(e2) or e1==e2):
        e1,e2 = generate_expressions(),generate_expressions()
    rows['<'] = e1+','+e2
    while(e1=='' or e2=='' or eval(e1)<=eval(e2) or e1==e2):
        e1,e2 = generate_expressions(),generate_expressions()
    rows['>'] = e1+','+e2
    #print(rows)
    return rows

def get_formatted_options(optn):
    opt_list = []
    for dic in optn:
        opt_list.append(format_dict(dic))
    return opt_list

def main():
    rows = generate_table()
    Question,corr_op = print_questions(rows)
    options_str,optn = print_options(corr_op)
    Solution = print_solution(rows,corr_op)

    optn.remove(corr_op)
    correct_option_string = format_dict(corr_op)
    wop1,wop2,wop3 = get_formatted_options(optn)

    database_dict= database_fn(
        Answer_Type='1',
        Topic_Number='030102',
        Variation='v9',
        Question=Question,
        Correct_Answer_1=correct_option_string,
        Wrong_Answer_1=wop1,
        Wrong_Answer_2=wop2,
        Wrong_Answer_3=wop3,
        Solution_text=Solution
    )
    return database_dict

putInCsv(
    Topic_Number='030102',
    Number_Of_Iterations=15,
    Main_Function=main,
    Filename='v9_1'
)
