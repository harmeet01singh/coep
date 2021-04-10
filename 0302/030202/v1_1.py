import random as rd
from typing import Text
from coep_package.latex import latex
from coep_package.csv_module import database_fn , putInCsv


#$ {} - {} $
#$ {} \times {} $
#$ {} \div {} $
#$ {} + {} $

def ageSolution():
    global solutionText
    print("Let the initial age be $x$.<br>The current age after {} years is {}.<br>Therefore we can write the equation as $x + {} = {}$<br>By adding {} from both sides<br>We get the equation as $x + {} + {} = {} + {}$.".format(lhsConst, rhsConst, lhsConst, rhsConst, lhsConst, lhsConst, lhsConst, rhsConst, lhsConst))
    solutionText = "Let the initial age be $x$.<br>The current age after {} years is {}.<br>Therefore we can write the equation as $x + {} = {}$<br>By adding {} from both sides<br>We get the equation as $x + {} + {} = {} + {}$.".format(lhsConst, rhsConst, lhsConst, rhsConst, lhsConst, lhsConst, lhsConst, rhsConst, lhsConst)
    
def timeSolution():
    global solutionText
    print("Let the initial time be $x$.<br>Since {} {} were spent we can write the equation as $x - {}$<br>Since {} {} are left we can write the equation as $x - {} = {}$<br>Adding {} on both sides<br>We get the equation as $x - {} + {} = {} + {}$".format(lhsConst, selectedTimeWord, lhsConst, rhsConst,  selectedTimeWord, lhsConst, rhsConst, lhsConst, lhsConst, lhsConst, rhsConst, lhsConst, lhsConst))
    solutionText = "Let the initial time be $x$.<br>Since {} {} were spent we can write the equation as $x - {}$<br>Since {} {} are left we can write the equation as $x - {} = {}$<br>Adding {} on both sides<br>We get the equation as $x - {} + {} = {} + {}$".format(lhsConst, selectedTimeWord, lhsConst, rhsConst,  selectedTimeWord, lhsConst, rhsConst, lhsConst, lhsConst, lhsConst, rhsConst, lhsConst, lhsConst)
    
def nounSolution():
    global solutionText
    print("Let the initial number of items be $x$.<br>Since {} items were {} we can write that as $x - {}$<br>Since {} items are now left we can write the equation as $x - {} = {}$<br>Add {} on both sides<br>We get the equation as $x - {} + {} = {} + {}$".format(lhsConst, solutionWord, lhsConst, rhsConst, lhsConst, rhsConst, lhsConst, lhsConst, lhsConst, rhsConst, lhsConst, lhsConst))
    solutionText = "Let the initial number of items be $x$.<br>Since {} items were {} we can write that as $x - {}$<br>Since {} items are now left we can write the equation as $x - {} = {}$<br>Add {} on both sides<br>We get the equation as $x - {} + {} = {} + {}$".format(lhsConst, solutionWord, lhsConst, rhsConst, lhsConst, rhsConst, lhsConst, lhsConst, lhsConst, rhsConst, lhsConst, lhsConst)

def printSolution():
    print("Solution : ")
    if(questionType == 1):
        nounSolution()
    elif(questionType == 2):
        ageSolution()
    else:
        timeSolution()
    
def getAnswerInput(correctAnswerPosition):
    optionSelected = int(input("Enter your answer : "))
    if (optionSelected - 1 == correctAnswerPosition):
        print("That is the correct answer!")
    else:
        print("Incorrect answer!")
    printSolution()
        
def printOptions(shuffledOptions,correctAnswerPosition):
    print("Options : ")
    print("1) {}".format(shuffledOptions[0]))
    print("2) {}".format(shuffledOptions[1]))
    print("3) {}".format(shuffledOptions[2]))
    print("4) {}".format(shuffledOptions[3]))
    
    getAnswerInput(correctAnswerPosition)
    
def generateOptions():
    
    global correctAnswer1,wrongAnswer1,wrongAnswer2,wrongAnswer3
    
    options = ["$ x - {} + {} = {} + {} $".format(lhsConst, lhsConst,rhsConst,lhsConst),
               "$ x - {} - {} = {} - {} $".format(lhsConst, lhsConst,rhsConst,lhsConst),
               "$ (x - {}) \\times {} = {} \\times {} $".format(lhsConst, lhsConst,rhsConst,lhsConst),
               "$ (x - {}) \div {} = {} \div {} $".format(lhsConst, lhsConst,rhsConst,lhsConst)]
    
    correctAnswer1 = options[0]
    wrongAnswer1 = options[1]
    wrongAnswer2 = options[2]
    wrongAnswer3 = options[3]
    
    correctAnswerPosition = rd.randint(0,3)
    shuffledOptions = [1,2,3,4]
    shuffledOptions[correctAnswerPosition] = options[0]
    
    positionsDone = [correctAnswerPosition]

    for i in range(1,4):
        while (1):
            position = rd.randint(0,3)
            if (not (position in positionsDone)):
                break
    
        positionsDone.insert(i,position)
        shuffledOptions[position] = options[i]
        
    printOptions(shuffledOptions,correctAnswerPosition)
    
