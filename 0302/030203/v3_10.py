from coep_package.csv import putInCsv,database_fn
from coep_package.latex import latex,to_frac        
from IndianNameGenerator import *
import random

def main_function():

    n1=randomMarathi()
    n2=randomMarathi()

    r2 = random.randint(1, 20)
    if r2%2!= 0:
            r2=r2+1

    r1 = random.randint(45, 100)
    if r1%2!= 0:
            r1=r1+1

    #option 4
    c=(r1+r2)/2
    d=c-r2

    #option 1
    r3 = random.randint(25, 40)
    #options should not be same
    if r3==c or r3==d:
            r3=r3+1

    r4=abs(r1-r3)

    if r3==r1:
            r3=r3-15
            r4=15

    #option 2
    r5 = random.randint(22, 50)
    #options should not be same
    if r5==c:
        r5=r5+1
        
    r6 = r5-r2

    #option 3
    r7 = d
    r8 = c

    items= ['Apples', 'books', 'pens', 'sheets', 'toys', 'candies', 'pencils', 'shirts', 'pants', 'T-shirts', 'Jackets', 'Bananas', 'chocolates', 'Watermelons', 'Cookies']

    i= random.choice(items)

    temp1= n1+' and '+n2+' have a total of '+str(r1)+' '+i+'.'

    r=random.randint(1,5)
    if r>3:
            n1,n2=n2,n1
            
    temp2='If '+n2+' has '+str(r2)+''+i+'less than '+n1+', how many '+i+' does each one have?\n'

    question=temp1+temp2
    print(question)

    op=["","","",""]
    sq=[0,1,2,3]
    #option variables
    o1= n1+''' has '''+str(int(r3))+''' '''+i+''' and '''+n2+''' has '''+str(int(r4))+''' '''+i
    o2= n1+''' has '''+str(int(r5))+''' '''+i+''' and '''+n2+''' has '''+str(int(r6))+''' '''+i
    o3= n1+''' has '''+str(int(c))+''' '''+i+''' and '''+n2+''' has '''+str(int(d))+''' '''+i
    o4= n1+''' has '''+str(int(r7))+''' '''+i+''' and '''+n2+''' has '''+str(int(r8))+''' '''+i

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
    value = 3#int(input("Enter the option number : "))



    def sol():
        sol=( '''let '''+n1+''' has '''+latex('x')+''' '''+i+'''.
    <br/>Since, '''+n2+''' has '''+latex(str(r2))+''' less '''+i+''' than '''+n1+'''
        <br/>Therefore, '''+n2+''' will have '''+latex('x')+'''-'''+latex(str(r2))+''' '''+i+'''.
    <br/>Since, '''+n1+''' and '''+n2+''' have a total of '''+str(r1)+''' '''+i+'''    
        <br/>=> '''+latex('''x+(x-'''+str(r2)+''')='''+str(r1))+'''  
        <br/>=> '''+latex('''x+x-'''+str(r2)+'''='''+str(r1))+'''    
        <br/>=> '''+latex('''2x-'''+str(r2)+'''='''+str(r1)))

        sol=sol+("<br/>=> "+latex("2x="+str(r1)+"+"+str(r2)))+"\n"
        a=r1+r2
        sol=sol+("<br/>Dividing both the sides by 2")+"\n"    
        sol=sol+("<br/>=> "+latex("x="+to_frac(str(a),"2")))+"\n"
        sol=sol+("<br/>=> "+latex("x="+str(int(a/2))))+"\n"
        sol=sol+("<br/>=> "+latex("x-"+str(r2)+"="+str(int(a/2))+"-"+str(r2)+"="+str(int((a/2-r2)))))+"\n"
        sol=sol+('<br/>Hence, '+n1+' has '+latex(str(int(a/2)))+' '+i+' and '+n2+' has '+latex(str(int((a/2-r2))))+' '+i+' ')

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
    Variation='v3_10',
    Question=question,
    Correct_Answer_1=o3,
    Wrong_Answer_1=o1,
    Wrong_Answer_2=o2,
    Wrong_Answer_3=o4,
    ContributorMail='2018.aaryan.raina@ves.ac.in',
    Solution_text=sol()
    )
    return database_dict


putInCsv('030203',15,main_function,'v3_10')
