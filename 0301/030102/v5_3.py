from PIL import Image, ImageDraw, ImageFont
import random
from coep_package.latex import latex
from coep_package.csv import database_fn, putInCsv

l1, b1, l2, b2 = ( 0, 0, 0, 0)

def changeGlobals():
    global l1, b1, l2, b2
    l1 = random.randint(5, 8)
    b1 = random.randint(5, 8)
    l2 = random.randint(l1-2, l1+2)
    b2 = random.randint(b1-2, b1+2)

def getQuestion():
    return "Are A and B identical in size: A = B?"

def getCorrectAnswer():
    return "Yes" if l1 == l2 and b1 == b2 else "No"

def generate_image():
    imageName = f'030102_R_{l1}-{b1}_{l2}-{b2}.png'

    margin, multiple = 50, 50
    width = margin*3 + multiple*(b1+b2)
    height = multiple*(l1 if l1 > l2 else l2) + margin*3
    img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    #For A matrix
    a_start_cordinate = (margin, margin)
    a_end_cordinate = (margin + b1*multiple, margin + l1*multiple)
    draw.rectangle([a_start_cordinate, a_end_cordinate],
                   fill="red", outline="black", width=1)
    for i in range(1, b1):
        draw.line([margin + i*multiple, margin, margin + i*multiple,
                   margin + l1*multiple], fill="black", width=1)  # Vertical Lines
    for i in range(1, l1):
        draw.line([margin, margin + i*multiple, margin + b1*multiple,
                   margin + i*multiple], fill="black", width=1)  # Horizontal Lines
    draw.text((margin + (a_end_cordinate[0] - margin)//2, a_end_cordinate[1] + 50),
              "A", font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    # For B Matrx
    b_start_cordinate = (2*margin + b1*multiple, margin)
    b_end_cordinate = (2*margin + b1*multiple + b2 *
                       multiple, margin + l2*multiple)
    draw.rectangle([b_start_cordinate, b_end_cordinate],
                   fill="green", outline="black", width=1)
    for i in range(1, b2):
        draw.line([b_start_cordinate[0] + i*multiple, margin, b_start_cordinate[0] +
                   i*multiple, margin + l2*multiple], fill="black", width=1)  # Vertical Lines
    for i in range(1, l2):
        draw.line([b_start_cordinate[0], b_start_cordinate[1] + i*multiple, b_end_cordinate[0],
                   b_start_cordinate[1] + i*multiple], fill="black", width=1)  # Horizontal Lines
    draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0])//2,
               b_end_cordinate[1] + 50), "B", font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    # Display Image
    img.save('images/'+imageName)

    return 'images/'+imageName
    

def getWrongAnswers():
    wrong_options = ["No" if l1 == l2 and b1 == b2 else "Yes", "Maybe", "Can't tell!"]
    random.shuffle(wrong_options)
    return wrong_options

def sol():
    is_equal = "equal" if l1 == l2 and b1 == b2 else "not equal"
    answer = "Yes" if  l1 == l2 and b1 == b2 else "No"
    multiplySymbol = '\\times '
    return f"Here we have A as a matrix of {latex( str(l1)+multiplySymbol+str(b1) )} and B as a matrix of {latex( str(l2)+multiplySymbol+str(b2) )}. Since they are {is_equal}, the correct answer is {answer}."

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
                        ContributorMail='2019mangesh.sokalwar@ves.ac.in',
                        Solution_text=solution
                    )

    return database_dict

putInCsv('030102', 5, main_function, __file__)