def generateQuestion():
    global questionType
    global solutionWord
    global selectedTimeWord
    global question
    
    itemHolder = ["Sristi", "Nidhi", "Shanti", "Shusma", "Bhavya", "Ali", "Thomas", "Aditya", "Karan", "Arujun", "Ram", "kabir", "Sita", "Mary"]
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
        print("{} lost {} {} now {} has {} {}. Select the correct statement from below to solve for $x$.".format(selectedItemHolder,lhsConst,selectedItem,selectedItemHolder,rhsConst, selectedItem ))
        question = "{} lost {} {} now {} has {} {}. Select the correct statement from below to solve for $x$.".format(selectedItemHolder,lhsConst,selectedItem,selectedItemHolder,rhsConst, selectedItem)
    
    elif(selectedItem in giveableItems):
        questionType = 1
        solutionWord = "given"
        while(1): # ensures second item holder to not be the same as the first
            secondItemHolder = itemHolder[rd.randint(0,len(itemHolder)-1)]
            if(secondItemHolder != selectedItemHolder):
                break
        print("{} gave {} {} to {}, now {} has {} {}. Select the correct statement from below to solve for $x$.".format(selectedItemHolder, lhsConst, selectedItem, secondItemHolder, selectedItemHolder, rhsConst, selectedItem)) 
        question = "{} gave {} {} to {}, now {} has {} {}. Select the correct statement from below to solve for $x$.".format(selectedItemHolder, lhsConst, selectedItem, secondItemHolder, selectedItemHolder, rhsConst, selectedItem)
        
    elif(selectedItem in lendableItems):
        questionType = 1
        solutionWord = "lent"
        while(1): # ensures second item holder to not be the same as the first
            secondItemHolder = itemHolder[rd.randint(0,len(itemHolder)-1)]
            if(secondItemHolder != selectedItemHolder):
                break
        print("{} lent {} {} to {}, now {} has {} {}. Select the correct statement from below to solve for $x$.".format(selectedItemHolder, lhsConst, selectedItem, secondItemHolder, selectedItemHolder, rhsConst, selectedItem))    
        question = "{} lent {} {} to {}, now {} has {} {}. Select the correct statement from below to solve for $x$.".format(selectedItemHolder, lhsConst, selectedItem, secondItemHolder, selectedItemHolder, rhsConst, selectedItem)
        
    elif(selectedItem in timeFrames):
        if(selectedItem == "age"):
            questionType = 2
            print("{} years ago {} was {} years old. Select the correct statement from below to solve for $x$.".format(lhsConst, selectedItemHolder, rhsConst))
            question = "{} years ago {} was {} years old. Select the correct statement from below to solve for $x$.".format(lhsConst, selectedItemHolder, rhsConst)
        elif(selectedItem == "Hours"):
            questionType = 3
            selectedTimeWord = selectedItem
            print("{} spent {} hours {}, now {} has {} hours left. Select the correct statement from below to solve for $x$.".format(selectedItemHolder, lhsConst, activitesHours[rd.randint(0,len(activitesHours)-1)], selectedItemHolder, rhsConst))
            question = "{} spent {} hours {}, now {} has {} hours left. Select the correct statement from below to solve for $x$.".format(selectedItemHolder, lhsConst, activitesHours[rd.randint(0,len(activitesHours)-1)], selectedItemHolder, rhsConst)
        else:
            questionType = 3
            selectedTimeWord = selectedItem
            print("{} spent {} {} {}, now {} has {} {} left. Select the correct statement from below to solve for $x$.".format(selectedItemHolder, lhsConst, selectedItem, activites[rd.randint(0,len(activites)-1)], selectedItemHolder, rhsConst, selectedItem))
            question = "{} spent {} {} {}, now {} has {} {} left. Select the correct statement from below to solve for $x$.".format(selectedItemHolder, lhsConst, selectedItem, activites[rd.randint(0,len(activites)-1)], selectedItemHolder, rhsConst, selectedItem)
            
    generateOptions()

def main():
    global lhsConst, rhsConst
    global question, correctAnswer1, wrongAnswer1, wrongAnswer2, wrongAnswer3, solutionText
    lhsConst = rd.randint(1,50)
    rhsConst = rd.randint(1,50)
    generateQuestion()
    database_dict = database_fn(Answer_Type='Text', Topic_Number= '030202', Variation=1, Question=question, Correct_Answer_1= correctAnswer1, Wrong_Answer_1= wrongAnswer1, Wrong_Answer_2= wrongAnswer2, Wrong_Answer_3= wrongAnswer3, ContributorMail= '2019bhavya.hingorani@ves.ac.in', Solution_text= solutionText)
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

lhsConst = 0
rhsConst = 0
putInCsv(
    Topic_Number='030202',
    Number_Of_Iterations=10,
    Main_Function=main,
    Filename= 'v1_1'
)













