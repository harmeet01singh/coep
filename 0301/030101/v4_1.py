#Q4
from coep_package.csv_module import putInCsv,database_fn
from coep_package.latex import latex
import random
def main():
    eq=["Two sides of an expression are unequal","A see-saw is unbalanced","A lever system is unbalanced","Two sides of a weighing scale are unequal","Length of two stright lines are unequal", "Area of two triangles are unequal", "Area of two squares are unequal", "Weight of two pouches are unequal"]
    #nteq=["Placing books on bookshelf","Filling water in bucket","Spinning of ferris wheel"]
    #car=random.choice([eq,nteq])
    cop=random.choice(eq)
    #print("Ques :If "+cop+", will it form an equation? - True or False ? \n")
    ques= cop+". Does the representation of this form an equation? State True or False. \n"
    #print("1.True \n2.False")
    #val=int(input("\nChoose a option : "))
    if cop in eq:
        Solution = "This representation will Falset form an equation because in this situation the Left Hand Side(LHS) will Falset be equal to Right Hand Side(RHS)."
        Corr_op = "False"
        wrong_op1="True"
    #if cop in nteq:
        #Solution = cop+" will Falset form a equation because in this situation the LHS will Falset be equal to RHS"
        #Corr_op = "False"
        #wrong_op1="True"
    Question = ques
    wrong_op2,wrong_op3 = "",""
    database_dict= database_fn("text",
    Answer_Type='1',
    Topic_Number='030101',
    Variation=4,
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
                "v4_1",
                Create_Textfile=True,
                Remove_Duplicates=True
                )