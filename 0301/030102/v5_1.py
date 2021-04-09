from PIL import Image,ImageDraw, ImageFont
import random
from coep_package.latex import latex
from coep_package.csv import database_fn, putInCsv

a, b = ( 0, 0)

def changeGlobals():
    global a, b
    a = random.randint(5, 8)
    b = random.randint(a-2, a+2)

def getQuestion():
    return "Are A and B identical in size: A = B?"

def getCorrectAnswer():
    return "Yes" if a == b else "No"

def generate_image():
    imageName = f'030102_S_{a}_{b}.png'

    margin, multiple = 50, 50
    width = margin*3 + multiple*(a+b)
    height = multiple*(a if a > b else b) + margin*3
    img = Image.new( mode="RGB", size = (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    #For A matrix
    a_start_cordinate = (margin, margin)
    a_end_cordinate = (margin + a*multiple, margin + a*multiple)
    draw.rectangle([a_start_cordinate, a_end_cordinate], fill="red", outline="black", width=1)
    for i in range(1,a):
        draw.line([margin + i*multiple , margin, margin + i*multiple , margin + a*multiple], fill="black", width=1)     #Vertical Lines
        draw.line([margin , margin + i*multiple, margin + a*multiple , margin + i*multiple], fill="black", width=1)     #Horizontal Lines
    draw.text((margin + (a_end_cordinate[0] - margin)//2, a_end_cordinate[1] + 50),"A", font=ImageFont.truetype("arial.ttf", size=15), fill="black")
    
    #For B matrix
    b_start_cordinate = (2*margin + a*multiple , margin)
    b_end_cordinate = (2*margin + a*multiple + b*multiple, margin + b*multiple)
    draw.rectangle([b_start_cordinate, b_end_cordinate], fill="green", outline="black", width=1)
    for i in range(1,b):
        draw.line([b_start_cordinate[0] + i*multiple , margin, b_start_cordinate[0]+ i*multiple , margin + b*multiple], fill="black", width=1)      #Vertical Lines
        draw.line([b_start_cordinate[0] , b_start_cordinate[1] + i*multiple, b_end_cordinate[0] , b_start_cordinate[1] + i*multiple], fill="black", width=1)     #Horizontal Lines
    draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0])//2, b_end_cordinate[1] + 50), "B", font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    #Display Image
    img.save('images/' + imageName, format="PNG")
    return 'images/' + imageName

def getWrongAnswers():
    wrong_options = ["No" if a==b else "Yes", "Maybe", "Can't tell!"]
    random.shuffle(wrong_options)
    return wrong_options

def sol():
    is_equal = "equal" if a == b else "not equal"
    answer = "Yes" if a == b else "No"
    multiplySymbol = '\\times '
    return f"Here we have A as a matrix of {latex(str(a) + multiplySymbol + str(a))} and B as a matrix of {latex(str(b) + multiplySymbol + str(b))}. Since they are {is_equal}, the correct answer is {answer}."

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
                        ContributorMail='2018.harmeet.kathoda@ves.ac.in',
                        Solution_text=solution
                    )

    return database_dict

putInCsv('030102', 5, main_function, __file__)