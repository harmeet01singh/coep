# Find out the solution of the following equations using cramer's rule i.e. determinants
# 5x + 3y = -11
# 2x + 4y = -10

import numpy as np
import random as rd

coeff_list = []
a1,b1,c1,a2,b2,c2,x,y = [0 for i in range(8)]
D = np.zeros((2,2))
Dx = np.zeros((2,2))
Dy = np.zeros((2,2))

def print_Equations():
    print(
        '''
        Solve the following equations using Determinants method (cramer's rule)

        Equation 1 -> {0}x + {1}y = {2}
        Equation 2 -> {3}x + {4}y = {5} 
        '''.format(a1,b1,c1,a2,b2,c2)
    )

def print_Options(corr_op):
    interchanged_op = corr_op[::-1]
    corr_x = [corr_op[0],-corr_op[1]]
    corr_y = [-corr_op[0],corr_op[1]]
    opt = [corr_op,interchanged_op,corr_x,corr_y]
    rd.shuffle(opt)

    print(
        '''
            1)x: {:.2f}, y {:.2f}
            2)x: {:.2f}, y {:.2f}
            3)x: {:.2f}, y {:.2f}
            4)x: {:.2f}, y {:.2f}
        '''.format(opt[0][0],opt[0][1],opt[1][0],opt[1][1],opt[2][0],opt[2][1],opt[3][0],opt[3][1])
    )

    return opt

def show_answer():
    global x,y
    print('The correct answer is -')
    print('x: %.2f'%x)
    print('y: %.2f'%y)

def print_solution():
    global D,Dx,Dy
    detD = np.linalg.det(D)
    detDx = np.linalg.det(Dx)
    detDy = np.linalg.det(Dy)
    print(
        '''
            \nFirst calculate value of Determinant D with\n \n[a1  b1]\n[a2  b2]
            \nD = (a1 x b2) - (a2 x b1) \n = ({} x {}) - ({} x {}) \n = ({}) - ({}) \n = {:.2f} 
        '''.format(a1,b2,a2,b1,a1*b2,a2*b1,detD)
    )
    print(
        '''
            \nThen calculate value of Determinant Dx with\n \n[c1  b1]\n[c2  b2]
            \nDx = (c1 x b2) - (c2 x b1) \n = ({} x {}) - ({} x {}) \n = ({}) - ({}) \n = {:.2f} 
        '''.format(c1,b2,c2,b1,c1*b2,c2*b1,detDx)
    )
    print(
        '''
            \nFinally calculate value of Determinant Dy with\n \n[a1  c1]\n[a2  c2]
            \nDy = (a1 x c2) - (a2 x c1) \n = ({} x {}) - ({} x {}) \n = ({}) - ({}) \n = {:.2f} 
        '''.format(a1,c2,a2,c1,a1*c2,a2*c1,detDy)
    )
    print(
        '''
            \nDivide Dx with D to obtain x
            \n x = Dx / D = {:.2f}/{:.2f} = {:.2f} 
        '''.format(detDx,detD,detDx/detD)
    )
    print(
        '''
            \nDivide Dy with D to obtain y
            \n y = Dy / D = {:.2f}/{:.2f} = {:.2f} 
        '''.format(detDy,detD,detDy/detD)
    )
    show_answer()

def take_input(options,corr_op):
    ans = None
    while(ans == None or ans>4 or ans<1):
        ans = input('Enter your answer - \n')
        if(ans.isnumeric()):
            ans = int(ans)
        else:
            ans = None
            continue

    if(options[ans-1] == corr_op):
        print('Your answer is right')
    else:
        print('Wrong answer!!\n')
        print_solution()


def main_function():
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

    print_Equations()


    options = print_Options([x,y])
    
    take_input(options,[x,y])

main_function()
