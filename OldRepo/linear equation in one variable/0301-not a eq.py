#which of thee followng is not a linear eq in one variable
##A. 33z+5
##
##B. 33(x+y)
##
##C. 33x+5
##
##D. 33y+5
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
    return str(str(x1)+str(varx)+" "+str(opx)+" "+str(y2)+" = "+str(c3))
def num():
    ops = ['+', '-', '*', '/']
    num1 = random.randint(12,35)
    num2 = random.randint(1,12)
    operation = random.choice(ops)
    maths = eval(str(num1) + operation + str(num2))
    return str(str(num1)+" "+str(operation)+" "+str(num2)+" = "+str(maths))

def notequi():
    r1=random.randint(2,30)
    r2=random.randint(15,30)
    op=["<",">"]
    operation = random.choice(op)
    return str(str(r1)+"p"+" "+str(operation)+" "+str(r2))

def line():
    r1=random.randint(2,30)
    r2=random.randint(0,3)
    op=["+","-","*","/"]
    return str("x"+" "+str(op[r2])+" "+str(r1))

def main():
        print("Ques. Which of the following is an equation ?") 
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

        value = int(input("Choose one option : "))

        def sol():
            print("Solution: ",op[ra])
            print("Equation can be defined as a mathematical statement \nin which two expressions are set equal to each other")
##            print("In option => ",op[ra])
##            print("=> ",varx, " is the variable and ",x1,varx," is the variable term")
##            print("=> ",y2," and ",c3," are the constant terms")
            
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



