from coep_package.latex import latex
from coep_package.csv_module import database_fn, putInCsv

# A total of $10000 is distributed among 150 persons as gift. A gift is either of $50 or $100. 
# Find the number of gifts of each type.

import random

#x = int((total - v2*people)/(v1 - v2)) due to this expression 
# sometimes (v1-v2) was becoming negative 
# or 
# sometimes (total-v2*people) was becoming negative
# So I introduced while loop which will make sure (v1-v2) and (total-v2*people) stays positive all the time.

#print(v1,v2)

#print(total, item, people, v1, v2)

#if choice == corr:
#    print('Your answer is correct!')
    #soln(total, item, people, v1, v2)
#elif choice in [1,2,3,4]:
#    print('Your answer is incorrect!')
#    print('The correct answer is option', corr)
#    print('-------- SOLUTION----------')
#    soln(total, item, people, v1, v2)
#else:
#    print("Invalid input")

def main_function():
    
    total_set = [10000, 20000, 30000, 40000, 50000,80000,100000]
    
    people_set = [150,200,250,300,400,500,600]

    dist_set = [50, 100,150,200,500,1000]

    v1,v2=0,0
    while(v1<=v2 or total<=v2*people or v1*people < total or (total - v2*people)%(v1 - v2) != 0):
        v1,v2 = random.choices(dist_set, k=2)
        total = random.choice(total_set)
        people = random.choice(people_set)

    item_set = ['gift', 'prize', 'coupon']
    item = random.choice(item_set)
    
    def get_question():
        q = "A total of " + latex("Rs") + " " +latex(str(total)) + " is distributed among " + latex(str(people)) + " persons as " + item +"s" + ". A " + str(item) + " is either of " + latex("Rs") + " " + latex(str(v1)) + " or " + latex("Rs") + " " + latex(str(v2)) + ". Find the number of " + item +"s" + " of each type."
        return q

    def soln():
        sol1 = "Total number of " + item + "s" + " = " + latex(str(people)) + '<br>' + " Let the number of " + item + "s of " + latex("Rs") + ' ' + latex(str(v1)) + ' ' + " be " + latex("x") + "." + "<br>" + "Then the number of " + item + 's of ' + latex("Rs") + ' ' + latex(str(v2)) + ' is ' + latex(str('(' + str(people) + " - x" + ")" ))  + '<br>' 
        sol1 = sol1 + ' Amount spent on ' + latex('x') + ' ' +item +'s' + " of " + latex("Rs") + " " + latex(str(v1)) + " = " + latex("Rs") + " " + latex(str(v1) + "x") + "<br>"
        sol1 = sol1 + " Amount spent on " + latex(str("(" + str(people) + " - x" + ")")) + ' ' + item + 's' + ' of ' + latex("Rs") + ' ' + latex(str(v2)) + " = " + latex("Rs") + ' ' + latex(str(str(v2) + "(" + str(people) + " - x" + ")")) + "<br>"
        sol1 = sol1 + " Total amount spent for " + item + 's = ' + latex("Rs") + ' ' + latex(str(total)) + '<br>'  
        sol1 = sol1 + " According to the question, " + '<br>'
        sol1 = sol1 + latex(str(str(v1) + "x")) + " + " + latex(str(v2)) + latex(str( "(" + str(people) + '- x' + ')')) + ' = ' + latex(str(total)) + "<br>"
        sol1 = sol1 + " => " + latex(str(str(v1) + "x"))  + " + " + latex(str((v2*people))) + " - " + latex(str(str(v2) +"x ")) + " = " + latex(str(total)) + "<br>"
        sol1 = sol1 + " => " + latex(str(str(v1-v2) + 'x')) + ' = ' + latex(str(total)) + ' - ' + latex(str(v2*people)) + "<br>"
        sol1 = sol1 + " => " + latex(str(str(v1-v2) + 'x')) + ' = ' + latex(str(total - v2*people)) +  "<br>" + '=>' + latex('x') + ' = ' + latex(str(str(total - v2*people) + "/" + str(v1-v2))) + "<br>"
        sol1 = sol1 + " => " + ' ' + latex('x') + ' = ' + latex(str(int((total - v2*people)/(v1 - v2)))) + "<br>"
        sol1 = sol1 + " => " + latex(str(str(people) + '- x')) + ' = ' + latex(str(people)) + ' - ' + latex(str(x))  + ' = ' + latex(str(people-x)) + "<br>"
        return sol1  

    x = int((total - v2*people)/(v1 - v2))
    solution = soln()

    a = latex(x) + " , " +latex(str(people-x))
    b = latex(str(x-10)) +  " , " + latex(str(people-x+15))
    c = latex(str(x-10)) +  " , " + latex((people-x+10))
    d = latex(str(x-5)) +  " , " + latex(str(people-x+5))

    def correctans():
        return a

    correct_answer_1 = correctans()
    wrong_answer_1, wrong_answer_2, wrong_answer_3 = [b,c,d]
    
    question = get_question()

    database_dict = database_fn(Question_Type='text', 
                                Answer_Type='text', 
                                Topic_Number= '0302', 
                                Variation=16,
                                Question=question,
                                Correct_Answer_1=correct_answer_1,
                                Wrong_Answer_1=wrong_answer_1,
                                Wrong_Answer_2=wrong_answer_2,
                                Wrong_Answer_3=wrong_answer_3,
                                ContributorMail='2019raghuttam.parvatikar@ves.ac.in',
                                Solution_text=solution
                                )
    return database_dict

putInCsv('030203',10,main_function,'v16_1',Remove_Duplicates=True, Create_Textfile=True)
