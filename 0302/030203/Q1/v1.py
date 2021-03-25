#solve for x, 2x+5=11
from coep_package.csv import putInCsv,database_fn
from coep_package.latex import latex,to_frac
import random
def substraction():
    #x - 3 = 5,solve for x
    def hard():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(4,21)
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(0,35)
        if r3%2!= 0:
            r3=r3+1
        y=(r3+r2)
        x= y/r1

        ques="Solve for x, ",latex(str(r1)+"x - "+str(r2)+" = "+str(r3))
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
        def sol():
            sol=("solution: \n")
            sol=sol+(latex(str(r1)+"x - "+str(r2)+" = "+str(r3)))+"\n"
            sol=sol+str(latex(str(r1)+"x = "+str(r3)+" + "+str(r2))+" (adding "+str(r2)+" to both sides)")+"\n"
            sol=sol+str(latex(str(r1)+"x = "+str(y)))+"\n"
            sol=sol+str(latex("x = "+to_frac(str(y),str(r1)))+" (dividing by "+str(r1)+" in both sides)")+"\n"
            sol=sol+str(latex("x = "+str(x)))+"\n"
            return sol
        solution=sol()
        Question = ques
        Corr_op = op[ra]
        wrong_op1,wrong_op2,wrong_op3 = op[sq[0]],op[sq[1]],op[sq[2]]
        Solution = solution
        database_dict= database_fn("text",
        Answer_Type='1',
        Topic_Number='030203',
        Variation='v1',
        Question=Question,
        ContributorMail="2018.hemkesh.raina@ves.ac.in",                           
        Correct_Answer_1=Corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        Solution_text=solution
        )
        return database_dict
        #print(" option 1 : ","%.3f" % o1,"\n","option 2 : ",o2,"\n","option 3 : ",o3,"\n","option 4 : ",o4,"\n")

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
        
            
    def easy():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(4,21)
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(21,35)
        if r3%2!= 0:
            r3=r3+1
        r1=2
        y=(r3+r2)
        x= y/r1

        print("Ques: Solve for x, ",r1,"x - ",r2," = ",r3)

        o1=((r3-r2)/r1)
        o2=(r2+r3-r1)*(-1)
        o3=x
        o4=(r3+r2)*r1

        print(" option 1 : ",int(o1),"\n","option 2 : ",int(o2),"\n","option 3 : ",int(o3),"\n","option 4 : ",int(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x - ",r2," = ",r3)
            print(r1,"x = ",r3," + ",r2,"(adding ",r2," to both sides)")
            print(r1,"x = ",y)
            print("x = ",y,"/",r1,"(dividing by ",r1," on both sides)")
            print("x = ",x)
            
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

    print("1.easy")
    print("2.hard")
    ch=int(input("choose level:"))
    if ch==1:
        easy()
    elif ch==2:
        putInCsv(
                '030203',
                10,
                hard,
                "v1"
                )
    else:
        print("invalid choice")
def addition():
    #solve for x, 2x+5=11
    def hard():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(4,21)
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(21,35)
        if r3%2!= 0:
            r3=r3+1
        y=(r3-r2)
        x= y/r1

        print("Ques: Solve for x, ",r1,"x + ",r2," = ",r3)

        o1=((r3+r2)/r1)*(-1)
        o2=r1+r2+r3
        o3=x
        o4=(r3+r2)*r1

        print(" option 1 : ","%.3f" % o1,"\n","option 2 : ",int(o2),"\n","option 3 : ",float(o3),"\n","option 4 : ",int(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x + ",r2," = ",r3)
            print(r1,"x = ",r3," - ",r2,"(subtracting ",r2," from both sides)")
            print(r1,"x = ",y)
            print("x = ",y,"/",r1,"(dividing by ",r1," on both sides)")
            print("x = ",x)
            
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

    def easy():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(4,21)
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(21,35)
        if r3%2!= 0:
            r3=r3+1
        r1=2
        y=(r3-r2)
        x= y/r1

        print("Ques: Solve for x, ",r1,"x + ",r2," = ",r3)

        o1=((r3+r2)/r1)*(-1)
        o2=r1+r2+r3
        o3=x
        o4=(r3-r2)*r1

        print(" option 1 : ",int(o1),"\n","option 2 : ",int(o2),"\n","option 3 : ",int(o3),"\n","option 4 : ",int(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x + ",r2," = ",r3)
            print(r1,"x = ",r3," - ",r2,"(subtracting ",r2," from both sides)")
            print(r1,"x = ",y)
            print("x = ",y,"/",r1,"(dividing by ",r1," on both sides)")
            print("x = ",x)
            
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

    print("1.easy")
    print("2.hard")
    ch=int(input("choose level:"))
    if ch==1:
        easy()
    elif ch==2:
        hard()
    else:
        print("invalid choice")
def multiplication():
    #solve for x, 10 = 2x
    def easy():
        r1=random.randint(2,21)
        r2=random.randint(1,10)
        r3=r1*r2
        x=r3/r1
        print("Ques: Solve for x, ",r1,"x = ",r3)

        o1=r3*r1
        o2=r3-r1
        o3=x
        o4=r3+r1

        print(" option 1 : ",int(o1),"\n","option 2 : ",int(o2),"\n","option 3 : ",int(o3),"\n","option 4 : ",int(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x = ",r3)
            print("x = ",r3,"/",r1,"(dividing by ",r1," on both sides)")
            print("x = ",x)
            
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

    def hard():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r3=random.randint(21,41)
        if r3%2!= 0:
            r3=r3+1
        x=r3/r1

        print("Ques: Solve for x, ",r1,"x = ",r3)


        o1=r3*r1
        o2=r3-r1
        o3=x
        o4=r1/r3

        print(" option 1 : ",o1,"\n","option 2 : ",o2,"\n","option 3 : ",o3,"\n","option 4 : ",o4,"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x = ",r3)
            print("x = ",r3,"/",r1,"(dividing by ",r1," on both sides)")
            print("x = ",x)
            
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

    print("1.easy")
    print("2.hard")
    ch=int(input("choose level:"))
    if ch==1:
        easy()
    elif ch==2:
        hard()
    else:
        print("invalid choice")
def division():
    #solve for x, 15/x = 3
    def easy():
        r1=random.randint(2,21)
        r2=random.randint(1,10)
        r3=r1*r2
        x=r3/r1
        print("Ques: Solve for x, ",r3,"/x = ",r1)

        o1=r3*r1
        o2=r3-r1
        o3=x
        o4=r1/r3

        print(" option 1 : ",int(o1),"\n","option 2 : ",int(o2),"\n","option 3 : ",int(o3),"\n","option 4 : ","%.3f" % o4,"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r3,"/x = ",r1)
            print("x = ",r3,"/",r1,"(Multiplying by x on both sides)")
            print("x = ",x)
            
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

    def hard():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r3=random.randint(21,41)
        if r3%2!= 0:
            r3=r3+1
        x=r3/r1

        print("Ques: Solve for x, ",r3,"/x = ",r1)


        o1=r3*r1
        o2=r3-r1
        o3=x
        o4=r1/r3

        print(" option 1 : ",o1,"\n","option 2 : ",o2,"\n","option 3 : ",o3,"\n","option 4 : ","%.3f" % o4,"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r3,"/x = ",r1)
            print("x = ",r3,"/",r1,"(Multiplying by x on both sides)")
            print("x = ",x)
            
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

    print("1.easy")
    print("2.hard")
    ch=int(input("choose level:"))
    if ch==1:
        easy()
    elif ch==2:
        hard()
    else:
        print("invalid choice")
#----main-----
while 1:
    print(">------------NEW QUESTION-------------<\n")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    ch=int(input("choose the relation between constant and the variable term:"))
    if ch==1:
        addition()
    elif ch==2:
        substraction()
    elif ch==3:
        multiplication()
    elif ch==4:
        division()
    else:
        print("invalid choice")
