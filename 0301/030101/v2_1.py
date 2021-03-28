from IndianNameGenerator import *
import random
from coep_package.latex import latex
from coep_package.csv import database_fn, putInCsv


n1 = maleMarathi()
n2 = femaleMarathi()
item = random.choice([ 'books', 'flowers', 'bottles', 'plates', 'spoons', 'pencils', 'erasers', 'staplers', 'sharperners', 'rulers', 'pens', 'brushes', 'crayons'])

#def sol():
    
def getQuestion():
    ques=str(n1)+" is having same number of "+str(item)+" as "+str(n2)+ " has. Each one of them is having how many "+str(item)+"? "
    return ques
 



def getWrongAnswers():
    options = [latex(random.randint(0,4)), latex(random.randint(5,7)),latex(random.randint(8,10)) ]
    random.shuffle(options)
    return options


def main_function():
    arr1=['a','b','c','m','n',"x","y",'z']
    variable= latex(random.choice(arr1)) 
    solu= "\n-----------------SOLUTION--------------------- \n Since we do not know the exact number of "+str(item)+" with "+str(n1)+" and "+str(n2)+" let us use letter "+str(variable)+" to represent unknown quantity of "+str(item)+" with "+str(n1)
    solu=solu+" and since " +str(n2)+" holds equal no. of "+str(item)+" we can represent number of "+str(item)+" with her again as "+str(variable)+"."
    question= getQuestion()
    CorrectAnswer1= variable
    Wrong_Answer_1, Wrong_Answer_2, Wrong_Answer_3= getWrongAnswers()
    


    database_dict = database_fn(Answer_Type= 'text',
                                Topic_Number= '030101',
                                Variation= 2,
                                Question=question,
                                Correct_Answer_1=CorrectAnswer1,
                                Wrong_Answer_1=Wrong_Answer_1,
                                Wrong_Answer_2=Wrong_Answer_2,
                                Wrong_Answer_3=Wrong_Answer_3,
                                ContributorMail= '2018.shubhra.jena@ves.ac.in',
                                Solution_text= solu
                                )
    return database_dict

putInCsv('030101', 10, main_function, 'v2_1')
