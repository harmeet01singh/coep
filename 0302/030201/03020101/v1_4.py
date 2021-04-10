#Quotient of a certain dividend having 25 as a divisor is 6, a/24=6
#4. a number divided by 24 , a/24 equals 6,a/24=6

from num2words import num2words
import random
from coep_package.csv import putInCsv,database_fn
from coep_package.latex import latex,to_frac
def division():
        r1=random.randint(2,30)#coeffiecient
        r2=random.choice(("a","b","c","x","y","x"))#variable
        r3=random.randint(1,10)
        ques="Quotient of a certain dividend having "+num2words(r1)+" as a divisor, is "+num2words(r3)+"\n"
        ques=ques+"Represent the following in the form of an equation : "
        sol=latex(r2+"/"+str(r1)+"="+str(r3))
        print(ques)
        #OPTION GENERATION
        op=[0,0,0,0]
        sq=[0,1,2,3]
        ra=random.randint(0,3) #correct option
        op[ra]=sol
        sq.remove(ra)
        op[sq[0]]=latex(str(str(r2)+"/"+str(r3))+"="+str(r1))
        op[sq[1]]=latex(str(str(r1)+"/"+str(r3))+"="+str(r2))
        op[sq[2]]=latex(str(str(r1)+"/"+str(r2))+"="+str(r3))

        
        for i in range(1,5):
            print(i,". ",op[i-1])

        def sol():
            sol1="Let's say certain no. will be : "+latex(str(r2))+"\n"
            sol1=sol1+"For finding the Dividend, we need to perform division operation"+"\n"
            sol1=sol1+"Divisor : "+latex(str(r1))+" and Quotient : "+latex(str(r3))+"\n"
            sol1=sol1+"Solution would be : "+latex(str(r2)+" / "+str(r1)+" = "+str(r3))
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
        ContributorMail="2019rahul.nailwal@ves.ac.in",                           
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
division()
putInCsv(
                '03020101',
                10,
                division,
                "v1_4"
                )

