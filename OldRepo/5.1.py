
import names
import random

n1=names.get_first_name()
n2=names.get_first_name()

r2 = random.randint(1, 20)
r1 = random.randint(30, 100)

r3 = random.randint(1, r1)
r4 = random.randint(1, r1)

r5 = random.randint(1, r1)
r6 = random.randint(1, r1)

r7 = random.randint(1, r1)
r8 = random.randint(1, r1)

print( n1+' and '+n2+' have a total of '+str(r1)+' cakes. If '+n2+' has '+str(r2)+' more cakes than '+n1+', how many cakes does each one have?')
c=(r1-r2)/2
d=c+r2
print(' option 1 : '+n1+' has '+str(r3)+' cakes and '+n2+' has '+str(r4)+' cakes   \n option 2 : '+n1+' has '+str(r5)+' cakes and '+n2+' has '+str(r6)+' cakes \n option 3 : '+n1+' has '+str(r7)+' cakes and '+n2+' has '+str(r8)+' cakes\n option 4 : '+n1+' has '+str(c)+' cakes and '+n2+' has '+str(d)+' cakes\n')

choice = int(input("Enter the option number "))

def sol():
    print( '''let '''+n1+''' and '''+n2+''' have x and y cakes respectively.
    Therefore, according to the question :-
    x+y='''+str(r1)+''' (as '''+n1+''' and '''+n2+''' have a total of '''+str(r1)+''' cakes)

    Also, y='''+str(r2)+'''+x (as '''+n2+''' has '''+str(r2)+''' more cakes than '''+n1+''')
    => x+'''+str(r2)+'''+x='''+str(r1))

    print("    => 2x=",r1,"-",r2)
    a=r1-r2
    print("    => x=",a,"/","2")
    print("    => x=",a/2)
    print("    => y=",a/2,"+",r2)
    print("    => y=",(a/2)+r2)

if choice == 1:
    print('Your answer is incorrect!\n')
    print('-------- SOLUTION----------')
    sol()
elif choice == 2:
    print('Your answer is incorrect!')
    print('-------- SOLUTION----------')
    sol()
elif choice == 3:
    print('Your answer is incorrect!')
    print('-------- SOLUTION----------')
    sol()
elif choice == 4:
    print('Your answer is correct!')
    print('-------- SOLUTION----------')
    sol()
else:
    print("Invalid input")


