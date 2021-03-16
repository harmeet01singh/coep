
from IndianNameGenerator import *
import random



n1=randomMarathi()
n2=randomMarathi()

r2 = random.randint(2, 10)

        
r1 = random.randint(10, 40)
r1=r1*(r2+1)

#option 4
c=(r1)/(r2+1)
d=c*r2

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
    
r6 = r2*r5 

#option 3
r7 = (r1)/(r2+1)
r8 = r7*r2

items= ['Apples', 'books', 'pens', 'sheets', 'toys', 'candies', 'pencils', 'shirts', 'pants', 'T-shirts', 'Jackets', 'Bananas', 'chocolates', 'Watermelons', 'Cookies', 'lollipops', 'balls']

i= random.choice(items)

print( n1+' and '+n2+' have a total of '+str(r1)+' ',i,'.')

r=random.randint(1,5)
if r>3:
        n1,n2=n2,n1
        
print('If '+n2+' has '+str(r2)+' times the ',i,' that '+n1+' has, how many ',i,' does each one have?\n')

op=["","","",""]
sq=[0,1,2,3]

#option variables
o1= n1+''' has '''+str(int(r3))+''' '''+i+''' and '''+n2+''' has '''+str(int(r4))+''' '''+i
o2= n1+''' has '''+str(int(r5))+''' '''+i+''' and '''+n2+''' has '''+str(int(r6))+''' '''+i
o3= n1+''' has '''+str(int(c))+''' '''+i+''' and '''+n2+''' has '''+str(int(d))+''' '''+i
o4= n1+''' has '''+str(int(r8))+''' '''+i+''' and '''+n2+''' has '''+str(int(r7))+''' '''+i

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
    print( '''let '''+n1+''' has x''',i,'''.
Since, '''+n2+''' has '''+str(r2)+''' times the ''',i,''' that '''+n1+''' has
    Therefore, '''+n2+''' will have '''+str(r2)+'''*x ''',i,'''.
Since, '''+n1+''' and '''+n2+''' have a total of '''+str(r1)+''' ''',i,'''
    => x+('''+str(r2)+'''*x)='''+str(r1)+''' 
    => x + '''+str(r2)+'''*x ='''+str(r1))
    print("    => (",(r2+1),")* x=",r1)
    a=r2+1
    print("Dividing both the sides by ",a)    
    print("    => x=",r1,"/","",a)
    print("    => x=" ,int(r1/a))
    print("    => ("+str(r2)+")*x=(",r2,")*",int(r1/a),"=",int((r1/a)*r2))
    print('Hence, '+n1+' has '+str(int(r1/a))+'',i,'and '+n2+' has '+str(int((r1/a)*r2))+' ',i,' ')



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


