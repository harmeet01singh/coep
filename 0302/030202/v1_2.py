import random as rd
from typing import Text
from coep_package.latex import latex
from coep_package.csv import database_fn, putInCsv

def ageSolution():
    global solutionText
    print("Let the initial age be $x$.<br>The current age is {} years, and initial age to be found was {} years ago is $x$.<br>Therefore we can write the equation as $x + {} = {}$<br>By subtracting {} from both sides<br>We get the equation as $x + {} - {} = {} - {}$.".format( rhsConst,lhsConst, lhsConst, rhsConst, lhsConst, lhsConst, lhsConst, rhsConst, lhsConst))
    solutionText ="Let the initial age be $x$.<br>The current age is {} years, and initial age to be found was {} years ago is $x$.<br>Therefore we can write the equation as $x + {} = {}$<br>By subtracting {} from both sides<br>We get the equation as $x + {} - {} = {} - {}$.".format( rhsConst,lhsConst, lhsConst, rhsConst, lhsConst, lhsConst, lhsConst, rhsConst, lhsConst)

def timeSolution():
    global solutionText
    print("Let the current time left be $x$.<br>The initial time was {} {} and {} {} were spent.<br>Therefore we can write the equation as $x + {} = {}$<br>By subtracting {} from both sides<br>We get the equation as $x + {} - {} = {} - {}$.".format(rhsConst, selectedTimeWord, lhsConst, selectedTimeWord, rhsConst, lhsConst, rhsConst, lhsConst, lhsConst, lhsConst, rhsConst, lhsConst))
    solutionText ="Let the current time left be $x$.<br>The initial time was {} {} and {} {} were spent.<br>Therefore we can write the equation as $x + {} = {}$<br>By subtracting {} from both sides<br>We get the equation as $x + {} - {} = {} - {}$.".format(rhsConst, selectedTimeWord, lhsConst, selectedTimeWord, rhsConst, lhsConst, rhsConst, lhsConst, lhsConst, lhsConst, rhsConst, lhsConst)

def nounSolution():
    global solutionText
    print("Let the current number of items be $x$.<br>The initial amount of items before {} items were {} is {}.<br>Therefore we can write that as $x + {}={}$ <br>By subtracting {} on both sides<br>We get the equation as $x + {} - {} = {} - {}$.".format(lhsConst, solutionWord, rhsConst, lhsConst, rhsConst, lhsConst,lhsConst, lhsConst, rhsConst, lhsConst))
    solutionText ="Let the current number of items be $x$.<br>The initial amount of items before {} items were {} is {}.<br>Therefore we can write that as $x + {}={}$ <br>By subtracting {} on both sides<br>We get the equation as $x + {} - {} = {} - {}$.".format(lhsConst, solutionWord, rhsConst, lhsConst, rhsConst, lhsConst,lhsConst, lhsConst, rhsConst, lhsConst)

def printSolution():
   #answer = rhsConst - lhsConst
    #print("Solution : ")
    #print("Let the initial number of items be x.")
    #print("Therefore, the equation will be: x + {} = {}".format(lhsConst, rhsConst))
    #print("By subtracting {} from both sides of the equation, we get:".format(lhsConst))
    #print("x + {} - {} = {} - {} <br>".format(lhsConst, lhsConst, rhsConst, lhsConst))
    #print("Therefore x = {} is the correct answer".format(answer))
    print("Solution : ")
    if(questionType == 1):
        nounSolution()
    elif(questionType == 2):
        ageSolution()
    else:
        timeSolution()


def getAnswerInput(shuffledOptions):
    
    while(1):
        optionSelected = int(input("Enter your answer : "))
        if(optionSelected > 0 and optionSelected <5):
            break
        else:
            print("INVALID INPUT! PLEASE ENTER ANSWER BETWEEN 1 TO 4")

    if ( "$ x + {} - {} = {} - {} $".format(lhsConst, lhsConst,rhsConst,lhsConst) == shuffledOptions[optionSelected-1]):
        print("That is the correct answer!<br>")
    else:
        print("Incorrect answer!<br>")

    printSolution()
    
        
def printOptions(shuffledOptions):
    print("Options : ")
    print("1) {}".format(shuffledOptions[0]))
    print("2) {}".format(shuffledOptions[1]))
    print("3) {}".format(shuffledOptions[2]))
    print("4) {}".format(shuffledOptions[3]))
    
    getAnswerInput(shuffledOptions)


