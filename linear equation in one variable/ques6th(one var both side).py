import random

def addition():
    #solve for x, 4x+4=5x+2
    def easy():
        r1=random.randint(2,11)#coffi of LHS var
        if r1%2!= 0:
            r1=r1+1
        r2=r1+2
        '''r2=random.randint(2,11)#coffi of RHS var
        if r2%2!= 0:
            r2=r2+1'''
        r3=random.randint(2,21)
        if r3%2!= 0:
            r3=r3+1
        r4=random.randint(2,21)
        if r4%2!= 0:
            r4=r4+1
        if r3==r4:
            r3=r3+1
        if r1==r2:
            r2=r2+1
        a=r2-r1
        b=r3-r4
        c=b/a
        print("Ques: Solve for x, ",r1,"x + ",r3," = ",r2,"x + ",r4)

        o1=(r3+r4)/(r2-r1)
        o2=c
        o3=(r3+r4)/(r2+r1)
        o4=(r3-r4)*(r2-r1)

        print(" option 1 : ",int(o1),"\n","option 2 : ",o2,"\n","option 3 : ","%.3f" % o3,"\n","option 4 : ",int(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x + ",r3," = ",r2,"x + ",r4)
            print(r2,"x - ",r1,"x = ",r3," - ",r4," (taking all varible terms in LHS)")
            print(a,"x = ",b)
            print("x = ",c," (Dividing both sides by ",a,")")
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nright option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")
    def hard():
        r1=random.randint(2,11)#coffi of LHS var
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(2,11)#coffi of RHS var
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(2,21)
        if r3%2!= 0:
            r3=r3+1
        r4=random.randint(2,21)
        if r4%2!= 0:
            r4=r4+1
        if r3==r4:
            r3=r3+1
        if r1==r2:
            r2=r2+1
        a=r2-r1
        b=r3-r4
        c=b/a
        print("Ques: Solve for x, ",r1,"x + ",r3," = ",r2,"x + ",r4)

        o1=(r3+r4)/(r2-r1)
        o2=c
        o3=(r3-r4)/(r2+r1)
        o4=(r3-r4)*(r2-r1)

        print(" option 1 : ",int(o1),"\n","option 2 : ",o2,"\n","option 3 : ","%.3f" % o3,"\n","option 4 : ",int(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x + ",r3," = ",r2,"x + ",r4)
            print(r2,"x - ",r1,"x = ",r3," - ",r4," (taking all varible terms in LHS)")
            print(a,"x = ",b)
            print("x = ",c," (Dividing both sides by ",a,")")
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nright option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nwrong option")
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

def substraction():
    #solve for x,4x-5=5x-4
    def easy():
        r1=random.randint(2,11)#coffi of LHS var
        if r1%2!= 0:
            r1=r1+1
        r2=r1+2
        '''r2=random.randint(2,11)#coffi of RHS var
        if r2%2!= 0:
            r2=r2+1'''
        r3=random.randint(2,21)
        if r3%2!= 0:
            r3=r3+1
        r4=random.randint(2,21)
        if r4%2!= 0:
            r4=r4+1
        if r3==r4:
            r3=r3+1
        if r1==r2:
            r2=r2+1
        a=r2-r1
        b=r4-r3
        c=b/a
        print("Ques: Solve for x, ",r1,"x - ",r3," = ",r2,"x - ",r4)

        o1=(r3+r4)/(r2-r1)
        o2=c
        o3=(r3-r4)/(r2+r1)
        o4=(r3-r4)*(r2-r1)

        print(" option 1 : ",int(o1),"\n","option 2 : ",int(o2),"\n","option 3 : ","%.3f" % o3,"\n","option 4 : ",int(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x - ",r3," = ",r2,"x - ",r4)
            print(r2,"x - ",r1,"x = ",r4," - ",r3," (taking all varible terms in LHS)")
            print(a,"x = ",b)
            print("x = ",c," (Dividing both sides by ",a,")")
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nright option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")
    def hard():
        r1=random.randint(2,11)#coffi of LHS var
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(2,11)#coffi of RHS var
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(2,21)
        if r3%2!= 0:
            r3=r3+1
        r4=random.randint(2,21)
        if r4%2!= 0:
            r4=r4+1
        if r3==r4:
            r3=r3+1
        if r1==r2:
            r2=r2+1
        a=r2-r1
        b=r4-r3
        c=b/a
        print("Ques: Solve for x, ",r1,"x - ",r3," = ",r2,"x - ",r4)

        o1=(r3+r4)/(r2-r1)
        o2=c
        o3=(r3-r4)/(r1+r2)
        o4=(r3-r4)*(r2-r1)

        print(" option 1 : ",int(o1),"\n","option 2 : ",o2,"\n","option 3 : ","%.3f" % o3,"\n","option 4 : ",int(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x - ",r3," = ",r2,"x - ",r4)
            print(r2,"x - ",r1,"x = ",r4," - ",r3," (taking all varible terms in LHS)")
            print(a,"x = ",b)
            print("x = ",c," (Dividing both sides by ",a,")")
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nright option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nwrong option")
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
def addandsub():
    #solve for x,4x+5=5x-4
    def easy():
        r1=random.randint(2,11)#coffi of LHS var
        if r1%2!= 0:
            r1=r1+1
        r2=r1+2
        '''r2=random.randint(2,11)#coffi of RHS var
        if r2%2!= 0:
            r2=r2+1'''
        r3=random.randint(2,21)
        if r3%2!= 0:
            r3=r3+1
        r4=random.randint(2,21)
        if r4%2!= 0:
            r4=r4+1
        if r3==r4:
            r3=r3+1
        if r1==r2:
            r2=r2+1
        a=r2-r1
        b=r3+r4
        c=b/a
        print("Ques: Solve for x, ",r1,"x + ",r3," = ",r2,"x - ",r4)

        o1=(r3-r4)/(r2-r1)
        o2=c
        o3=(r3-r4)/(r2+r1)
        o4=(r3+r4)*(r2-r1)

        print(" option 1 : ",int(o1),"\n","option 2 : ",int(o2),"\n","option 3 : ","%.3f" % o3,"\n","option 4 : ",int(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x + ",r3," = ",r2,"x - ",r4)
            print(r2,"x - ",r1,"x = ",r4," + ",r3," (taking all varible terms in LHS)")
            print(a,"x = ",b)
            print("x = ",c," (Dividing both sides by ",a,")")
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nright option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        elif value==4:
             print("\nwrong option")
             print(">--------------------------<")
             sol()
        else :
            print("\nInvalid Choice")
    def hard():
        r1=random.randint(2,11)#coffi of LHS var
        if r1%2!= 0:
            r1=r1+1
        r2=random.randint(2,11)#coffi of RHS var
        if r2%2!= 0:
            r2=r2+1
        r3=random.randint(2,21)
        if r3%2!= 0:
            r3=r3+1
        r4=random.randint(2,21)
        if r4%2!= 0:
            r4=r4+1
        if r3==r4:
            r3=r3+1
        if r1==r2:
            r2=r2+1
        a=r2-r1
        b=r3+r4
        c=b/a
        print("Ques: Solve for x, ",r1,"x + ",r3," = ",r2,"x - ",r4)

        o1=(r3-r4)/(r2-r1)
        o2=c
        o3=(r3-r4)/(r2+r1)
        o4=(r3+r4)*(r2-r1)

        print(" option 1 : ",int(o1),"\n","option 2 : ",o2,"\n","option 3 : ","%.3f" % o3,"\n","option 4 : ",int(o4),"\n")

        value = int(input("Choose one option : "))

        def sol():
            print("solution: \n")
            print(r1,"x + ",r3," = ",r2,"x - ",r4)
            print(r2,"x - ",r1,"x = ",r4," + ",r3," (taking all varible terms in LHS)")
            print(a,"x = ",b)
            print("x = ",c," (Dividing both sides by ",a,")")
        if value==1:
            print("\nwrong option")
            print(">--------------------------<")
            sol()
        elif value==2:
            print("\nright option")
            print(">--------------------------<")
            sol()
        elif value==3:
             print("\nwrong option")
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
    print("3.Addition as well as substraction")
    ch=int(input("choose the relation between constant and the variable term:"))
    if ch==1:
        addition()
    elif ch==2:
        substraction()
    elif ch==3:
        addandsub()
    else:
        print("invalid choice")


