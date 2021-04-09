import random
from coep_package.csv import putInCsv,database_fn
from coep_package.latex import latex,to_frac
from IndianNameGenerator import *
from fractions import Fraction

def main_function():

    n1=randomMarathi()
    n2=randomMarathi()

    r2 = random.randint(1, 5)
    r9=random.randint(2, 7)
    if r2%r9==0:
        r9=r9+1
    if r2>r9:
        r2,r9=r9,r2

    r10_latex=latex(to_frac(str(r2),str(r9)))
    r10=Fraction(r2,r9)   
    r1 = random.randint(10, 60)


    #option 4
    c=(r1)/(r10+1)
    d=c*r10

    #option 1
    r3 = random.randint(10, 30)
    #options should not be same
    if r3==c or r3==d:
            r3=r3+1

    r4=abs(r1-r3)

    if r3==r1:
            r3=r3-15
            r4=15

    #option 2
    r5 = random.randint(10, 30)
    #options should not be same
    if r5==c:
        r5=r5+1
        
    r6 = r10*r5 

    #option 3
    r7 = d
    r8 = c

    items= ['Lemonade', 'Tea', 'Coffee', 'Milk', 'Orange juice', 'Mango juice', 'water', 'Soup', 'Soft drink', 'Oil', 'Apple juice']

    i= random.choice(items)

    temp1=n1+' and '+n2+' have a total of '+str(r1)+' litres of '+i+'. '

    r=random.randint(1,5)
    if r>3:
            n1,n2=n2,n1

    temp2='If '+n2+' has '+str(r10_latex)+' times the '+i+' that '+n1+' has, how many litres of '+i+' does each one have?\n'

    question=temp1+temp2
    print(question)

    op=["","","",""]
    sq=[0,1,2,3]
    #option variables
    o1= n1+''' has '''+latex(str((r3)))+''' litres of '''+i+''' and '''+n2+''' has '''+latex(str((r4)))+''' litres of '''+i
    o2= n1+''' has '''+latex(str((r5)))+''' litres of '''+i+''' and '''+n2+''' has '''+latex(str((r6)))+''' litres of '''+i
    o3= n1+''' has '''+latex(str((c)))+''' litres of '''+i+''' and '''+n2+''' has '''+latex(str((d)))+''' litres of '''+i
    o4= n1+''' has '''+latex(str((r7)))+''' litres of '''+i+''' and '''+n2+''' has '''+latex(str((r8)))+''' litres of '''+i

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


    #solution function
    def sol():
        sol=( '''let '''+n1+''' has '''+latex('x')+''' litres of '''+i+'''.
    <br/>Since, '''+n2+''' has '''+(r10_latex)+''' times the '''+i+''' that '''+n1+''' has
        <br/>Therefore, '''+n2+''' will have ('''+r10_latex+''')* '''+latex('x')+''' litres of '''+i+'''.  
    <br/>Since, '''+n1+''' and '''+n2+''' have a total of '''+latex(str(r1))+''' litres of '''+i+'''
        <br/>=>'''+latex('''x+(''')+r10_latex+latex(''')*x='''+str(r1))+'''       
        <br/>Taking '''+latex('x')+''' common from both the terms in L.H.S :-
        <br/>=> '''+latex('''(1+''')+r10_latex+latex(''')*x='''+str(r1)))+"\n"
        sol=sol+(" <br/>   => "+latex("("+to_frac(str(r2+r9),str(r9))+")* x ="+str(r1)))+"\n"
        a=r10+1
        sol=sol+("<br/>Dividing both the sides by "+latex(to_frac(str(r2+r9),str(r9))))+"\n"    
        sol=sol+(" <br/>   => "+latex("x="+to_frac(str(r1),str(a))))+"\n"
        sol=sol+(" <br/>   => "+latex("x="+str(r1/a)))+"\n"
        b=Fraction((r2+r9),(r9))
        sol=sol+(" <br/>   => "+latex("(")+r10_latex+latex(")*x = (")+r10_latex+latex(")*("+to_frac(str(r1),str(b))+")="+str((r1/a)*r10)))+"\n"
        sol=sol+('<br/>Hence, '+n1+' has '+latex(str((r1/a)))+' litres of '+i+' and '+n2+' has '+latex(str(((r1/a)*r10)))+' litres of '+i+' ')+"\n"

        return sol


    if value==ra+1:
            print("\nYour answer is Correct!")
            print(">------------- SOLUTION -------------<")
            print(sol())
    elif value!=ra+1 and value<5 and value>0:
            print("\nYour answer is incorrect!")
            print(">------------- SOLUTION --------------<")
            print(sol())
    else :
            print("invalid choice")


    database_dict= database_fn(
    Answer_Type='1',
    Topic_Number='030203',
    Variation='v3_12',
    Question=question,
    Correct_Answer_1=o3,
    Wrong_Answer_1=o1,
    Wrong_Answer_2=o2,
    Wrong_Answer_3=o4,
    ContributorMail='2018.aaryan.raina@ves.ac.in',
    Solution_text=sol()
    )
    return database_dict

#main_function()
putInCsv('030203',15,main_function,'v3_12')