def generateOptions():
    global correctAnswer1
    global wrongAnswer1
    global wrongAnswer2
    global wrongAnswer3
    
    options = ["$ x + {} + {} = {} + {} $".format(lhsConst, lhsConst,rhsConst,lhsConst),
               "$ x + {} - {} = {} - {} $".format(lhsConst, lhsConst,rhsConst,lhsConst),
               "$ (x + {}) \\times {} = {} \\times {} $".format(lhsConst, lhsConst,rhsConst,lhsConst),
               "$(x + {}) \div {} = {} \div {} $".format(lhsConst, lhsConst,rhsConst,lhsConst)]

    correctAnswer1 = options[1]
    wrongAnswer1 = options[0]
    wrongAnswer2 = options[2]
    wrongAnswer3 = options[3]
    rd.shuffle(options)
    printOptions(options)


#def generateOptions():
#    options = [rhsConst + lhsConst , abs(rhsConst - lhsConst), (rhsConst % lhsConst) + 10, round((lhsConst*rhsConst)/10), ]

#    correctAnswerPosition = rd.randint(0,3)
#    shuffledOptions = [1,2,3,4]
#    #shuffledOptions = [0,1,2,3]
#    shuffledOptions[correctAnswerPosition] = abs(rhsConst - lhsConst)
#    positionsDone = [correctAnswerPosition]

#    for i in range(0,3):
#        while (1):
#            position = rd.randint(0,3)
#            if (not (position in positionsDone)):
#                break
    
#        positionsDone.insert(i,position)
#        shuffledOptions[position] = options[i]
        
#    printOptions(shuffledOptions,correctAnswerPosition)
    

