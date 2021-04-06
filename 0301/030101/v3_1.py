#Q3
from coep_package.csv import putInCsv,database_fn
import random
def main():
    eq=["two sides of an expression","two numbers","two objects","two things","the weight of potatoes kept on both sides of weighing scale"]
    #nteq=["Placing books on bookshelf","Filling water in bucket","Spinning of ferris wheel"]
    #car=random.choice([eq,nteq])
    cop=random.choice(eq)
    #print("Ques :If",cop,"are equal, will it form an equation? - True or False ? \n")
    ques="If "+cop+"are equal, will it form an equation? - True or False ? \n"
    #print("1.True \n2.False")
    #val=int(input("\nChoose a option : "))
    if cop in eq:
        Solution = "If "+cop+" are equal, it will form an equation because in this situation the LHS will be equal to RHS"
        Corr_op = "True"
        wrong_op1="False"
    #if cop in nteq:
        #Solution = cop+" will not form a equation because in this situation the LHS will not be equal to RHS"
        #Corr_op = "False"
        #wrong_op1="True"
    Question = ques
    wrong_op2,wrong_op3 = "",""
    database_dict= database_fn("text",
    Answer_Type='1',
    Topic_Number='030101',
    Variation=3,
    Question=Question,
    ContributorMail="2018.shubhra.jena@ves.ac.in",                           
    Correct_Answer_1=Corr_op,
    Wrong_Answer_1=wrong_op1,
    Wrong_Answer_2=wrong_op2,
    Wrong_Answer_3=wrong_op3,
    Solution_text=Solution
    )
    return database_dict
putInCsv(
                '030101',
                10,
                main,
                "v3_1"
                )