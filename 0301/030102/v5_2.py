from PIL import Image,ImageDraw, ImageFont
import random
from coep_package.latex import latex
from coep_package.csv import database_fn, putInCsv

a, b = ( 0, 0)

def changeGlobals():
    global a, b
    a, b = ( random.randint(2, 5)*2, random.randint(2, 5)*2)

def getQuestion():
    return "Are A and B identical in size: A = B?"

def getCorrectAnswer():
    return "Yes" if a == b else "No"

def generate_image():
    imageName = f'030102_C_{a}_{b}.png'

    margin, multiple = 50, 50
    width = margin*3 + multiple*(a+b)
    height = multiple*(a if a > b else b) + margin*3
    img = Image.new( mode="RGB", size = (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    if(a>b):
        a_start_cordinate = (margin,margin)
        a_end_cordinate = (margin + a*multiple, margin + a*multiple)
        b_start_cordinate = (2*margin + a*multiple , margin+((a-b)/2)*multiple)
        b_end_cordinate = (2*margin + a*multiple + b*multiple, b_start_cordinate[1] + b*multiple)
        draw.text((margin + (a_end_cordinate[0] - margin)//2, a_end_cordinate[1] + 50),"A", font=ImageFont.truetype("arial.ttf", size=15), fill="black")
        draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0])//2, a_end_cordinate[1] + 50), "B", font=ImageFont.truetype("arial.ttf", size=15), fill="black")
    else:
        b_start_cordinate = (2*margin + a*multiple , margin)
        b_end_cordinate = (2*margin + a*multiple + b*multiple, margin + b*multiple)
        a_start_cordinate = (margin,margin+((b-a)/2)*multiple)
        a_end_cordinate = (margin + a*multiple, a_start_cordinate[1] + a*multiple)
        draw.text((margin + (a_end_cordinate[0] - margin)//2, b_end_cordinate[1] + 50),"A", font=ImageFont.truetype("arial.ttf", size=15), fill="black")
        draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0])//2, b_end_cordinate[1] + 50), "B", font=ImageFont.truetype("arial.ttf", size=15), fill="black")
    
    #For A circle
    draw.ellipse([a_start_cordinate, a_end_cordinate], fill="red", outline="black", width=1)
    
    #For B circle
    draw.ellipse([b_start_cordinate, b_end_cordinate], fill="green", outline="black", width=1)

    img.save('images/'+imageName)
    
    return 'images/'+imageName

def getWrongAnswers():
    wrong_options = ["No" if a==b else "Yes", "Maybe", "Can't tell!"]
    random.shuffle(wrong_options)
    return wrong_options

def sol():
    is_equal = "equal" if a == b else "not equal"
    answer = "Yes" if a == b else "No"
    return f'Here we have A as a circle of diameter {latex(str(a))} and B as a circle of diameter {latex(str(b))}. Since they are {is_equal}, the correct answer is {answer}.'

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
                        ContributorMail='2019chinmay.thakur@ves.ac.in',
                        Solution_text=solution
                    )

    return database_dict

putInCsv('030102', 5, main_function, __file__)