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

        print("Ques: Solve for x, ",r2," - ",r1,"x = ",r3)
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

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r2," - ",r1,"x = ",r3)
            print(r2," - ",r3," = ",r1,"x"," (taking constants in LHS and variable terms in RHS)")
            print(r1,"x = ",y)
            print("x = ",y,"/",r1,"(dividing by ",r1," in both sides)")
            print("x = ",x)
            
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

        print("Ques: Solve for x, ",r2," + ",r1,"x = ",r3)

        o1=((r3+r2)/r1)
        o2=r1+r2+r3
        o3=x
        o4=(r3+r2)*r1

        print(" option 1 : ","%.3f" % o1,"\n","option 2 : ",int(o2),"\n","option 3 : ",float(o3),"\n","option 4 : ",int(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r2," + ",r1,"x = ",r3)
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

def division():
        r1=random.randint(2,12)
        if r1%2!= 0:
            r1=r1+1
        r3=random.randint(21,41)
        if r3%2!= 0:
            r3=r3+1
        x=r1*r3

        print("Ques: Solve for x, ","x /",r3," = ",r1)


        o1=r3/r1
        o2=r3-r1
        o3=x
        o4=r1/r3

        print(" option 1 : ",o1,"\n","option 2 : ",o2,"\n","option 3 : ",o3,"\n","option 4 : ","%.3f" % o4,"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print("x /",r3," = ",r1)
            print("x = ",r3,"*",r1,"(Multiplying by ",r3," on both sides)")
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

#----main-----
while 1:
    print(">------------NEW QUESTION-------------<\n")
    print("1.Addition")
    print("2.Substraction")
    print("3.Division")
    ch=int(input("choose the relation between constant and the variable term:"))
    if ch==1:
        addition()
    elif ch==2:
        substraction()
    elif ch==3:
        division()
    else:
        print("invalid choice")


        
