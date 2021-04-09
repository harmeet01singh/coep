from PIL import Image, ImageDraw, ImageFont
import random
from coep_package.latex import latex
from coep_package.csv import database_fn, putInCsv

weight1 = 0
weight2 = 0
totalWeight = 0

def intValByTen(val):
    return int(val/10)

def changeGlobals():
    global weight1, weight2, totalWeight
    weight1 = random.randint(10, 25)*10
    weight2 = random.randint(1, 10)*10
    totalWeight = random.randint(intValByTen(weight1 + weight2 -10), intValByTen(weight1 + weight2 +10))*10

def getQuestion():
    return "Does the following weight-balance form an equation?"

def getCorrectAnswer():
    return 'Yes' if weight1 + weight2 == totalWeight else 'No'

def getWrongAnswer():
    return 'No' if weight1 + weight2 == totalWeight else 'Yes'

def generateImage():
    imageName = f'030102_W_{weight1}_{weight2}_{totalWeight}.png'

    with Image.open('weight-balance.png') as img:
        draw = ImageDraw.Draw(img)
        draw.text((30, 40), text=str(weight1)+' gm', fill='black', font=ImageFont.truetype("arial.ttf", size=15))
        draw.text((100, 40), text=str(weight2)+' gm', fill='black', font=ImageFont.truetype("arial.ttf", size=15))
        draw.text((295, 40), text=str(totalWeight)+' gm', fill='black', font=ImageFont.truetype("arial.ttf", size=15))
        img.save('images/'+imageName)
    
    return 'images/'+imageName

def sol():
    return f'Since the LHS(Left hand side) of the balance is equal to {weight1} + {weight2} and the weight on RHS(Right hand side) is equal to {totalWeight}. The correct option is {getCorrectAnswer()}'

def main_function():
    changeGlobals()
    question = getQuestion()
    CorrectAnswer1= getCorrectAnswer()
    Wrong_Answer_1 = getWrongAnswer()
    imagePath = generateImage()
    solution = sol()

    database_dict = database_fn(
                        Question_Type='image',
                        Answer_Type='text',
                        Topic_Number='030102',
                        Variation=4,
                        Question=question,
                        Correct_Answer_1=CorrectAnswer1,
                        Wrong_Answer_1=Wrong_Answer_1,
                        Question_IAV=imagePath,
                        ContributorMail='2018.harmeet.kath0da@ves.ac.in',
                        Solution_text=solution
                    )

    return database_dict

putInCsv('030102', 5, main_function, __file__)