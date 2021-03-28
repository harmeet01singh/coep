#If Rashmi wieghs 24 kg and Rashi is 21 Kg,
#Radhika is 18 Kg and Ramola 15 kg., which two pairs will form an equation?
#a)...., b)...., c)...., d).... ( an such many examples)

import random
from coep_package.csv import putInCsv,database_fn
from coep_package.latex import latex,to_frac
from IndianNameGenerator import *

n1=""
n2=""
n3=""
n4=""
n5=""
r1=0
r2=0
r3=0
r4=0
items= [' Apples', ' books', ' pens', ' sheets', ' toys', ' candies', ' pencils', ' shirts', ' pants', ' T-shirts', ' Jackets', ' Bananas', ' chocolates', ' Watermelons', ' Cookies'  ]
i= ''


def change_globals():
    global n1,n2,n3,n4,n5,r1,r2,r3,r4,i
    i= random.choice(items)

    n1=randomMarathi()
    n2=randomMarathi()
    n3=randomMarathi()
    n4=randomMarathi()
    n5=randomMarathi()

    if n1==n2 or n1==n3 or n1==n4 or n1==n5 or n2==n3 or n3==n4 or n4==n5 or n1==n2==n3==n4==n5:
        n1=randomMarathi()
        n2=randomMarathi()
        n3=randomMarathi()
        n4=randomMarathi()
        n5=randomMarathi()

    r1 = random.randint(25, 54)
    if r1%2!=0:
        r1=r1+1
    r2 = random.randint(25, 58)
    if r2%2!=0:
        r2=r2+1
    r3 = random.randint(1, 2)
    if r3%2!=0:
        r3=r3+1
    
    #weights should not be same
    if r1==r2 or r1==r3 or r2==r3 or r1==r2==r3:
        r1=r1+5
        r2=r2+8
        r3=r3+1
        
    r3=r1*r3

    r4=int((r3/r1)*r2)

    r=random.randint(0,15)
    if r>3 and r<7:
        r4,r3=r3,r4

    elif r>7 and r<11:
        r4,r2=r2,r4

    elif r>11 and r<15:
        r4,r1=r1,r4
        


