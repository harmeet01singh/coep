from csv_latex.csv import putInCsv,database_fn

#this function generates question
def getQuestion():
    return 'Question'

#this function generates correct option
def getCorrOption():
    return 'correct option'

#this function generates wrong options
def getWrongOptions():
    return ['wrong option 1','wrong option 2','wrong option 3']

#this function generates Solution
def getSolution():
    return 'Solution'


#When this main_function runs 1 time it creates one Question and its solution
def main_function():

    Question = getQuestion()
    Corr_op = getCorrOption()
    wrong_op1,wrong_op2,wrong_op3 = getWrongOptions()
    Solution = getSolution()


    #this database_fn
    #for understanding the parameters used refer to the DST_Lot_2 Excel sheet shared in the Readme file
    #all the attributes mentioned in DST_lot_2 file are implemented in this function.
    database_dict= database_fn(
        Answer_Type='1',
        Topic_Number='01010101',
        Variation='v1',
        Question=Question,
        Correct_Answer_1=Corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        Solution_text=Solution
    )
    return database_dict


#if you want N questions in your csv file pass N as the value for Number of Iteraions
putInCsv(
    Topic_Number='01010101',
    Number_Of_Iterations=10,
    Main_Function=main_function,
    Filename=__file__
)