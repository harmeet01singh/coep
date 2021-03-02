from IndianNameGenerator import *
import random

n1=randomMarathi()
n2=randomMarathi()

r2 = random.randint(1, 20)
if r2%2!= 0:
        r2=r2+1

r1 = random.randint(30, 100)
if r1%2!= 0:
        r1=r1+1

#x-34=176-34
#option 4
c=(r1-r2)/2
d=c+r2

#option 1
r3 = random.randint(22, 50)
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
    
r6 = r5+r2

#option 3
r7 = d
r8 = c

items= ['Apples', 'books', 'pens', 'sheets', 'toys', 'candies', 'pencils', 'shirts', 'pants', 'T-shirts', 'Jackets', 'Bananas', 'chocolates', 'Watermelons', 'Cookies'  ]

i= random.choice(items)

print( n1+' and '+n2+' have a total of '+str(r1)+' ',i,'.')

r=random.randint(1,5)
if r>3:
        n1,n2=n2,n1
        
print('If '+n2+' has '+str(r2)+' more ',i,' than '+n1+', how many ',i,' does each one have?\n')

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
value = int(input("Enter the option number : "))

def sol():
    print( '''let us assume '''+n1+''' has x''',i,'''.
Since, '''+n2+''' has '''+str(r2)+''' more ''',i,''' than '''+n1+'''
    Therefore, '''+n2+''' will have x+'''+str(r2)+''' ''',i,'''.
Since, '''+n1+''' and '''+n2+''' have a total of '''+str(r1)+''' ''',i,'''
    => x+(x+'''+str(r2)+''')='''+str(r1)+''' 
    => x+x+'''+str(r2)+'''='''+str(r1)+'''     
    => 2x+'''+str(r2)+'''='''+str(r1))

    print("    => 2x =",r1,"-",r2)
    a=r1-r2
    print("Dividing both the sides by 2")
    print("    => x=",a,"/","2")
    print("    => x=",int(a/2))
    print("    => x+"+str(r2)+"=",int(a/2),"+",r2,"=",int((a/2+r2)))
    print('Hence, '+n1+' has '+str(int(a/2))+'',i,'and '+n2+' has '+str(int((a/2+r2)))+' ',i,' ')


      
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