def main_function():
    change_globals()
    x=random.randint(0,5)
    #print(x)
    if x>=0 and x<=2:
        #Question
        question="If "+n1+" weighs "+latex(str(r1))+" Kg and "+n2+" weighs "+latex(str(r2))+" Kg, "+n3+" weighs "+latex(str(r3))+" Kg and "+n4+" weighs "+latex(str(r4))+" Kg.\nWhich two pairs will form an equation?\n"
        print(question)
        op=["","","",""]
        sq=[0,1,2,3]
        #options


        if r1/r2==r3/r4 or r2/r1==r4/r3 or r1/r2==r4/r3 or r2/r1==r3/r4:
            o3='''('''+n1+''' , '''+n2+''') and ('''+n3+''' , '''+n4+''')'''
            o1='''('''+n1+''' , '''+n3+''') and ('''+n2+''' , '''+n4+''')'''
            o2='''('''+n1+''' , '''+n4+''') and ('''+n2+''' , '''+n3+''')'''
            o4='''('''+n1+''' , '''+n4+''') and ('''+n2+''' , '''+n5+''')'''
        elif r1/r3==r2/r4 or r3/r1==r4/r2 or r1/r3==r4/r2 or r3/r1==r2/r4:
            o3='''('''+n1+''' , '''+n3+''') and ('''+n2+''' , '''+n4+''')'''
            o1='''('''+n1+''' , '''+n2+''') and ('''+n3+''' , '''+n4+''')'''
            o2='''('''+n1+''' , '''+n4+''') and ('''+n2+''' , '''+n3+''')'''
            o4='''('''+n1+''' , '''+n5+''') and ('''+n2+''' , '''+n3+''')'''
        elif r1/r4==r2/r3 or r4/r1==r3/r2 or r1/r4==r3/r2 or r4/r1==r2/r3:
            o3='''('''+n1+''' , '''+n4+''') and ('''+n2+''' , '''+n3+''')'''
            o1='''('''+n1+''' , '''+n3+''') and ('''+n2+''' , '''+n4+''')'''
            o2='''('''+n1+''' , '''+n2+''') and ('''+n3+''' , '''+n4+''')'''
            o4='''('''+n1+''' , '''+n4+''') and ('''+n5+''' , '''+n3+''')'''

        ra=random.randint(0,3)
        op[ra]=o3
        sq.remove(ra)
        op[sq[0]]=o1
        op[sq[1]]=o2
        op[sq[2]]=o4
        #PRINTING OPTIONS
        for z in range(1,5):
                print("Option",z,":",op[z-1])
            
        print("")
        value = 3 #int(input("Enter the option number : "))

        def sol3():
            sol3=("Since, it is given that the weights of "+n1+", "+n2+", "+n3+" and "+n4+"\nare "+latex(str(r1))+", "+latex(str(r2))+", "+latex(str(r3))+" and "+latex(str(r4))+" respectively")+"\n"
            if r1/r2==r3/r4:
                a="{:.2f}".format(r1/r2)
                b="{:.2f}".format(r3/r4)
                sol3=sol3+("Now, "+latex(to_frac(str(r1),str(r2))+" = "+str(a)))+"\n"
                sol3=sol3+("Also, "+latex(to_frac(str(r3),str(r4))+" = "+str(b)))+"\n"
                sol3=sol3+("=> "+latex(to_frac(str(r1),str(r2))+" = "+to_frac(str(r3),str(r4))))+"\n"
                sol3=sol3+("=> L.H.S = R.H.S")+"\n"
                sol3=sol3+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol3=sol3+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n2+" , "+n3+" and "+n4)+"\n"

            elif r2/r1==r4/r3:
                a="{:.2f}".format(r2/r1)
                b="{:.2f}".format(r4/r3)
                sol3=sol3+("Now, "+latex(to_frac(str(r2),str(r1))+" = "+str(a)))+"\n"
                sol3=sol3+("Also, "+latex(to_frac(str(r4),str(r3))+" = "+str(b)))+"\n"
                sol3=sol3+("=> "+latex(to_frac(str(r2),str(r1))+" = "+to_frac(str(r4),str(r3))))+"\n"
                sol3=sol3+("=> L.H.S = R.H.S")+"\n"
                sol3=sol3+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol3=sol3+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n2+" , "+n3+" and "+n4)+"\n"

            elif r1/r2==r4/r3:
                a="{:.2f}".format(r1/r2)
                b="{:.2f}".format(r4/r3)
                sol3=sol3+("Now, "+latex(to_frac(str(r1),str(r2))+" = "+str(a)))+"\n"
                sol3=sol3+("Also, "+latex(to_frac(str(r4),str(r3))+" = "+str(b)))+"\n"
                sol3=sol3+("=> "+latex(to_frac(str(r1),str(r2))+" = "+to_frac(str(r4),str(r3))))+"\n"
                sol3=sol3+("=> L.H.S = R.H.S")+"\n"
                sol3=sol3+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol3=sol3+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n2+" , "+n3+" and "+n4)+"\n"


            elif r2/r1==r3/r4:
                a="{:.2f}".format(r2/r1)
                b="{:.2f}".format(r3/r4)
                sol3=sol3+("Now, "+latex(to_frac(str(r2),str(r1))+" = "+str(a)))+"\n"
                sol3=sol3+("Also, "+latex(to_frac(str(r3),str(r4))+" = "+str(b)))+"\n"
                sol3=sol3+("=> "+latex(to_frac(str(r2),str(r1))+" = "+to_frac(str(r3),str(r4))))+"\n"
                sol3=sol3+("=> L.H.S = R.H.S")+"\n"
                sol3=sol3+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol3=sol3+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n2+" , "+n3+" and "+n4)+"\n"

                
            
            elif r1/r3==r2/r4:
                a="{:.2f}".format(r1/r3)
                b="{:.2f}".format(r2/r4)
                sol3=sol3+("Now, "+latex(to_frac(str(r1),str(r3))+" = "+str(a)))+"\n"
                sol3=sol3+("Also, "+latex(to_frac(str(r2),str(r4))+" = "+str(b)))+"\n"
                sol3=sol3+("=> "+latex(to_frac(str(r1),str(r3))+" = "+to_frac(str(r2),str(r4))))+"\n"
                sol3=sol3+("=> L.H.S = R.H.S")+"\n"
                sol3=sol3+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol3=sol3+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n3+" , "+n2+" and "+n4)+"\n"

            elif r3/r1==r4/r2:
                a="{:.2f}".format(r3/r1)
                b="{:.2f}".format(r4/r2)
                sol3=sol3+("Now, "+latex(to_frac(str(r3),str(r1))+" = "+str(a)))+"\n"
                sol3=sol3+("Also, "+latex(to_frac(str(r4),str(r2))+" = "+str(b)))+"\n"
                sol3=sol3+("=> "+latex(to_frac(str(r3),str(r1))+" = "+to_frac(str(r4),str(r2))))+"\n"
                sol3=sol3+("=> L.H.S = R.H.S")+"\n"
                sol3=sol3+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol3=sol3+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n3+" , "+n2+" and "+n4)+"\n"



            elif r1/r3==r4/r2:
                a="{:.2f}".format(r1/r3)
                b="{:.2f}".format(r4/r2)
                sol3=sol3+("Now, "+latex(to_frac(str(r1),str(r3))+" = "+str(a)))+"\n"
                sol3=sol3+("Also, "+latex(to_frac(str(r4),str(r2))+" = "+str(b)))+"\n"
                sol3=sol3+("=> "+latex(to_frac(str(r1),str(r3))+" = "+to_frac(str(r4),str(r2))))+"\n"
                sol3=sol3+("=> L.H.S = R.H.S")+"\n"
                sol3=sol3+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol3=sol3+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n3+" , "+n2+" and "+n4)+"\n"


            elif r3/r1==r2/r4:
                a="{:.2f}".format(r3/r1)
                b="{:.2f}".format(r2/r4)
                sol3=sol3+("Now, "+latex(to_frac(str(r3),str(r1))+" = "+str(a)))+"\n"
                sol3=sol3+("Also,"+latex(to_frac(str(r2),str(r4))+" = "+str(b)))+"\n"
                sol3=sol3+("=> "+latex(to_frac(str(r3),str(r1))+" = "+to_frac(str(r2),str(r4))))+"\n"
                sol3=sol3+("=> L.H.S = R.H.S")+"\n"
                sol3=sol3+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol3=sol3+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n3+" , "+n2+" and "+n4)+"\n"


            
            elif r1/r4==r2/r3:
                a="{:.2f}".format(r1/r4)
                b="{:.2f}".format(r2/r3)
                sol3=sol3+("Now, "+latex(to_frac(str(r1),str(r4))+" = "+str(a)))+"\n"
                sol3=sol3+("Also, "+latex(to_frac(str(r2),str(r3))+" = "+str(b)))+"\n"
                sol3=sol3+("=> "+latex(to_frac(str(r1),str(r4))+" = "+to_frac(str(r2),str(r3))))+"\n"
                sol3=sol3+("=> L.H.S = R.H.S")+"\n"
                sol3=sol3+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol3=sol3+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n4+" , "+n2+" and "+n3)+"\n"
                
            elif r4/r1==r3/r2:
                a="{:.2f}".format(r4/r1)
                b="{:.2f}".format(r3/r2)
                sol3=sol3+("Now, "+latex(to_frac(str(r4),str(r1))+" = "+str(a)))+"\n"
                sol3=sol3+("Also, "+latex(to_frac(str(r3),str(r2))+" = "+str(b)))+"\n"
                sol3=sol3+("=> "+latex(to_frac(str(r4),str(r1))+" = "+to_frac(str(r3),str(r2))))+"\n"
                sol3=sol3+("=> L.H.S = R.H.S")+"\n"
                sol3=sol3+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol3=sol3+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n4+" , "+n2+" and "+n3)+"\n"



            elif r1/r4==r3/r2:
                a="{:.2f}".format(r1/r4)
                b="{:.2f}".format(r3/r2)
                sol3=sol3+("Now, "+latex(to_frac(str(r1),str(r4))+" = "+str(a)))+"\n"
                sol3=sol3+("Also, "+latex(to_frac(str(r3),str(r2))+" = "+str(b)))+"\n"
                sol3=sol3+("=> "+latex(to_frac(str(r1),str(r4))+" = "+to_frac(str(r3),str(r2))))+"\n"
                sol3=sol3+("=> L.H.S = R.H.S")+"\n"
                sol3=sol3+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol3=sol3+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n4+" , "+n2+" and "+n3)+"\n"



            elif r4/r1==r2/r3:
                a="{:.2f}".format(r4/r1)
                b="{:.2f}".format(r2/r3)
                sol3=sol3+("Now, "+latex(to_frac(str(r4),str(r1))+" = "+str(a)))+"\n"
                sol3=sol3+("Also, "+latex(to_frac(str(r2),str(r3))+" = "+str(b)))+"\n"
                sol3=sol3+("=> "+latex(to_frac(str(r4),str(r1))+" = "+to_frac(str(r2),str(r3))))+"\n"
                sol3=sol3+("=> L.H.S = R.H.S")+"\n"
                sol3=sol3+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol3=sol3+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n4+" , "+n2+" and "+n3)+"\n"

            return sol3			


        if value==ra+1:
                print("\nYour answer is Correct!")
                print(">------------- SOLUTION -------------<")
                print(sol3())
        elif value!=ra+1 and value<5 and value>0:
                print("\nYour answer is incorrect!")
                print(">------------- SOLUTION --------------<")
                print(sol3())
        else :
                print("invalid choice")


    elif x>2 and x<=5:
        #Question
        question="If "+n1+" has "+latex(str(r1))+" "+i+", "+n2+" has "+latex(str(r2))+" "+i+", "+n3+" has "+latex(str(r3))+" "+i+" and "+n4+" has "+latex(str(r4))+" "+i+".\nWhich two pairs will form an equation?\n"
        print(question)
        op=["","","",""]
        sq=[0,1,2,3]
        #options


        if r1/r2==r3/r4 or r2/r1==r4/r3 or r1/r2==r4/r3 or r2/r1==r3/r4:
            o3='''('''+n1+''' , '''+n2+''') and ('''+n3+''' , '''+n4+''')'''
            o1='''('''+n1+''' , '''+n3+''') and ('''+n2+''' , '''+n4+''')'''
            o2='''('''+n1+''' , '''+n4+''') and ('''+n2+''' , '''+n3+''')'''
            o4='''('''+n1+''' , '''+n4+''') and ('''+n2+''' , '''+n5+''')'''
        elif r1/r3==r2/r4 or r3/r1==r4/r2 or r1/r3==r4/r2 or r3/r1==r2/r4:
            o3='''('''+n1+''' , '''+n3+''') and ('''+n2+''' , '''+n4+''')'''
            o1='''('''+n1+''' , '''+n2+''') and ('''+n3+''' , '''+n4+''')'''
            o2='''('''+n1+''' , '''+n4+''') and ('''+n2+''' , '''+n3+''')'''
            o4='''('''+n1+''' , '''+n5+''') and ('''+n2+''' , '''+n3+''')'''
        elif r1/r4==r2/r3 or r4/r1==r3/r2 or r1/r4==r3/r2 or r4/r1==r2/r3:
            o3='''('''+n1+''' , '''+n4+''') and ('''+n2+''' , '''+n3+''')'''
            o1='''('''+n1+''' , '''+n3+''') and ('''+n2+''' , '''+n4+''')'''
            o2='''('''+n1+''' , '''+n2+''') and ('''+n3+''' , '''+n4+''')'''
            o4='''('''+n1+''' , '''+n4+''') and ('''+n5+''' , '''+n3+''')'''

        ra=random.randint(0,3)
        op[ra]=o3
        sq.remove(ra)
        op[sq[0]]=o1
        op[sq[1]]=o2
        op[sq[2]]=o4
        #PRINTING OPTIONS
        for z in range(1,5):
                print("Option",z,":",op[z-1])
            
        print("")
        value = 3 #int(input("Enter the option number : "))

        def sol4():
            sol4=("Since, it is given that the weights of "+n1+", "+n2+", "+n3+" and "+n4+"\nare "+latex(str(r1))+", "+latex(str(r2))+", "+latex(str(r3))+" and "+latex(str(r4))+" respectively")+"\n"
            if r1/r2==r3/r4:
                a="{:.2f}".format(r1/r2)
                b="{:.2f}".format(r3/r4)
                sol4=sol4+("Now, "+latex(to_frac(str(r1),str(r2))+" = "+str(a)))+"\n"
                sol4=sol4+("Also, "+latex(to_frac(str(r3),str(r4))+" = "+str(b)))+"\n"
                sol4=sol4+("=> "+latex(to_frac(str(r1),str(r2))+" = "+to_frac(str(r3),str(r4))))+"\n"
                sol4=sol4+("=> L.H.S = R.H.S")+"\n"
                sol4=sol4+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol4=sol4+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n2+" , "+n3+" and "+n4)+"\n"

            elif r2/r1==r4/r3:
                a="{:.2f}".format(r2/r1)
                b="{:.2f}".format(r4/r3)
                sol4=sol4+("Now, "+latex(to_frac(str(r2),str(r1))+" = "+str(a)))+"\n"
                sol4=sol4+("Also, "+latex(to_frac(str(r4),str(r3))+" = "+str(b)))+"\n"
                sol4=sol4+("=> "+latex(to_frac(str(r2),str(r1))+" = "+to_frac(str(r4),str(r3))))+"\n"
                sol4=sol4+("=> L.H.S = R.H.S")+"\n"
                sol4=sol4+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol4=sol4+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n2+" , "+n3+" and "+n4)+"\n"

            elif r1/r2==r4/r3:
                a="{:.2f}".format(r1/r2)
                b="{:.2f}".format(r4/r3)
                sol4=sol4+("Now, "+latex(to_frac(str(r1),str(r2))+" = "+str(a)))+"\n"
                sol4=sol4+("Also, "+latex(to_frac(str(r4),str(r3))+" = "+str(b)))+"\n"
                sol4=sol4+("=> "+latex(to_frac(str(r1),str(r2))+" = "+to_frac(str(r4),str(r3))))+"\n"
                sol4=sol4+("=> L.H.S = R.H.S")+"\n"
                sol4=sol4+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol4=sol4+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n2+" , "+n3+" and "+n4)+"\n"


            elif r2/r1==r3/r4:
                a="{:.2f}".format(r2/r1)
                b="{:.2f}".format(r3/r4)
                sol4=sol4+("Now, "+latex(to_frac(str(r2),str(r1))+" = "+str(a)))+"\n"
                sol4=sol4+("Also, "+latex(to_frac(str(r3),str(r4))+" = "+str(b)))+"\n"
                sol4=sol4+("=> "+latex(to_frac(str(r2),str(r1))+" = "+to_frac(str(r3),str(r4))))+"\n"
                sol4=sol4+("=> L.H.S = R.H.S")+"\n"
                sol4=sol4+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol4=sol4+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n2+" , "+n3+" and "+n4)+"\n"

                
            
            elif r1/r3==r2/r4:
                a="{:.2f}".format(r1/r3)
                b="{:.2f}".format(r2/r4)
                sol4=sol4+("Now, "+latex(to_frac(str(r1),str(r3))+" = "+str(a)))+"\n"
                sol4=sol4+("Also, "+latex(to_frac(str(r2),str(r4))+" = "+str(b)))+"\n"
                sol4=sol4+("=> "+latex(to_frac(str(r1),str(r3))+" = "+to_frac(str(r2),str(r4))))+"\n"
                sol4=sol4+("=> L.H.S = R.H.S")+"\n"
                sol4=sol4+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol4=sol4+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n3+" , "+n2+" and "+n4)+"\n"

            elif r3/r1==r4/r2:
                a="{:.2f}".format(r3/r1)
                b="{:.2f}".format(r4/r2)
                sol4=sol4+("Now, "+latex(to_frac(str(r3),str(r1))+" = "+str(a)))+"\n"
                sol4=sol4+("Also, "+latex(to_frac(str(r4),str(r2))+" = "+str(b)))+"\n"
                sol4=sol4+("=> "+latex(to_frac(str(r3),str(r1))+" = "+to_frac(str(r4),str(r2))))+"\n"
                sol4=sol4+("=> L.H.S = R.H.S")+"\n"
                sol4=sol4+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol4=sol4+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n3+" , "+n2+" and "+n4)+"\n"



            elif r1/r3==r4/r2:
                a="{:.2f}".format(r1/r3)
                b="{:.2f}".format(r4/r2)
                sol4=sol4+("Now, "+latex(to_frac(str(r1),str(r3))+" = "+str(a)))+"\n"
                sol4=sol4+("Also, "+latex(to_frac(str(r4),str(r2))+" = "+str(b)))+"\n"
                sol4=sol4+("=> "+latex(to_frac(str(r1),str(r3))+" = "+to_frac(str(r4),str(r2))))+"\n"
                sol4=sol4+("=> L.H.S = R.H.S")+"\n"
                sol4=sol4+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol4=sol4+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n3+" , "+n2+" and "+n4)+"\n"


            elif r3/r1==r2/r4:
                a="{:.2f}".format(r3/r1)+"\n"
                b="{:.2f}".format(r2/r4)+"\n"
                sol4=sol4+("Now, "+latex(to_frac(str(r3),str(r1))+" = "+str(a)))+"\n"
                sol4=sol4+("Also,"+latex(to_frac(str(r2),str(r4))+" = "+str(b)))+"\n"
                sol4=sol4+("=> "+latex(to_frac(str(r3),str(r1))+" = "+to_frac(str(r2),str(r4))))+"\n"
                sol4=sol4+("=> L.H.S = R.H.S")+"\n"
                sol4=sol4+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol4=sol4+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n3+" , "+n2+" and "+n4)+"\n"


            
            elif r1/r4==r2/r3:
                a="{:.2f}".format(r1/r4)
                b="{:.2f}".format(r2/r3)
                sol4=sol4+("Now, "+latex(to_frac(str(r1),str(r4))+" = "+str(a)))+"\n"
                sol4=sol4+("Also, "+latex(to_frac(str(r2),str(r3))+" = "+str(b)))+"\n"
                sol4=sol4+("=> "+latex(to_frac(str(r1),str(r4))+" = "+to_frac(str(r2),str(r3))))+"\n"
                sol4=sol4+("=> L.H.S = R.H.S")+"\n"
                sol4=sol4+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol4=sol4+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n4+" , "+n2+" and "+n3)+"\n"
                
            elif r4/r1==r3/r2:
                a="{:.2f}".format(r4/r1)
                b="{:.2f}".format(r3/r2)
                sol4=sol4+("Now, "+latex(to_frac(str(r4),str(r1))+" = "+str(a)))+"\n"
                sol4=sol4+("Also, "+latex(to_frac(str(r3),str(r2))+" = "+str(b)))+"\n"
                sol4=sol4+("=> "+latex(to_frac(str(r4),str(r1))+" = "+to_frac(str(r3),str(r2))))+"\n"
                sol4=sol4+("=> L.H.S = R.H.S")+"\n"
                sol4=sol4+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol4=sol4+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n4+" , "+n2+" and "+n3)+"\n"



            elif r1/r4==r3/r2:
                a="{:.2f}".format(r1/r4)
                b="{:.2f}".format(r3/r2)
                sol4=sol4+("Now, "+latex(to_frac(str(r1),str(r4))+" = "+str(a)))+"\n"
                sol4=sol4+("Also, "+latex(to_frac(str(r3),str(r2))+" = "+str(b)))+"\n"
                sol4=sol4+("=> "+latex(to_frac(str(r1),str(r4))+" = "+to_frac(str(r3),str(r2))))+"\n"
                sol4=sol4+("=> L.H.S = R.H.S")+"\n"
                sol4=sol4+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol4=sol4+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n4+" , "+n2+" and "+n3)+"\n"



            elif r4/r1==r2/r3:
                a="{:.2f}".format(r4/r1)
                b="{:.2f}".format(r2/r3)
                sol4=sol4+("Now, "+latex(to_frac(str(r4),str(r1))+" = "+str(a)))+"\n"
                sol4=sol4+("Also, "+latex(to_frac(str(r2),str(r3))+" = "+str(b)))+"\n"
                sol4=sol4+("=> "+latex(to_frac(str(r4),str(r1))+" = "+to_frac(str(r2),str(r3))))+"\n"
                sol4=sol4+("=> L.H.S = R.H.S")+"\n"
                sol4=sol4+("As we know that,\nAn Equation is a mathematical statement consisting of an equal symbol between two expressions having the same value.")+"\n"
                sol4=sol4+("Therefore, according to the question,\nThe two pairs which will form an equation are : "+n1+" and "+n4+" , "+n2+" and "+n3)+"\n"

            return sol4			


        if value==ra+1:
                print("\nYour answer is Correct!")
                print(">------------- SOLUTION -------------<")
                print(sol4())
        elif value!=ra+1 and value<5 and value>0:
                print("\nYour answer is incorrect!")
                print(">------------- SOLUTION --------------<")
                print(sol4())
        else :
                print("invalid choice")            


    if x>=0 and x<=2:
        sol=sol3()

    elif x>2 and x<=5:
        sol=sol4()



    database_dict= database_fn(
    Question_Type='text',	
    Answer_Type='1',
    Topic_Number='030102',
    Variation=3,
    Question=question,
    Correct_Answer_1=o3,
    Wrong_Answer_1=o1,
    Wrong_Answer_2=o2,
    Wrong_Answer_3=o4,
    ContributorMail='2018.aaryan.raina@ves.ac.in',
    Solution_text=sol
    )
    return database_dict

#main_function()
putInCsv('030102',20,main_function,'v3_2')                