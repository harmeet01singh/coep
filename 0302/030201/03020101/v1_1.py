#1. the sum of a certain number and 3 = x+3
#2. The difference obtained by subtracting 11 from another number , y-11
#3. The product of 15 and another number , 15*z
#4. a number divided by 24 , a/24 
from word2number import w2n
from num2words import num2words
#print(w2n.word_to_num("nine"))
import random
from coep_package.csv_module import putInCsv,database_fn
from coep_package.latex import latex,to_frac
def addition():
        r1=random.randint(3,10)
        #print(num2words(r1))
        r2=random.choice(("a","b","c","x","y","x"))
        r3=random.randint(3,20)
        ques="The sum of a cetrtain number and "+num2words(r1)+" is "+num2words(r3)+",represent in equation"
        sol=latex(r2+"+"+str(r1)+"="+str(r3))
        print(ques)
        #OPTION GENERATION
        op=[0,0,0,0]
        sq=[0,1,2,3]
        ra=random.randint(0,3)
        op[ra]=sol
        sq.remove(ra)
        op[sq[0]]=latex(str(str(r1)+str(r2))+"="+str(r3))
        op[sq[1]]=latex(str(str(r1)+str(r2)+"+"+str(r1))+"="+str(r3))
        op[sq[2]]=latex(str(str(r2)+"="+str(r1))+"-"+str(r3))
        for i in range(1,5):
            print(i,". ",op[i-1])
        def sol():
            sol1="Let's say certain no. will be :"+latex(str(r2))+"\n"
            sol1=sol1+"Sum means addition"+"\n"
            sol1=sol1+"Constant terms are : "+latex(str(r1))+" and "+latex(str(r3))+"\n"
            sol1=sol1+"solution would be : "+latex(str(r2)+"+"+str(r1)+"="+str(r3))+"\n"
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
addition()
putInCsv(
                '03020101',
                10,
                addition,
                "v1_1"
                )
