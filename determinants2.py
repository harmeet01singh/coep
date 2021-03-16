# For the given solution for x (/y) which of the following represents correct set of linear simultaneous equations

import numpy as np
import random as rd
import warnings
from coep_csv import store_csv
#to ignore divide by zero warning
warnings.filterwarnings("ignore")

#CSV code
csvobj = store_csv.store_csv()

coeff_list = []
opt = []
a1,b1,c1,a2,b2,c2,x,y = [0 for i in range(8)]
D = np.zeros((2,2))
Dx = np.zeros((2,2))
Dy = np.zeros((2,2))

def print_Questions(x=0,y=0):
    q='''
        \n====================Question====================
        \nWhich of the following represents correct set of linear simultaneous equations for given solution
        \n(x = {}, y = {})
        \n---------------------------------------------------------------------------------------------------'''.format(int(x),int(y))
    print(q)
    return q

def print_Options():
    global opt
    opt = [] 
    a = [a1,b1,c1,a2,b2,c2]
    oseq = [a.copy() for j in range(4)]
    #for debugging
    #print(oseq)
    for i in range(4):
        if i != 0:
            rd.shuffle(oseq[i])

        opt.append(
            '''\n ({}x) + ({}y) = {} 
               \n ({}x) + ({}y) = {}'''.format(oseq[i][0],oseq[i][1],oseq[i][2],oseq[i][3],oseq[i][4],oseq[i][5])
            )
    
    temp = list(zip(opt, oseq)) 
    rd.shuffle(temp) 
    opt, oseq = zip(*temp)

    #for debugging
    #print(oseq)

    print(
        ''' \n1){}
            \n2){}
            \n3){}
            \n4){}'''.format(opt[0],opt[1],opt[2],opt[3])
    )
    print(opt)
    return oseq

def print_solution():
    s1 = ''' \n====================Solution====================
            \nTo check the corectness of the solution
            \nsubstitute values of x and y into the addition of both the equations in the given option pair'''
    print(s1)
    s2 = ''' \n {}x + ({}y) = {} 
            \n {}x + ({}y) = {}'''.format(a1,b1,c1,a2,b2,c2)
    print(s2)
    s3 = '''\nAdding both the equations 
            \n     {}x + ({})y = {} 
            \n +   ({})x + ({})y = {}
            \n-------------------------------
            \n     ({})x + ({})y = {}'''.format(a1,b1,c1,a2,b2,c2,a1+a2,b1+b2,c1+c2)
    print(s3)
    s4 = '''\nSubstituting values of x and y in the above equation
            \nL.H.S = ({} x ({})) + ({} x ({}))
            \nL.H.S = {} + ({})
            \nL.H.S = {}
            \nL.H.S = R.H.S'''.format(a1+a2,int(x),b1+b2,int(y),int((a1+a2)*x),int((b1+b2)*y),int((a1+a2)*x + (b1+b2)*y))
    print(s4)
    return s1+s2+s3+s4

def take_input(options,corr_op):
    ans = None
    while(ans == None or ans>4 or ans<1):
        ans = input('\n--------------------------------\nEnter your answer - \n')
        if(ans.isnumeric()):
            ans = int(ans)
        else:
            ans = None
            continue

    if(str(options[ans-1]) == str(corr_op)):
        print('--------------------------------\nYour answer is right')
    else:
        print('--------------------------------\nWrong answer!!\n')

def calculate_variables():
    global coeff_list
    global a1,b1,c1,a2,b2,c2,x,y
    global D,Dx,Dy

    coeff_list = [i for i in range(-15,15)]

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
        x = np.linalg.det(Dx)/np.linalg.det(D)
        y = np.linalg.det(Dy)/np.linalg.det(D)
    except ValueError:
        a2+=1
        b2+=1
        c2+=1
        D = [[a1,b1],[a2,b2]]
        Dx = [[c1,b1],[c2,b2]]
        Dy = [[a1,c1],[a2,c2]]
        x = np.linalg.det(Dx)/np.linalg.det(D)
        y = np.linalg.det(Dy)/np.linalg.det(D)

    return [x,y,D]

def main_function():
    #not correct tn and vn only for test purposes
    Tn='0304060404'
    Vn='v5'
    x=0.0
    y=0.0
    D=0.0

    while((not(x.is_integer() and y.is_integer()) or (x==0 or y==0)) or int(np.linalg.det(D))==0.0):
        x,y,D = calculate_variables()
        #print(x,y,np.linalg.det(D))
    #x,y = calculate_variables()
    Question=print_Questions(x,y)
    options = print_Options()
    print(options)
    take_input(options,[a1,b1,c1,a2,b2,c2])
    Solution=print_solution()

    #database_dict= csvobj.database_fn(
    #    Topic_Number=Tn,
    #    Variation=Vn,
    #    Question=Question,
    #    Correct_Answer_1=Corr_a,
    #    Wrong_Answer_1=wrong_a1,
    #    Wrong_Answer_2=wrong_a2,
    #    Wrong_Answer_3=wrong_a3,
    #    Solution_text=Solution
    #)
    #return database_dict

main_function()
#csvobj.putInCsv(
#    NumberOfIterations=10,
#    main_function=main_function,
#    filename=__file__
#)
