# Find out the solution of the following equations using cramer's rule i.e. determinants
# 5x + 3y = -11
# 2x + 4y = -10

import numpy as np
import random as rd
import warnings
import csv
import sys
#from csv_module import store_csv
import store_csv

#CSV code
csvobj = store_csv.store_csv()

#from coep_csv import store_csv
#to ignore divide by zero warning
warnings.filterwarnings("ignore")

coeff_list = []
a1,b1,c1,a2,b2,c2,x,y = [0 for i in range(8)]
D = np.zeros((2,2))
Dx = np.zeros((2,2))
Dy = np.zeros((2,2))

def cal_xy(Dx,Dy,D):
    x = np.linalg.det(Dx)/np.linalg.det(D)
    y = np.linalg.det(Dy)/np.linalg.det(D)
    return [x,y]

def wrong_options(corr_op):
    wr_options = []
    #interchanged option
    if (corr_op[0] != corr_op[1]):
        wr_options.append(corr_op[::-1])

    #changing determinant arrangement and inverting them
    D = [[a1,b1],[a2,b2]]
    Dx = [[b1,c1],[b2,c2]]
    Dy = [[c1,a1],[c2,a2]]
    wrong_xy = cal_xy(Dx,Dy,D)
    wr_options.append(wrong_xy)

    if (wrong_xy[0] != wrong_xy[1]):
        wr_options.append(wrong_xy[::-1])

    #changing determinant arrangement second time and inverting them
    D = [[a1,b1],[a2,b2]]
    Dx = [[b1,c1],[c2,b2]]
    Dy = [[c1,a1],[a2,c2]]
    wrong_xy = cal_xy(Dx,Dy,D)
    wr_options.append(wrong_xy)

    if (wrong_xy[0] != wrong_xy[1]):
        wr_options.append(wrong_xy[::-1])

    wr_options = [tuple(li) for li in wr_options]
    conv_set = set(wr_options)
    while len(conv_set) < 4:
        wrong_x = rd.randint(-7,7)
        wrong_y = rd.randint(-7,7)
        conv_set.add((wrong_x,wrong_y))
    wr_options = [list(tup) for tup in wr_options]
    #print(len(wr_options))
    #print(wr_options)
    return wr_options


def print_Equations():
    Question =  '''\n====================Question====================
        \nSolve the following equations using Determinants method (cramer's rule)
        \nEquation 1 -> {0}x + {1}y = {2}
        \nEquation 2 -> {3}x + {4}y = {5}
        \n---------------------------------------------------------------------------------------------------'''.format(a1,b1,c1,a2,b2,c2)
    print(Question)
    return Question

def print_Options(corr_op):
    opt = wrong_options(corr_op)
    opt = rd.sample(opt,3)
    #print(opt)
    opt.append(corr_op)
    #print(opt)
    rd.shuffle(opt)
    #print(opt)
    for item in range(len(opt)):
        opt[item] = [int(i) for i in opt[item]]

    Final_options_str = '''\n1)x = {:2}, y = {:2}
            \n2)x = {:2}, y = {:2}
            \n3)x = {:2}, y = {:2}
            \n4)x = {:2}, y = {:2}'''.format(opt[0][0],opt[0][1],opt[1][0],opt[1][1],opt[2][0],opt[2][1],opt[3][0],opt[3][1])
    print(Final_options_str)
    print(opt,opt.index(corr_op))
    return [opt,Final_options_str,opt.index(corr_op)]

