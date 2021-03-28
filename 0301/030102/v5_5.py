from PIL import Image, ImageDraw, ImageFont
import random
from coep_package.latex import latex
from coep_package.csv import database_fn, putInCsv

triangleSelector1, triangleSelector2 = ( 0, 0)

def changeGlobals():
    global triangleSelector1, triangleSelector2
    triangleSelector1 = random.randint(2, 7)
    triangleSelector2 = random.randint(triangleSelector1-1, triangleSelector1+1)

def getQuestion():
    return "Are A and B identical in size and orientation: A = B?"

def getCorrectAnswer():
    return "Yes" if triangleSelector1 == triangleSelector2 else "No"

def generate_image():
    imageName = f'030102_T_{triangleSelector1}_{triangleSelector2}.png'

    width = 500
    height = 500
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    size = selectTriangle1()
    x1, y1, x2, y2, x3, y3 = size
    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=(255, 0, 0), outline='black')
    draw.text((150, 425), "A",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")
    size = selectTriangle2()
    x1, y1, x2, y2, x3, y3 = size
    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill='yellow', outline='black')
    draw.text((350, 425), "B",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    img.save('images/' + imageName)
    return 'images/' + imageName

def selectTriangle1():
    equilateral1 = [150, 70, 100, 300, 200, 300]
    equilateral2 = [100, 70, 150, 300, 200, 70]

    normal1 = [175, 70, 75, 250, 225, 250]
    normal2 = [75, 70, 175, 250, 225, 70]

    rightAngled1 = [60, 70, 60, 300, 175, 300]
    rightAngled2 = [175, 70, 60, 300, 175, 300]
    rightAngled3 = [60, 70, 175, 300, 175, 70]
    rightAngled4 = [60, 70, 60, 300, 175, 70]

    if triangleSelector1 == 1:
        return equilateral1
    elif triangleSelector1 == 2:
        return equilateral2
    elif triangleSelector1 == 3:
        return normal1
    elif triangleSelector1 == 4:
        return normal2
    elif triangleSelector1 == 5:
        return rightAngled1
    elif triangleSelector1 == 6:
        return rightAngled2
    elif triangleSelector1 == 7:
        return rightAngled3
    elif triangleSelector1 == 8:
        return rightAngled4


def selectTriangle2():
    equilateral1 = [350, 70, 300, 300, 400, 300]
    equilateral2 = [300, 70, 350, 300, 400, 70]

    normal1 = [375, 70, 275, 250, 425, 250]
    normal2 = [275, 70, 375, 250, 425, 70]

    rightAngled1 = [260, 70, 260, 300, 375, 300]
    rightAngled2 = [375, 70, 260, 300, 375, 300]
    rightAngled3 = [260, 70, 375, 300, 375, 70]
    rightAngled4 = [260, 70, 260, 300, 375, 70]

    if triangleSelector2 == 1:
        return equilateral1
    elif triangleSelector2 == 2:
        return equilateral2
    elif triangleSelector2 == 3:
        return normal1
    elif triangleSelector2 == 4:
        return normal2
    elif triangleSelector2 == 5:
        return rightAngled1
    elif triangleSelector2 == 6:
        return rightAngled2
    elif triangleSelector2 == 7:
        return rightAngled3
    elif triangleSelector2 == 8:
        return rightAngled4


def getWrongAnswers():
    wrong_options = ['Yes' if triangleSelector1 == triangleSelector2 else 'No', 'Maybe', "Can't Tell"]
    random.shuffle(wrong_options)
    return wrong_options

def sol():
    is_equal = "equal" if triangleSelector1 == triangleSelector2 else "not equal"
    answer = "Yes" if triangleSelector1 == triangleSelector2 else "No"
    return f'Since A and B are {is_equal} in size and orientation, the correct answer is {answer}.'

def main_function():
    changeGlobals()
    question = getQuestion()
    Correct_Answer_1= getCorrectAnswer()
    Wrong_Answer_1, Wrong_Answer_2, Wrong_Answer_3 = getWrongAnswers()
    imagePath = generate_image()
    solution = sol()

    database_dict = database_fn(Answer_Type='text',
                        Topic_Number='030102',
                        Variation=5,
                        Question=question,
                        Correct_Answer_1=Correct_Answer_1,
                        Wrong_Answer_1=Wrong_Answer_1,
                        Wrong_Answer_2=Wrong_Answer_2,
                        Wrong_Answer_3=Wrong_Answer_3,
                        Question_IAV=imagePath,
                        ContributorMail='2019yash.kumthekar@ves.ac.in',
                        Solution_text=solution
                    )

    return database_dict

putInCsv('030102', 5, main_function, __file__)