from PIL import Image, ImageDraw, ImageFont
import random
from coep_package.latex import latex
from coep_package.csv import database_fn, putInCsv

x, y = ( 0, 0)
figureName1 = ''
figureName2 = ''

def changeGlobals():
    global x, y
    x, y = (random.randint(1, 4), random.randint(1, 4))

def getQuestion():
    return "Are A and B identical in shape and size: A = B?"

def getCorrectAnswer():
    return "Yes" if x == y else "No"

def generate_image():
    if x == 1:
        img = generate_image_square1(5)
        figureName1 = 'Square'
    elif x == 2:
        img = generate_image_rectangle1(8, 5)
        figureName1 = 'Rectangle'
    elif x == 3:
        img = generate_image_circle1(6)
        figureName1 = 'Circle'
    else:
        triangle = [175, 50, 50, 300, 300, 300]
        img = generate_image_triangle1(triangle)
        figureName1 = 'Triangle'
    if y == 1:
        finalImage = generate_image_square2(img, 5)
        figureName2 = 'Square'
    elif y == 2:
        finalImage = generate_image_rectangle2(img, 8, 5)
        figureName2 = 'Rectangle'
    elif y == 3:
        finalImage = generate_image_circle2(img, 6)
        figureName2 = 'Circle'
    else:
        triangle = [175, 50, 50, 300, 300, 300]
        finalImage = generate_image_triangle2(img, triangle)
        figureName2 = 'Triangle'

    imageName = f'030102_D_{figureName1[0]}_{figureName2[0]}.png'

    finalImage.save('images/' + imageName)
    return 'images/' + imageName

margin, multiple = 50, 50
width = 800
height = 600

def generate_image_square1(a):
    img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # For A matrix
    a_start_cordinate = (margin, margin)
    a_end_cordinate = (margin + a * multiple, margin + a * multiple)
    draw.rectangle([a_start_cordinate, a_end_cordinate], fill="red", outline="black", width=1)
    draw.text((margin + (a_end_cordinate[0] - margin) // 2, a_end_cordinate[1] + 50), "A",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    return img

def generate_image_square2(img, b):
    draw = ImageDraw.Draw(img)

    # For B matrix
    b_start_cordinate = (450, margin)
    b_end_cordinate = (450 + b * multiple, margin + b * multiple)
    draw.rectangle([b_start_cordinate, b_end_cordinate], fill="green", outline="black", width=1)
    draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0]) // 2, b_end_cordinate[1] + 50), "B",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    # Display Image
    return img

def generate_image_rectangle1(l1, b1):
    img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # For A matrix
    a_start_cordinate = (margin, margin)
    a_end_cordinate = (margin + b1 * multiple, margin + l1 * multiple)
    draw.rectangle([a_start_cordinate, a_end_cordinate],
                   fill="red", outline="black", width=1)
    draw.text((margin + (a_end_cordinate[0] - margin) // 2, a_end_cordinate[1] + 50),
              "A", font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    return img

def generate_image_rectangle2(img, l2, b2):
    draw = ImageDraw.Draw(img)

    # For B Matrx
    b_start_cordinate = (450, margin)
    b_end_cordinate = (450 + b2 * multiple, margin + l2 * multiple)
    draw.rectangle([b_start_cordinate, b_end_cordinate],
                   fill="green", outline="black", width=1)
    draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0]) // 2,
               b_end_cordinate[1] + 50), "B", font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    # Display Image
    return img

def generate_image_circle1(a):
    img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # For A circle
    a_start_cordinate = (margin, margin)
    a_end_cordinate = (margin + a * multiple, margin + a * multiple)
    draw.ellipse([a_start_cordinate, a_end_cordinate], fill="red", outline="black", width=1)
    draw.text((margin + (a_end_cordinate[0] - margin) // 2, a_end_cordinate[1] + 50), "A",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    return img

def generate_image_circle2(img, b):
    draw = ImageDraw.Draw(img)

    # For B circle
    b_start_cordinate = (450, margin)
    b_end_cordinate = (450 + b * multiple, margin + b * multiple)
    draw.ellipse([b_start_cordinate, b_end_cordinate], fill="green", outline="black", width=1)
    draw.text((b_start_cordinate[0] + (b_end_cordinate[0] - b_start_cordinate[0]) // 2, b_end_cordinate[1] + 50), "B",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    # Display Image
    return img

def generate_image_triangle1(triangle):
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # for A triangle
    size = triangle
    x1, y1, x2, y2, x3, y3 = size
    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill="red", outline="black")
    draw.text((175, 400), "A",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    return img

def generate_image_triangle2(img, triangle):
    draw = ImageDraw.Draw(img)

    # for B triangle
    size = triangle
    x1, y1, x2, y2, x3, y3 = size
    draw.polygon([(x1 + 400, y1), (x2 + 400, y2), (x3 + 400, y3)], fill="green", outline="black")
    draw.text((575, 400), "B",
              font=ImageFont.truetype("arial.ttf", size=15), fill="black")

    # Display Image
    return img

def getWrongAnswers():
    wrong_options = ["No" if x == y else "Yes", "Maybe", "Can't tell!"]
    random.shuffle(wrong_options)
    return wrong_options

def sol():
    shape = "equal" if x == y else "different"
    answer = "Yes" if x == y else "No"
    return f"Since they are {shape} shapes, the correct answer is {answer}."

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
                        ContributorMail='2019surendra.totre@ves.ac.in',
                        Solution_text=solution
                    )

    return database_dict

putInCsv('030102', 5, main_function, __file__)