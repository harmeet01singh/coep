from IndianNameGenerator import *
import random
from fractions import Fraction



n1=randomMarathi()
n2=randomMarathi()

r2 = random.randint(1, 5)
r9=random.randint(2, 7)
if r2%r9==0:
    r9=r9+1
if r2>r9:
    r2,r9=r9,r2

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

print( n1+' and '+n2+' have a total of '+str(r1)+' litres of',i,'.')

r=random.randint(1,5)
if r>3:
        n1,n2=n2,n1

print('If '+n2+' has',r10,'times the ',i,' that '+n1+' has, how many litres of',i,'does each one have?\n')


op=["","","",""]
sq=[0,1,2,3]
#option variables
o1= n1+''' has '''+str((r3))+''' litres of '''+i+''' and '''+n2+''' has '''+str((r4))+''' litres of '''+i
o2= n1+''' has '''+str((r5))+''' litres of '''+i+''' and '''+n2+''' has '''+str((r6))+''' litres of '''+i
o3= n1+''' has '''+str((c))+''' litres of '''+i+''' and '''+n2+''' has '''+str((d))+''' litres of '''+i
o4= n1+''' has '''+str((r7))+''' litres of '''+i+''' and '''+n2+''' has '''+str((r8))+''' litres of '''+i

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
value = int(input("Enter the option number : "))


#solution function
def sol():
    print( '''let '''+n1+''' has x litres of ''',i,'''.
Since, '''+n2+''' has ''',r10,''' times the ''',i,''' that '''+n1+''' has
    Therefore, '''+n2+''' will have (''',r10,''')*x litres of''',i,'''.  
Since, '''+n1+''' and '''+n2+''' have a total of '''+str(r1)+''' litres of''',i,'''
    x+(''',r10,''')*x='''+str(r1)+'''       
    Taking x common from both the terms in L.H.S :-
    => (1+''',r10,''')*x='''+str(r1))
    print("    => (",(r10+1),")* x =",r1)
    a=r10+1
    print("Dividing both the sides by ",a)    
    print("    => x=",r1,"/","(",a,")")
    print("    => x=" ,(r1/a))
    print("    => (",r10,")*x = (",r10,")*(",(r1/a),")=",((r1/a)*r10))
    print('Hence, '+n1+' has '+str((r1/a))+' litres of',i,'and '+n2+' has '+str(((r1/a)*r10))+' litres of',i,' ')



if value==ra+1:
        print("\nYour answer is Correct!")
        print(">------------- SOLUTION -------------<")
        sol()
elif value!=ra+1 and value<5 and value>0:
        print("\nYour answer is incorrect!")
        print(">------------- SOLUTION --------------<")
        sol()
else :
        print("invalid choice")
