#To be added later
import random
from coep_package.latex import latex
from coep_package.csv import database_fn, putInCsv

container = ''
item = ''
variable = ''

def changeGlobals():
    global container, item, variable
    container = random.choice([ 'container', 'box', 'jar', 'pouch', 'drawer'])
    item = random.choice([ 'pencils', 'erasers', 'staplers', 'sharperners', 'rulers', 'pens', 'brushes', 'crayons'])
    variable = latex(random.choice('abckmnxyz'))

def getQuestion():
    return f"In a {container} there are few {item}. How many {item} are there?"

def getCorrectAnswer():
    return variable

def getWrongAnswers():
    options = [ latex(random.randint(0,10)), latex(random.randint(0,10)), latex(random.randint(0,10)) ]
    random.shuffle(options)
    return options

def sol():
    return f"Since we don't know the exact number of {item} in the {container}. Let us represent the number of {item} with variable '{variable}'"

def main_function():
    changeGlobals()
    question = getQuestion()
    CorrectAnswer1= getCorrectAnswer()
    Wrong_Answer_1, Wrong_Answer_2, Wrong_Answer_3 = getWrongAnswers()
    solution = sol()

    database_dict = database_fn(Answer_Type='text',
                        Topic_Number='030101',
                        Variation='1',
                        Question=question,
                        Correct_Answer_1=CorrectAnswer1,
                        Wrong_Answer_1=Wrong_Answer_1,
                        Wrong_Answer_2=Wrong_Answer_2,
                        Wrong_Answer_3=Wrong_Answer_3,
                        ContributorMail='2018.harmeet.kath0da@ves.ac.in',
                        Solution_text=solution
                    )

    return database_dict

putInCsv('030101', 5, main_function, __file__)