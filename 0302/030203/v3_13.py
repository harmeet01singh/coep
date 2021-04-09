import random
from IndianNameGenerator import *
from coep_package.latex import latex
from coep_package.csv_module import database_fn, putInCsv
def main_function():
    name = femaleMarathi()
    given_c = random.randint(5,20)
    left_c = random.randint(10,20)
    total_c = given_c+left_c
    food_capacity = random.randint(100,300)
    amount_grams = food_capacity*total_c
    food_items = ['jam','chocolate', 'ice cream','nutella','cake','candies','pohe']
    food = food_items[random.randint(0,len(food_items)-1)]
    

    ques = f"{name} prepared some {food} at home and filled it in containers. After giving away {latex(given_c)} of the containers to her friends,she still has {latex(left_c)} for herself.\nHow many containers did she fill? If she filled {latex(food_capacity)}g of {food} in each container,what was the total weight of {food} she made? \n"


    options = [None]*4  #creating an empty list to store options


    options[0] =  f"{name} made a total of {latex(total_c)} containers and the total weight of the {food} is {latex(amount_grams)} "
    options[1] = f"{name} made a total of {latex(total_c)} containers and the total weight of the {food} is {latex(amount_grams+food_capacity)}"
    options[2] = f"{name} made a total of {latex(left_c +1+ given_c)} containers and the total weight of the {food} is {latex(amount_grams)}"
    options[3] = f"{name} made a total of {latex(left_c + given_c +1)} containers and the total weight of the {food} is {latex(amount_grams+food_capacity)}"

    options = random.sample(options,len(options))  #shuffiling all the options

    #findig the correct answer index, added a extra space in the correct string
    newOptionList = []     
    for option in options:
        if option[-1] == ' ':
            correct_index = options.index(option)
        else:
            newOptionList.append(option)

    
    solution = f""""
    <br/>Here is the correct detailed solution
    <br/>Let's suppose the total number of containers to be {latex('X')}
    <br/>We know that total containers = containers given + containers left with her
    <br/>That is, {latex('X')} = containers  given + containers left
    <br/>{latex('X')} = {latex(given_c)} + {latex(left_c)}
    <br/>Hence, the total number of containers = {latex(total_c)}
    <br/>As we know that one container contains {latex(food_capacity)} gm of {food}, 
    <br/>Therefore, {latex(total_c)} will contain {latex(total_c)}*{latex(food_capacity)}
    <Hence, the total number of containers is {latex(total_c)} and total weight of {food} is {latex(amount_grams)} grams"""
    Question = ques
    Corr_op = options[correct_index]
    wrong_op1, wrong_op2, wrong_op3 = newOptionList
    Solution = solution

    database_dict= database_fn(
        Answer_Type='1',
        Topic_Number='030202',
        Variation=v3_13,
        Question=Question,
        Correct_Answer_1=Corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        ContributorMail='2019aditya.dubey@ves.ac.in',
        Solution_text=Solution
    )
    return database_dict
putInCsv(
    Topic_Number='030202',
    Number_Of_Iterations=20,
    Main_Function=main_function,
    Filename="v3_13"
)