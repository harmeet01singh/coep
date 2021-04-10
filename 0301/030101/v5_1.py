#Balanced see-saw is an equation - True or False
from coep_package.csv_module import putInCsv,database_fn
import random
def main():
    eq=["Balanced see-saw","Simple pulley system","Analog weighing machine","Car-towing","A lever system"]
    nteq=["Placing books on bookshelf","Filling water in bucket","Spinning of ferris wheel"]
    car=random.choice([eq,nteq])
    cop=random.choice(car)
    print("Ques : ",cop," is an equation - True or False ? \n")
    ques=cop+" is an equation - True or False ? \n"
    print("1.True \n2.False")
    val=int(input("\nChoose a option : "))
    if cop in eq:
        Solution = cop+" will form a equation because in this situation the LHS will be equal to RHS"
        Corr_op = "True"
        wrong_op1="False"
    if cop in nteq:
        Solution = cop+" will not form a equation because in this situation the LHS will not be equal to RHS"
        Corr_op = "False"
        wrong_op1="True"
    Question = ques
    wrong_op2,wrong_op3 = "",""
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
    if val==1 and cop in eq:
        print("Right Option")
        print("Solution : ")
        print(cop," will form a equation because in this situation the LHS will be equal to RHS")
        #return
    if val==2 and cop in nteq:
        print("Right Option")
        print("Solution : ")
        print(cop," will not form a equation because in this situation the LHS will not be equal to RHS")
        #return
    elif val not in [1,2]:
        print("Invalid Choice")
    else:
        print("Wrong Option")
        if cop in eq:
            print("Solution : ")
            print(cop," will form a equation because in this situation the LHS will be equal to RHS")
            #return
        elif cop in nteq:
            print("Solution : ")
            print(cop," will not form a equation because in this situation the LHS will not be equal to RHS")
            #return
main()
putInCsv(
                '030101',
                20,
                main,
                "v5_1"
                )
