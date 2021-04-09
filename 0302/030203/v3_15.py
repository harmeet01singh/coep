from coep_package.csv import putInCsv,database_fn
from coep_package.latex import latex,to_frac
from IndianNameGenerator import *
import random
def main_function():
        n1=randomMarathi()

        r2 = random.randint(1, 35)
        
        r1 = random.randint(40, 100)

        #option1
        p1 = (r1+r2+1)

        # option 2 
        p2=(r1+r2)

        #Option 3
        p3= abs(r1-r2)

        #option 4
        p4= abs(r1-r2-1)


        
        items= ['Sheeps', 'books', 'pens', 'sheets', 'toys', 'candies', 'pencils', 'shirts', 'pants', 'T-shirts', 'Jackets', 'Bananas', 'chocolates', 'Watermelons', 'Cookies']

        i= random.choice(items)

        temp1 = n1 + ' has some '+ i +'. '+ n1 +' sells ' + str(r2) + ' of them in the market and left with ' + str(r1) +' '+ i

        r=random.randint(1,5)

        temp2 = ' How many '+ i + ' '+ n1 + ' had initially ?.\n'
           
        question=temp1+temp2

        print(question)
     

        op=["","","",""]
        sq=[0,1,2,3]
        #option variables
        o1= n1+''' had '''+str(int(p1))+''' '''+i
        o2= n1+''' had '''+str(int(p4))+''' '''+i
        o3= n1+''' had '''+str(int(p2))+''' '''+i
        o4= n1+''' had '''+str(int(p3))+''' '''+i

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

        """
        If we want solution using two variables then solution will be as follows 

        def sol():
        print('let',i,'sold in the market = x.\n' 'Total ' ,i, 'initially = y.')
        print('X + '+ str(r1) + ' = y.') 
        a = r2+r1
        print('y=',a)
        """

        def sol():
                sol = ('''Let us assume that the number of ''' + i +  ''' with ''' + n1 + ''' at first be '''+ latex('x')+ '<br/>' + n1 + ' sold ' + latex(str(r2)) + i + ' and left with ' + latex(str(r1)) + i +'<br/>'+' Number of ' + i + ' left = ' ' Number of ' + i + ' initially - ' ' Number of ' + i + ' sold at the market '+'<br/>' +' Therefore,' + latex('x -'  + str(r2) + ' = ' + str(r1)) + ' ' + '<br/>' + latex('x - ' + str(r2) + ' + '+  str(r2) + ' = ' + str(r1) + ' + ' + str(r2)) + '   (Add ' + latex(str(r2)) + ' to both sides)')
                a = r1 + r2
                str1 = ' x + 0 =' + str (a)
                str2 = ' x = ' + str (a)
                sol = sol + '<br/>'+latex(str(str1))
                sol = sol + '<br/>'+latex(str(str2))
                sol = sol + '<br/> Thus, there were ' + latex(str(a)) + ' ' + i + ' with ' + n1 + ' at first'
                return sol


        if value==ra+1:
                print("\nYour answer is Correct!")
                print("********** SOLUTION **********")
                sol()
        elif value!=ra+1 and value<5 and value>0:
                print("\nYour answer is incorrect!")
                print("********** SOLUTION **********")
                sol()
        else :
                print("invalid choice!..")


        database_dict= database_fn(
        Answer_Type='v3_15',
        Topic_Number='030203',
        Variation=7,
        Question=question,
        Correct_Answer_1=o3,
        Wrong_Answer_1=o1,
        Wrong_Answer_2=o2,
        Wrong_Answer_3=o4,
        ContributorMail='2019ajay.kachhela@ves.ac.in',
        Solution_text=sol()
        )
        return database_dict


putInCsv(
    Topic_Number='030203',
    Number_Of_Iterations=18,
    Main_Function=main_function,
    Filename='v3_15')