def print_solution(corr_op):
    global D,Dx,Dy
    detD = int(np.linalg.det(D))
    detDx = int(np.linalg.det(Dx))
    detDy = int(np.linalg.det(Dy))
    section1 = '''\n====================Solution====================
            \nFirst calculate value of Determinant D with
            \nD = 
            \n|a1  b1|\n|      |\n|a2  b2| 
            \n|{:3}  {:3}|\n|        |\n|{:3}  {:3}|
            \nD = (a1 x b2) - (a2 x b1) \n = ({} x {}) - ({} x {}) \n = ({}) - ({}) \n = {} 
        '''.format(a1,b1,a2,b2,a1,b2,a2,b1,int(a1*b2),int(a2*b1),detD)
    print(section1)
    section2 = '''
            \nThen calculate value of Determinant Dx with
            \nDx =
            \n|c1  b1|\n|      |\n|c2  b2|
            \n|{:3}  {:3}|\n|        |\n|{:3}  {:3}|
            \nDx = (c1 x b2) - (c2 x b1) \n = ({} x {}) - ({} x {}) \n = ({}) - ({}) \n = {} 
        '''.format(c1,b1,c2,b2,c1,b2,c2,b1,int(c1*b2),int(c2*b1),detDx)
    print(section2)
    section3 = '''
            \nFinally calculate value of Determinant Dy with
            \nDy =
            \n|a1  c1|\n|      |\n|a2  c2|
            \n|{:3}  {:3}|\n|        |\n|{:3}  {:3}|
            \nDy = (a1 x c2) - (a2 x c1) \n = ({} x {}) - ({} x {}) \n = ({}) - ({}) \n = {} 
        '''.format(a1,c1,a2,c2,a1,c2,a2,c1,int(a1*c2),int(a2*c1),detDy)
    print(section3)
    section4 = '''
            \nDivide Dx with D to obtain x
            \n x = Dx / D = ({})/({}) = {} 
        '''.format(detDx,detD,int(detDx/detD))
    print(section4)
    section5 = '''
            \nDivide Dy with D to obtain y
            \n y = Dy / D = ({})/({}) = {} 
        '''.format(detDy,detD,int(detDy/detD))
    print(section5)
    section6 = '''\n--------------------------------\nThe correct answer is -
            \nx: {}
            \ny: {}'''.format(int(corr_op[0]),int(corr_op[1]))
    print(section6)
    complete_solution = section1+section2+section3+section4+section5+section6
    return complete_solution

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
        print('\n--------------------------------\nYour answer is right')
    else:
        print('\n--------------------------------\nWrong answer!!\n')

def calculate_variables():
    global coeff_list
    global a1,b1,c1,a2,b2,c2,x,y
    global D,Dx,Dy

    coeff_list = [i for i in range(-50,50)]

    # to test if code fails on the condition D=0
    #a1,b1,c1 = 1,2,3
    #a2,b2,c2 = 2,4,6

    a1,b1,c1 = rd.choices(coeff_list,k=3)
    a2,b2,c2 = rd.choices(coeff_list,k=3)

    D = [[a1,b1],[a2,b2]]
    Dx = [[c1,b1],[c2,b2]]
    Dy = [[a1,c1],[a2,c2]]

    try:
        if(np.linalg.det(D) == 0): raise ValueError
        x,y = cal_xy(Dx,Dy,D)
    except ValueError:
        a2+=1
        b2+=2
        c2+=3
        D = [[a1,b1],[a2,b2]]
        Dx = [[c1,b1],[c2,b2]]
        Dy = [[a1,c1],[a2,c2]]
        x,y = cal_xy(Dx,Dy,D)

    return [x,y,D]

def main_function():
    Tn='0304060404'
    Vn='v5'
    x=0.0
    y=0.0
    D=0.0
    while((not(x.is_integer() and y.is_integer()) or (x==0 or y==0)) or int(np.linalg.det(D))==0.0):
        x,y,D = calculate_variables()
        #print(x,y,np.linalg.det(D))
    corr_op = [x,y]
    Question = print_Equations()
    options,options_str,corr_op_index = print_Options(corr_op)
    #take_input(options,corr_op)
    Solution = print_solution(corr_op)
    Corr_a= options.pop(corr_op_index)
    wrong_a1,wrong_a2,wrong_a3=options

    database_dict= csvobj.database_fn(
        Topic_Number=Tn,
        Variation=Vn,
        Question=Question,
        Correct_Answer_1=Corr_a,
        Wrong_Answer_1=wrong_a1,
        Wrong_Answer_2=wrong_a2,
        Wrong_Answer_3=wrong_a3,
        Solution_text=Solution
    )
    return database_dict

csvobj.putInCsv(
    NumberOfIterations=10,
    main_function=main_function,
    filename=__file__
)