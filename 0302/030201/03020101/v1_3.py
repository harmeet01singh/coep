#3. The product of 15 and another number is 45, 15*z=45
from num2words import num2words
import random
from coep_package.csv import putInCsv,database_fn
from coep_package.latex import latex,to_frac
def multiplication():
    r1 = random.randint(2,20)  #coeff
    r2=random.choice(("a","b","c","x","y","x"))  #variable
    r3=random.randint(2,30)  #rhs constant

    #Question
    ques = "Ques. The product of a certain number and " + num2words(r1)+" is " + num2words(r3) + ", represent in equation"

    solution = latex(str(r1)+ r2 +"="+ str(r3))

    print(ques)
    #Option

    op = [0,0,0,0]
    sq = [0,1,2,3]
    ra = random.randint(0,3)  #correct option
    op[ra] = solution
    sq.remove(ra)
    op[sq[0]] = latex(str(str(r3) + "*(" + str(r2) + "+" + str(r1) + ")" + "=" + str(r3)))  #addition 45*(z+15)+45
    op[sq[1]] = latex(str(str(r3) + "*(" + str(r1) + str(r2) + ")" +"=" + str(r3)) ) #subtraction 45*(15z)=45
    op[sq[2]] = latex(str(str(r1) + str(r2) + "+" + str(r2) + "=" + str(r3))) #product + addition 15z+z=45
    for i in range(1,5):
        print(i, ". " + op[i-1])

    def sol():
        sol = "Let's assume the certain number to be: " + latex(str(r2)) + "\n"
        sol = sol + "Product means multiplication" + "\n"
        sol = sol + "Hence, the certain number " + latex(str(r2)) + " is to be multiplied by " +  latex(str(r1)) + "\n"
        sol = sol + "Solution would be: " + latex(solution) + "\n"
        sol = sol + "Coefficient of " + latex(str(r2)) + " is: " + latex(str(r1)) + "\n"
        sol = sol + "Constant term is: " + latex(str(r3)) + "\n"
        return sol

    print(sol())
    Solution = sol()
    Corr_op = op[ra]
    wrong_op1=op[sq[0]]
    Question = ques
    wrong_op2,wrong_op3 = op[sq[1]],op[sq[2]]
    database_dict= database_fn("text",
    Answer_Type='1',
    Topic_Number='03020101',
    Variation='v3',
    Question=Question,
    ContributorMail="2019janhavi.mhatre@ves.ac.in",                           
    Correct_Answer_1=Corr_op,
    Wrong_Answer_1=wrong_op1,
    Wrong_Answer_2=wrong_op2,
    Wrong_Answer_3=wrong_op3,
    Solution_text=Solution
    )
    return database_dict

    value = int(input("Choose one option: "))
    if value == ra+1:
        print("\nRight option!")
        print(">---------------------------<")
        sol()
    elif value!= ra+1 and value<5 and value>0:
        print("\nWrong Option!")
        sol()
    else:
        print("Invalid Choice!")

multiplication()
putInCsv(
            '03020101',
            10,
            multiplication,
            "v1_3"
            )
