from coep_package.csv_module import putInCsv,database_fn
from csv_latex.latex import latex,to_frac
import random
def substraction():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(4,21)
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(0,35)
        if r3%2!= 0:
            r3=r3+1
        y=(r2-r3)
        x= y/r1

        ques="Solve for x, "+latex(str(r2)+" - "+str(r1)+"x = "+str(r3))
        op=[0,0,0,0]
        sq=[0,1,2,3]
        o1=((r3-r2)/r1)
        o2=(r2+r3-r1)
        o3=x
        o4=(r3+r2)*r1
        ra=random.randint(0,3)
        op[ra]=o3
        sq.remove(ra)
        op[sq[0]]=o1
        op[sq[1]]=o2
        op[sq[2]]=o4
        for i in range(1,5):
            print(i,". ",op[i-1])
        #print(" option 1 : ","%.3f" % o1,"\n","option 2 : ",o2,"\n","option 3 : ",o3,"\n","option 4 : ",o4,"\n")

        
        def sol():
            sol1 = "solution: \n"
            sol1=sol1 + latex(str(r2)+" - "+str(r1)+"x = "+str(r3))+"\n"
            sol1=sol1 + latex(str(r2)+" - "+str(r3)+" = "+str(r1)+"x")+" (taking constants in LHS and variable terms in RHS)"+"\n"
            sol1=sol1 + latex(str(r1)+"x = "+str(y))+"\n"
            sol1=sol1 + latex("x = ")+to_frac(str(y),str(r1))+"(dividing by "+str(r1)+" in both sides)"+"\n"
            sol1=sol1 + latex("x = "+str(x))+"\n"
            return sol1

        solution=sol()
        Question = ques
        Corr_op = op[ra]
        wrong_op1,wrong_op2,wrong_op3 = op[sq[0]],op[sq[1]],op[sq[2]]
        Solution = solution
        database_dict= database_fn("text",
        Answer_Type='1',
        Topic_Number='030203',
        Variation='v9',
        Question=Question,
        Correct_Answer_1=Corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        Solution_text=solution
        )
        return database_dict    

        value = int(input("Choose one option : "))

        if value==ra+1:
            print("\nright option")
            print(">--------------------------<")
            sol()
        elif value!=ra and value<5 and value>0:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        else :
            print("invalid choice")
        '''elif value==2:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nright option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")'''

def addition():

        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(4,21)
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(0,35)
        if r3%2!= 0:
            r3=r3+1
        y=(r3-r2)
        x= y/r1

        ques= "Solve for x, "+latex(str(r2)+" + "+str(r1)+"x = "+str(r3))


        op=[0,0,0,0]
        sq=[0,1,2,3]
        o1=((r3+r2)/r1)
        o2=r1+r2+r3
        o3=x
        o4=(r3+r2)*r1
        ra=random.randint(0,3)
        op[ra]=o3
        sq.remove(ra)
        op[sq[0]]=o1
        op[sq[1]]=o2
        op[sq[2]]=o4
        for i in range(1,5):
            print(i,". ",op[i-1])

        
        def sol():
            sol1="solution: \n"
            sol1=sol1+latex(str(r2)+" + "+str(r1)+"x = "+str(r3))+"\n"
            sol1=sol1+latex(str(r1)+"x = "+str(r3)+" - "+str(r2))+"(subtracting "+str(r2)+" from both sides)"+"\n"
            sol1=sol1+latex(str(r1)+"x = "+str(y))+"\n"
            sol1=sol1+latex("x = ")+to_frac(str(y),str(r1))+"(dividing by "+str(r1)+" on both sides)"+"\n"
            sol1=sol1+latex("x = "+str(x))
            return sol1
        
        solution=sol()
        Question = ques
        Corr_op = op[ra]
        wrong_op1,wrong_op2,wrong_op3 = op[sq[0]],op[sq[1]],op[sq[2]]
        Solution = solution
        database_dict= database_fn("text",
        Answer_Type='1',
        Topic_Number='030203',
        Variation='v10',
        Question=Question,
        Correct_Answer_1=Corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        Solution_text=solution
        )
        return database_dict
        print(" option 1 : ","%.3f" % o1,"\n","option 2 : ",int(o2),"\n","option 3 : ",float(o3),"\n","option 4 : ",int(o4),"\n")

        value = int(input("Choose one option : "))

        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nright option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")

def division():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r3=random.randint(21,41)
        if r3%2!= 0:
            r3=r3+1
        x=r1*r3

        ques= "Solve for x, "+latex("x /"+str(r3)+" = "+str(r1))


        o1=r3/r1
        o2=r3-r1
        o3=x
        o4=r1/r3
        
        op=[0,0,0,0]
        sq=[0,1,2,3]
        o1=r3/r1
        o2=r3-r1
        o3=x
        o4=r1/r3
        ra=random.randint(0,3)
        op[ra]=o3
        sq.remove(ra)
        op[sq[0]]=o1
        op[sq[1]]=o2
        op[sq[2]]=o4
        for i in range(1,5):
            print(i,". ",op[i-1])
        

        def sol():
            sol1="solution: \n"
            sol1=sol1+to_frac("x",str(r3))+latex(" = "+str(r1))
            sol1=sol1+latex("x = "+str(r3)+"*"+str(r1))+"(Multiplying by "+str(r3)+" on both sides)"
            sol1=sol1+latex("x = "+str(x))
            return sol1

        solution=sol()
        Question = ques
        Corr_op = op[ra]
        wrong_op1,wrong_op2,wrong_op3 = op[sq[0]],op[sq[1]],op[sq[2]]
        Solution = solution
        database_dict= database_fn("text",
        Answer_Type='1',
        Topic_Number='030203',
        Variation='v11',
        Question=Question,
        Correct_Answer_1=Corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        Solution_text=solution
        )
        return database_dict

        print(" option 1 : ",o1,"\n","option 2 : ",o2,"\n","option 3 : ",o3,"\n","option 4 : ","%.3f" % o4,"\n")

        value = int(input("Choose one option : "))    
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nright option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")

#----main-----
while 1:
    print(">------------NEW QUESTION-------------<\n")
    print("1.Addition")
    print("2.Substraction")
    print("3.Division")
    ch=int(input("choose the relation between constant and the variable term:"))
    if ch==1:
        putInCsv(
                '030203',
                20,
                addition,
                "v1_10"
                )
    elif ch==2:
        putInCsv(
                '030203',
                20,
                substraction,
                "v1_9"
                )
    elif ch==3:
        putInCsv(
                '030203',
                20,
                division,
                "v1_11"
                )
    else:
        print("invalid choice")


        
