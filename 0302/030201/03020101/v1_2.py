# The difference obtained by subtracting 11 from certain number is 6, x - 11 = 6
from num2words import num2words
import random
from coep_package.csv import putInCsv,database_fn
from coep_package.latex import latex,to_frac
def subtraction():
    r1 = random.randint(20,50)
    r2 = random.randint(2,20)
    r3 =random.choice(("a","b","c","x","y","z"))
    ques="Ques. The difference obtained by subtracting "+num2words(r1)+" from certain number is "+num2words(r2)+",represent in equation "
    sol = latex(r3+" - "+str(r1)+" = "+str(r2))
    print(ques)
    #option generation
    op = [0,0,0,0]
    sq = [0,1,2,3]
    ra = random.randint(0,3)
    op[ra]=sol
    sq.remove(ra)
    op[sq[0]]=latex(str(str(r1)+"-"+str(r3)+"="+str(r2)))#11-x=6
    op[sq[1]]=latex(str(str(r2)+" - "+str(r3)+" = "+str(r1)))#6-x=11
    op[sq[2]]=latex(str(str(r3)+" - "+str(r2)+" = "+str(r1)))#x-6=11
    for i in range(1,5):
        print(i,". ",op[i-1])

    

    def sol():
        sol1="Let's say certain number is :"+latex(str(r3))+"\n"
        sol1=sol1+"Difference is subtraction"+"\n"
        sol1=sol1+"Constant terms are : "+latex(str(r1))+" and "+latex(str(r2))+"\n"
        sol1=sol1+"Solution would be : "+latex(str(r3+" - "+str(r1)+" = "+str(r2)))
        return sol1
    print(sol())
    Solution = sol()
    Corr_op = op[ra]
    wrong_op1=op[sq[0]]
    Question = ques
    wrong_op2,wrong_op3 = op[sq[1]],op[sq[2]]
    database_dict= database_fn("text",
    Answer_Type='1',
    Topic_Number='03020101',
    Variation='v2',
    Question=Question,
    ContributorMail="2019siddhi.mudras@ves.ac.in",                           
    Correct_Answer_1=Corr_op,
    Wrong_Answer_1=wrong_op1,
    Wrong_Answer_2=wrong_op2,
    Wrong_Answer_3=wrong_op3,
    Solution_text=Solution
    )
    return database_dict
    value = int(input("Choose one option :"))
    if value==ra+1 :
            print("\n Right Option")
            print(">--------------------------------<")
            sol()
    elif value !=ra+1 and value<5 and value > 0:
            print("\n Wrong Option")
            print(">--------------------------------<")
            sol()
    else:
            print("Invalid Choice")
subtraction()
putInCsv(
                '03020101',
                10,
                subtraction,
                "v1_2"
                )
