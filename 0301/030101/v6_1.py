#. In a 'Tug of War' if no side wins it is an equation - True or False
import random
from coep_package.latex import latex
from coep_package.csv_module import database_fn, putInCsv
from IndianNameGenerator import *

n1=''
n2=''

r1=0
r2=0
r3=0
r4=0
r5=0
r6=0
r7=0
items= [' Apples', ' books', ' pens', ' sheets', ' toys', ' candies', ' pencils', ' shirts', ' pants', ' T-shirts', ' Jackets', ' Bananas', ' chocolates', ' Watermelons', ' Cookies'  ]

i= ''
def change_globals():
    global n1,n2,r1,r2,r3,r4,r5,r6,r7,i
    n1=randomMarathi()
    n2=randomMarathi()
    r1=random.randint(25,85)
    r3=random.randint(3,6)
    r2= r3*r1
    r4=random.randint(25,86)
    r6=random.randint(25,56)
    r5=r6+r4
    r7=random.randint(25,86)
    i= random.choice(items)
    
def main_function():
    change_globals()
    eq=["If "+n1+" has "+latex(str(r1))+i+" and "+n2+" has "+latex(str(r2))+i+" then "+n2+" has "+latex(str(r3))+" times the "+i+" that "+n1+" has" ,"In a Tug of War if no side wins","A weighing scale having its needle in center","Two persons sitting on either side of a See-Saw, having equal weights","If there are equal weights in both pans of a weighing scale, then the scale is balanced. Such a balanced scale is like an equation.","If "+n1+" has "+latex(str(r4))+i+" and "+n2+" has "+latex(str(r5))+i+" then "+n2+" has "+latex(str(r6))+i+" more than "+n1]
    nteq=["If "+n1+" has "+latex(str(r1))+i+" and "+n2+" has "+latex(str(r2))+i+" then "+n2+" has "+latex("2")+" times the "+i+" that "+n1+" has","A See-Saw having only one person sitting on a side","Two persons A and B are sitting on either side of a See-Saw. Person A is having more weight than Person B","In a Tug of War if a side wins","A weighing machine having "+latex("2")+" Kg  rice on one side and "+latex("1")+" Kg sugar on the other side","If "+n1+" has "+latex(str(r4))+i+" and "+n2+" has "+latex(str(r5))+i+" then "+n2+" has "+latex(str(r7))+i+" more than "+n1]
    #same time same speed same distance
    ques1=random.choice([eq,nteq])
    cop=random.choice(ques1)
    ques_f=cop+", it is an equation. State True or False.\n"
    print(ques_f)
    o1="option 1 : True"
    o2="option 2 : False"

##    r=random.randint(0,5)
##    if r>3:
##        o1="option 1 : False"
##        o2="option 2 : True"

    print(o1)
    print(o2)
    print("")
    val=1#int(input("Enter the option number : "))
    # if val==1 and cop in eq:
        
    #         sol=("Your answer is correct")
    #         sol=sol+("------------ SOLUTION -------------")
    #         sol=sol+("Since, we know that, an equation is defined as a mathematical statement consisting of two algebraic expressions having the same value")
    #         sol=sol+("So, in an equation there is always an '=' sign and the expression on the right hand side of the '=' sign is called the RHS.\nThe expression on the left hand side of the '=' sign is called the LHS.")
    #         sol=sol+("Therefore, according to the question, LHS is equal to RHS")
    #         sol=sol+("Thus,"+ cop +" will form an equation")
            
    # if val==2 and cop in nteq:
        
    #         sol=("Your answer is correct")
    #         sol=sol+("------------ SOLUTION -------------")
    #         sol=sol+("Since, we know that, an equation is defined as a mathematical statement consisting of two algebraic expressions having the same value")
    #         sol=sol+("So, in an equation there is always an '=' sign and the expression on the right hand side of the '=' sign is called the RHS.\nThe expression on the left hand side of the '=' sign is called the LHS.")
    #         sol=sol+("Therefore, according to the question, LHS is not equal to RHS")
    #         sol=sol+("Thus, "+cop+" will not form an equation")
           
    # elif val not in [1,2]:
    #         print("Invalid Choice")
    # else:
    #         print("Your answer is incorrect")
    #         if cop in eq:
    #             print("------------ SOLUTION ------------- ")
    #             print("Since, we know that, an equation is defined as a mathematical statement consisting of two algebraic expressions having the same value")+"\n"
    #             print("So, in an equation there is always an '=' sign and the expression on the right hand side of the '=' sign is called the RHS.\nThe expression on the left hand side of the '=' sign is called the LHS.")+"\n"
    #             print("Therefore, according to the question, LHS is equal to RHS")
    #             print("Thus, "+cop+" will form an equation")
                
    #         elif cop in nteq:
    #             print("------------ SOLUTION --------------- ")
    #             print("Since, we know that, an equation is defined as a mathematical statement consisting of two algebraic expressions having the same value")
    #             print("So, in an equation there is always an '=' sign and the expression on the right hand side of the '=' sign is called the RHS.\nThe expression on the left hand side of the '=' sign is called the LHS.")
    #             print("Therefore, according to the question, LHS is not equal to RHS")
    #             print("Thus, "+cop+" will not form an equation")
               
    if cop in eq:

        
        sol=("An equation is defined as a mathematical statement consisting of two algebraic expressions having the same value")
        sol=sol+('''<br/>So, in an equation there is always an '=' sign,
The expression on the right hand side of the '=' sign is called the RHS.
The expression on the left hand side of the '=' sign is called the LHS
''')
        sol=sol+("<br/>An equation is formed only if LHS is equal to RHS")
        sol=sol+("<br/>But in this question, LHS is equal to RHS")
        sol=sol+("<br/>Thus, "+ cop +" will form an equation")
        Solution = sol
        Corr_op = "True"
        wrong_op1="False"
    if cop in nteq:

        
        sol=("An equation is defined as a mathematical statement consisting of two algebraic expressions having the same value")
        sol=sol+('''<br/>So, in an equation there is always an '=' sign ,
The expression on the right hand side of the '=' sign is called the RHS.
The expression on the left hand side of the '=' sign is called the LHS
''')
        sol=sol+("<br/>An equation is formed only if LHS is equal to RHS")
        sol=sol+("<br/>But in this question, LHS is not equal to RHS")
        sol=sol+("<br/>Thus, "+ cop +" will not form an equation")
        Solution = sol
        Corr_op = "False"
        wrong_op1="True"
    database_dict= database_fn(
    'text',
    Answer_Type='4',
    Topic_Number='030101',
    Variation=6,
    Question=ques_f,
    Correct_Answer_1=Corr_op,
    Wrong_Answer_1=wrong_op1,
    ContributorMail='2018.aaryan.raina@ves.ac.in',
    Solution_text=Solution
    )
    return database_dict            

#main_function()
putInCsv('030101',15,main_function,'v6_1',Create_Textfile=True,Remove_Duplicates=True)
