# Is this value the solution to this equation? n+7=17, n=10, Yes/No

import random
from coep_package.csv import putInCsv,database_fn
from coep_package.latex import latex,to_frac

def addition():
    r1 = random.randint(2, 10)  # constants (7)
    r2 = random.choice(("a", "b", "c", "x", "y", "x"))  # variable (n)
    r3 = random.randint(10,30)  # rhs const (17)
 
    sol = r3 - r1                                       #correct ans (17-7 = 10)

    op = random.randint(sol - 1, sol+2)     #option displayed (9,12)

    if op == sol:
        ans = "Yes"         #actual answer (yes/no)
        wrong_ans = "No"
    else:
        ans = "No"
        wrong_ans = "Yes"

    eqn = latex(r2 + " + " + str(r1) + " = " + str(r3))    #(n+7=17)

    # Question
    ques = "For the equation " + str(eqn) + ", is the value of " + latex(r2 +  "=" + str(op)) + "? (Yes/No)"
    print(ques)
    


    def sol():
        sol1 = latex(r2 + " + " + str(r1) + " = " + str(r3)) + "\n"
        sol1 = sol1 + latex(r2 + " - " + str(r1) + " = " + str(r3) + " - " + str(r1) + "            (Subtracting " + str(r1) + " from both sides)" + "\n")
        sol1 = sol1 + latex(r2 + " = " + str(r3 - r1))
        return sol1

    print(sol())
    Solution = sol()
    Corr_op = ans
    wrong_op1=wrong_ans
    Question = ques
    wrong_op2,wrong_op3 = "",""
    database_dict= database_fn("text",
    Answer_Type='1',
    Topic_Number='030203',
    Variation='v1',
    Question=Question,
    ContributorMail="2019janhavi.mhatre@ves.ac.in",                           
    Correct_Answer_1=Corr_op,
    Wrong_Answer_1=wrong_op1,
    Wrong_Answer_2=wrong_op2,
    Wrong_Answer_3=wrong_op3,
    Solution_text=Solution
    )
    return database_dict

    value = str(input("Enter Yes/No: "))        #input answer

    if value.capitalize() == ans:
        print("\nRight option!")
        print(">---------------------------<")
        sol()

    else:
        print("\nWrong Option!")
        print(">---------------------------<")
        sol()

addition()
putInCsv(
                '030203',
                10,
                addition,
                "v2_1"
                )