def generateQuestion():
    global questionType
    global solutionWord
    global selectedTimeWord
    global question
    
    itemHolder = ["Sristi", "Nidhi", "Shanti", "Sushma", "Bhavya", "Ali", "Thomas", "Aditya", "Karan", "Arujun", "Ram", "Kabir", "Sita", "Mary"]
    giveableItems = ["apples", "mangos", "onions", "tomatoes", "chocolates", "bags", "tickets", "chairs", "flowers"]
    lendableItems = ["rupees", "pens", "pencils", "books", "laptops", "balls", "sanitizers", "soaps","suits", "shoes"]
    lostItems = ["bottles", "bags", "pages", "shirt buttons", "hair bands", "bracelets", "pen caps", "masks"]
    timeFrames = ["months","days","Hours","age"]
    activites = ["fasting","training","researching","travling","on a cruise","camping"]
    activitesHours = ["gaming","eating","playing","watching sports","Shopping","studying","cleaning","cooking","working"]
    
    listsOfItems = [giveableItems, lendableItems, lostItems,timeFrames]
    selectedList = listsOfItems[rd.randint(0,3)]
    
    selectedItem = selectedList[rd.randint(0,len(selectedList)-1)]
    selectedItemHolder = itemHolder[rd.randint(0,len(itemHolder)-1)]

    if(selectedItem in lostItems):
        questionType = 1
        solutionWord = "lost"
        print("{} had {} {} before {} lost {}. Select the correct statement from below.<br>Let $x$ be the number of {} after {} lost them".format(selectedItemHolder,rhsConst,selectedItem,selectedItemHolder,lhsConst,selectedItem,selectedItemHolder))
        question = "{} had {} {} before {} lost {}. Select the correct statement from below.<br>Let $x$ be the number of {} after {} lost them".format(selectedItemHolder,rhsConst,selectedItem,selectedItemHolder,lhsConst,selectedItem,selectedItemHolder)

    
    elif(selectedItem in giveableItems):
        questionType = 1
        solutionWord = "given"
        while(1): # ensures second item holder to not be the same as the first
            secondItemHolder = itemHolder[rd.randint(0,len(itemHolder)-1)]
            if(secondItemHolder != selectedItemHolder):
                break
        print("{} had {} {} before giving {} {} to {}. Select the correct statement from below.<br>Let $x$ be the number of {} after {} gave them to {}".format(selectedItemHolder, rhsConst, selectedItem, lhsConst, selectedItem, secondItemHolder, selectedItem, selectedItemHolder, secondItemHolder)) 
        question = "{} had {} {} before giving {} {} to {}. Select the correct statement from below.<br>Let $x$ be the number of {} after {} gave them to {}".format(selectedItemHolder, rhsConst, selectedItem, lhsConst, selectedItem, secondItemHolder, selectedItem, selectedItemHolder, secondItemHolder)
    
    elif(selectedItem in lendableItems):
        questionType = 1
        solutionWord = "lent"
        while(1): # ensures second item holder to not be the same as the first
            secondItemHolder = itemHolder[rd.randint(0,len(itemHolder)-1)]
            if(secondItemHolder != selectedItemHolder):
                break
        print("{} had {} {} before lending {} {} to {}. Select the correct statement from below.<br>Let $x$ be the number of {} after {} gave them to {}".format(selectedItemHolder, rhsConst, selectedItem, lhsConst, selectedItem, secondItemHolder, selectedItem, selectedItemHolder, secondItemHolder))
        question = "{} had {} {} before lending {} {} to {}. Select the correct statement from below.<br>Let $x$ be the number of {} after {} gave them to {}".format(selectedItemHolder, rhsConst, selectedItem, lhsConst, selectedItem, secondItemHolder,selectedItem, selectedItem, selectedItemHolder, secondItemHolder)    
    
    elif(selectedItem in timeFrames):
        if(selectedItem == "age"):
            questionType = 2
            #selectedItemHolder + " is " + str(rhsConst) + " years old today. How old was " + selectedItemHolder +" " + str(lhsConst) + " years ago?
            print("{} is {} years old today. How old was {} {} years ago?<br>Let $x$ be the age of {} {} years ago. Select the correct statement below to solve for $x$.".format( selectedItemHolder, rhsConst, selectedItemHolder, lhsConst, selectedItemHolder, lhsConst))
            question = "{} is {} years old today. How old was {} {} years ago?<br>Let $x$ be the age of {} {} years ago. Select the correct statement below to solve for $x$.".format( selectedItemHolder, rhsConst, selectedItemHolder, lhsConst, selectedItemHolder, lhsConst)
        elif(selectedItem == "Hours"):
            questionType = 3
            selectedTimeWord = selectedItem
            #selectedItemHolder + " spent " + str(lhsConst) + " " + selectedItem + " " + activitesHours[rd.randint(0,len(activites)-1)] + " now has " + str(rhsConst) + " left, how much time did " + selectedItemHolder + " have brfore?
            print( "{} had {} hours to complete homework, but {} spent {} hours {}. How many hours are left for {} to complete homework? Select the correct statement from below.<br>Let $x$ be the amount of time {} has now.".format(selectedItemHolder, rhsConst, selectedItemHolder, lhsConst, activitesHours[rd.randint(0,len(activitesHours)-1)], selectedItemHolder, selectedItemHolder) )
            question = "{} had {} hours to complete homework, but {} spent {} hours {}. How many hours are left for {} to complete homework? Select the correct statement from below.<br>Let $x$ be the amount of time {} has now.".format(selectedItemHolder, rhsConst, selectedItemHolder, lhsConst, activitesHours[rd.randint(0,len(activitesHours)-1)], selectedItemHolder, selectedItemHolder) #correct
        else:
            questionType = 3
            selectedTimeWord = selectedItem
            print("{} had {} {} to complete project, but {} spent {} {}. How many {} are left for {} to complete homework? Select the correct statement from below.<br>Let $x$ be the amount of time {} has now.".format(selectedItemHolder, rhsConst, selectedItem,selectedItemHolder, lhsConst, activitesHours[rd.randint(0,len(activitesHours)-1)],selectedItem, selectedItemHolder, selectedItemHolder, rhsConst)) #correct
            question = "{} had {} {} to complete project, but {} spent {} {}. How many {} are left for {} to complete homework? Select the correct statement from below.<br>Let $x$ be the amount of time {} has now.".format(selectedItemHolder, rhsConst, selectedItem,selectedItemHolder, lhsConst, activitesHours[rd.randint(0,len(activitesHours)-1)],selectedItem, selectedItemHolder, selectedItemHolder, rhsConst)

    generateOptions()
    
def main():
    global question, correctAnswer1, wrongAnswer1, wrongAnswer2, wrongAnswer3, solutionText
    global lhsConst, rhsConst
    lhsConst = rd.randint(1,24)
    rhsConst = rd.randint(25,50)
    generateQuestion()
    database_dict = database_fn(Answer_Type='Text', Topic_Number= '030202', Variation=1, Question=question, Correct_Answer_1= correctAnswer1, Wrong_Answer_1= wrongAnswer1, Wrong_Answer_2= wrongAnswer2, Wrong_Answer_3= wrongAnswer3, ContributorMail= '2019sristi.sharma@ves.ac.in', Solution_text= solutionText)
    return database_dict

questionType = 0
solutionWord = ""
selectedTimeWord = ""

# CSV variables
question = ""
correctAnswer1 = ""
wrongAnswer1 = ""
wrongAnswer2 = ""
wrongAnswer3 = ""
solutionText = ""

#lhsConst = rd.randint(1,24)
#rhsConst = rd.randint(25,50)
lhsConst = 0
rhsConst = 0
putInCsv(
    Topic_Number='030202',
    Number_Of_Iterations=10,
    Main_Function=main,
    Filename= 'v1_2'
)





