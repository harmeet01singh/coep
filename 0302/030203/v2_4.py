# Is this value the solution to this equation? n/6=2, n=12, Yes/No

import random
from coep_package.csv import putInCsv,database_fn
from coep_package.latex import latex,to_frac

def multiplication():
    r1 = random.randint(10,30)  # consts
    r2 = random.choice(("a", "b", "c", "x", "y", "x"))  # variable
    r3 = random.randint(2,10)  # rhs const

    sol = r3 * r1                                       #correct ans

    op = random.choice((sol,(sol*r3),(sol*r1),(sol+r3),(sol+r1)))     #option displayed

    if op == sol:
        ans = "Yes"                                     #actual answer (yes/no)
        wrong_ans = "No"
    else:
        ans = "No"
        wrong_ans = "Yes"

    eqn = latex(r2 + " / " + str(r1) + " = " + str(r3))

    # Question
    ques = "For the equation, " + latex(str(eqn)) + " is the value of " , latex(r2),  "=" , latex(op) , "? (Yes/No)"
    print(ques)

    def sol():
        sol1=latex(r2 + " / " + str(r1) + " = " + str(r3))+"\n"
        sol1=sol1+latex("( " + r2 + " / " + (str(r1)) +" )"+" * "+ str(r1) + " = " + str(r3)+" * "+str(r1)+"             (Multiplying " + str(r1) + " on both sides)")+"\n"
        sol1=sol1+latex(r2 + " = " + str(r3) + " * " + str(r1))+"\n"        
        sol1=sol1+latex(r2 + " = " + str(r3 * r1))
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
        Variation='v2',
        Question=Question,
        ContributorMail="2019rahul.nailwal@ves.ac.in",                           
        Correct_Answer_1=Corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        Solution_text=Solution
        )
    return database_dict
    value = str(input("Enter Yes/No: "))        #input answer

    
    
    if (value.capitalize() == ans) :
        print("\nRight answer!")
        print(">---------------------------<")
        sol()

    else:
        print("\nWrong answer!")
        print(">---------------------------<")
        sol()

multiplication()
putInCsv(
                '030203',
                10,
                multiplication,
                "v2_4"
                )
