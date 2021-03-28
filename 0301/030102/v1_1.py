#Which of the following is an equation?
#x+5
#7x
#2y+3=11
#2p<1
from coep_package.csv import putInCsv,database_fn
from coep_package.latex import latex,to_frac
import random
def line():
    r1=random.randint(2,30)
    r2=random.randint(0,3)
    op=["+","-","*","/"]
    line1=latex("x"+" "+str(op[r2])+" "+str(r1))
    return line1

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

def main():
        print("Ques. Which of the following is an equation ?") 
        ques="Which of the following is an equation ?"
        op=[0,0,0,0]
        sq=[0,1,2,3]
        ra=random.randint(0,3)
        op[ra]=equi()
        sq.remove(ra)
        op[sq[0]]=notequi()
        op[sq[1]]=num()
        op[sq[2]]=line()
        for i in range(1,5):
            print(i,". ",op[i-1])
        def sol():
            sol= "Solution:"
            sol=sol+"Equation can be defined as a mathematical statement \nin which two expressions are set equal to each other"
            sol=sol+"In option => "+op[ra]
            sol=sol+"=> "+latex(str(varx))+" is the variable and "+latex(str(x1))+latex(str(varx))+" is the variable term"
            sol=sol+"=> "+latex(str(y2))+" and "+latex(str(c3))+" are the constant terms"
            return sol
        Solution = sol()
        Corr_op = op[ra]
        wrong_op1=op[sq[0]]
        Question = ques
        wrong_op2,wrong_op3 = op[sq[1]],op[sq[2]]
        database_dict= database_fn("text",
        Answer_Type='1',
        Topic_Number='030101',
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
                "v1_1"
                )
