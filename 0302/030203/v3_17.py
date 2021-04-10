import random
from IndianNameGenerator import *
from coep_package.latex import latex
from coep_package.csv_module import database_fn, putInCsv

r1 = random.randint(10,25) #r1 is the no. of years
r2 = random.randint(1,6) #r2 is no. of times Kanwar was elder.
r3 = random.randint(1,15) #r3 is no. of years before

def getWrongAnswers():
    c = (r1 * r3) + r2 #option 1
    e = (r1 + r2) * r3 #option 3
    f = (r1 + r3) * r2 #option 4
    options= [c,e,f]
    return random.shuffle(options)

def main_function():
    n1 = maleMarathi()
    n2 = femaleMarathi()
    mapping = {n1: 'He', n2: 'She'}
    name = random.choice([n1, n2])
    
    r1 = random.randint(10,25) #r1 is the no. of years
    r2 = random.randint(1,6) #r2 is no. of times Kanwar was elder.
    r3 = random.randint(1,15) #r3 is no. of years before
    c = (r1 * r3) + r2 #option 1
    e = (r1 + r2) * r3 #option 3
    f = (r1 + r3) * r2 #option 4

    item = ['bajra', 'wheat', 'jawar', 'maize', 'rice', 'lentils']
    cop= random.choice(item)
  
    def getQuestion():
        # ques="After "+str(r1)+" years, "+str(n1)+"  shall be "+str(r3)+"  times as old as he was "+str(r3)+" years ago. Find "+mapping[name]+" present age. "
        # return ques
        ques= name+ " bought some kilograms of "+(cop)+". "+mapping[name]+" requires "+latex(str(r1))+ latex("kg ")+ "per month and "+mapping[name]+" got enough "+(cop)+" milled for "+latex(str(r2))+" months. After that "+ mapping[name]+" had "+latex(str(r3))+latex("kg ")+" left. How much "+(cop)+" had "+name+" bought altogether?"
        return ques
    question= getQuestion()
    corr = (r1 * r2) + r3
    CorrectAnswer1= corr
    Wrong_Answer_1, Wrong_Answer_2, Wrong_Answer_3= [c,e,f]

    sol='Let the amount of '+cop+' bought by '+name+' be' +latex(' x.') +'<br>'+ 'Hence,'  +'<br>'+ latex('x-(')+latex(str(r1))+ '*' + latex(str(r2)) + '=' + latex(str(r3))+')' +'<br>'+ latex('x  - ') + latex(str(r1 * r2)) + ' = ' + latex(str(r3)) +'<br>'+ latex('x') + ' = ' + latex(str((r1 * r2) + r3)) + latex('kg ') +'<br>'+ ' Hence, ' + name + ' had bought ' + latex(str((r1 * r2) + r3)) + latex('kg ')+cop+' altogether.'


    
    database_dict = database_fn(Answer_Type= 'text',
                                Topic_Number= '0302',
                                Variation= 17,
                                Question=question,
                                Correct_Answer_1=CorrectAnswer1,
                                Wrong_Answer_1=Wrong_Answer_1,
                                Wrong_Answer_2=Wrong_Answer_2,
                                Wrong_Answer_3=Wrong_Answer_3,
                                ContributorMail= '2019nidhi.jain@ves.ac.in',
                                Solution_text= sol
                                )
    return database_dict
    

putInCsv('030203',10, main_function, 'v17_1', Remove_Duplicates=True, Create_Textfile=True)
