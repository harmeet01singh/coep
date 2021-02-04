# For the given solution for x (/y) which of the following represents correct set of linear simultaneous equations

import numpy as np
import random as rd

coeff_list = []
opt = []
a1,b1,c1,a2,b2,c2,x,y = [0 for i in range(8)]
D = np.zeros((2,2))
Dx = np.zeros((2,2))
Dy = np.zeros((2,2))

def print_Questions(x=0,y=0):
    print(
        '''
        \nWhich of the following represents correct set of linear simultaneous equations for given solution
        \n(x = {:.2f}, y={:.2f})
        '''.format(x,y)
    )

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
            '''
                \n ({}x) + ({}y) = {} 
                \n ({}x) + ({}y) = {} 
            '''.format(oseq[i][0],oseq[i][1],oseq[i][2],oseq[i][3],oseq[i][4],oseq[i][5])
            )
    
    temp = list(zip(opt, oseq)) 
    rd.shuffle(temp) 
    opt, oseq = zip(*temp)

    #for debugging
    #print(oseq)

    print(
        '''
            \n1){}
            \n2){}
            \n3){}
            \n4){}
        '''.format(opt[0],opt[1],opt[2],opt[3])
    )
    return oseq

def print_solution():
    print(
        '''
            \nTo check the corectness of the solution \n
            \nsubstitute it into each equation pair and it should satisfiy both the equations

        '''
    )
    print(
        '''
            \n ({:.2f}x) + ({:.2f}y) = {:.2f} 
            \n ({:.2f}x) + ({:.2f}y) = {:.2f} 
        '''.format(a1,b1,c1,a2,b2,c2)
    )
    print(
        '''
            \nSubstituting values of x and y in equation 1
            \n({:.2f} x {:.2f}) + ({:.2f} x {:.2f}) = {:.2f}
            \n({:.2f}) + ({:.2f}) = {:.2f}
            \n {:.2f} = {:.2f}
        '''.format(a1,x,b1,y,c1,a1*x,b1*y,c1,(a1*x + b1*y),c1)
    )
    print(
        '''
            \nSubstituting values of x and y in equation 2
            \n({:.2f} x {:.2f}) + ({:.2f} x {:.2f}) = {:.2f}
            \n({:.2f}) + ({:.2f}) = {:.2f}
            \n {:.2f} = {:.2f}
        '''.format(a2,x,b2,y,c2,a2*x,b2*y,c2,(a2*x + b2*y),c2)
    )

def take_input(options,corr_op):
    ans = None
    while(ans == None or ans>4 or ans<1):
        ans = input('Enter your answer - \n')
        if(ans.isnumeric()):
            ans = int(ans)
        else:
            ans = None
            continue

    if(str(options[ans-1]) == str(corr_op)):
        print('Your answer is right')
    else:
        print('Wrong answer!!\n')
        print_solution()

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

    return [x,y]

def main_function():

    x,y = calculate_variables()
    print_Questions(x,y)
    options = print_Options()
    take_input(options,[a1,b1,c1,a2,b2,c2])

main_function()
