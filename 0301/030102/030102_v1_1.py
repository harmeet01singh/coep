#which of thee followng is not a linear eq in one variable
##A. 33z+5
##
##B. 33(x+y)
##
##C. 33x+5
##
##D. 33y+5
from coep_package.csv_module import putInCsv,database_fn
from coep_package.latex import latex,to_frac
import random
def equi():
    global x1,y2,c3,opx,varx
    x1=random.randint(2,30)
    y2=random.randint(3,30)
    c3=random.randint(15,30)
    op=['+', '-', '*', '/']
    var=["a","b","c","x","y","z"]
    opx = random.choice(op)
    varx = random.choice(var)
    equi1 = latex(str(x1)+str(varx)+" "+str(opx)+" "+str(y2)+" = "+str(c3))
    return equi1

def num():
    ops = ['+', '-', '*', '/']
    num1 = random.randint(12,35)
    num2 = random.randint(1,12)
    operation = random.choice(ops)
    op=["<",">"]
    opr= random.choice(op)
    maths = eval(str(num1) + operation + str(num2))
    num1 = latex(str(num1)+" "+str(operation)+" "+str(num2)+" "+str(opr)+" "+str(maths))
    return num1

def notequi():
    r1=random.randint(2,30)
    r2=random.randint(15,30)
    op=["<",">"]
    operation = random.choice(op)
    notequi1=latex(str(r1)+"p"+" "+str(operation)+" "+str(r2))
    return notequi1

def line():
    r1=random.randint(2,30)
    r2=random.randint(0,3)
    op=["+","-","*","/"]
    line1=latex("x"+" "+str(op[r2])+" "+str(r1))
    return line1
def main():
        print("Ques. Which of the following is not an equation ?")
        ques="Which of the following is not an equation ?" 
        op=[0,0,0,0]
        sq=[0,1,2,3]
        wr=[line(),notequi(),num()]
        ra=random.randint(0,3)
        op[ra]=random.choice(wr)
        sq.remove(ra)
        op[sq[0]]=equi()
        op[sq[1]]=equi()
        op[sq[2]]=equi()
        for i in range(1,5):
            print(i,". ",op[i-1])

        def sol():
            sol="Solution: "+ latex(op[ra])
            sol=sol+"Equation can be defined as a mathematical statement \nin which two expressions are set equal to each other"
            return sol
##            print("In option => ",op[ra])
##            print("=> ",varx, " is the variable and ",x1,varx," is the variable term")
##            print("=> ",y2," and ",c3," are the constant terms")
        Solution = sol()
        Corr_op = op[ra]
        wrong_op1=op[sq[0]]
        Question = ques
        wrong_op2,wrong_op3 = op[sq[1]],op[sq[2]]
        database_dict= database_fn("text",
        Answer_Type='1',
        Topic_Number='030102',
        Variation='v1',
        Question=Question,
        ContributorMail="2018.hemkesh.raina@ves.ac.in",                           
        Correct_Answer_1=Corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        Solution_text=Solution
        )
        return database_dict    
        value = int(input("Choose one option : "))
        if value==ra+1:
            print("\nright option")
            print(">--------------------------<")
            sol()
        elif value!=ra+1 and value<5 and value>0:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        else :
            print("invalid choice")
main()

putInCsv(
                '030102',
                20,
                main,
                "v1_1",
                Remove_Duplicates = False
                )


