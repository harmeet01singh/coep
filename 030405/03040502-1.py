import string
import random

variable1 = random.choice(string.ascii_lowercase)
variable2 = random.choice(string.ascii_lowercase)

def superscript(variable, power):
    if power == 1:
        return variable + chr(0x00b9)
    elif power == 2 or power == 3:
        return variable + chr(0x00b0 + power)
    else:
        return variable + chr(0x2070 + power)

def convert_to_term(coefficient, variable1, power1, variable2, power2):
    return str(coefficient) + superscript(variable1, power1) + superscript(variable2, power2)

def terms(is_numerator):
    if is_numerator:
        coefficient = random.randint(11, 99)
        power1 = random.randint(4, 9)
        power2 = random.randint(4, 9)
        return [ coefficient, variable1, power1, variable2, power2, convert_to_term(coefficient, variable1, power1, variable2, power2)]
    else:
        coefficient = random.randint(1, 9)
        power1 = random.randint(1, 3)
        power2 = random.randint(1, 3)
        return [ coefficient, variable1, power1, variable2, power2, convert_to_term(coefficient, variable1, power1, variable2, power2)]

def sol(n, d, qcoefficient, qpower1, qpower2, quotient, remainder):
    print("\n--------------------------------SOLUTION--------------------------------------")
    print("We have numerator as: " + n + " and the denominator as: " + d)
    print("So by dividing the coefficients we get the number as:" + str(qcoefficient))
    print("Further subtrating the powers of variables in the denominator with that of numerator we get the two variables as: " + superscript(variable1, qpower1) + " and " + superscript(variable2, qpower2))
    print("So we have the quotient as: " + quotient)
    print("And the remainder becomes: " + str(remainder))

def options(n, d, correct_option):
    qcoefficient, qpower1, qpower2 = ( n[0]//d[0], n[2]-d[2], n[4]-d[4])
    quotient = convert_to_term(qcoefficient, variable1, qpower1, variable2, qpower2)
    remainder = n[0]%d[0]
    option_array = []

    for i in range(4):
        if i + 1 == correct_option:
            option_array.append( ' ' + quotient + ', ' + str(remainder))
        else:
            option_array.append( random.choice('  -') + convert_to_term(qcoefficient + random.randint(-5, 5), variable1, random.randint(1,9), variable2, random.randint(1,9)) + ', ' + str(random.randint(1,10)) )

    for i in range(1, 5):
        print(str(i) + '. ' + option_array[i-1])
    
    selected = int(input("Select any one option:"))
    
    if selected == correct_option:
        print("You have Selected the right option")
        sol(numerator[5], denominator[5], qcoefficient, qpower1, qpower2, quotient, remainder)
    else:
        print("The selected option is wrong")
        sol(n[5], d[5], qcoefficient, qpower1, qpower2, quotient, remainder)

numerator = terms(True)
denominator = terms(False)

print("Divide the following monomial and select the correct quotient and remainder:" + numerator[5] + "/" + denominator[5])
correct_option = random.randint(1, 4)
options(numerator, denominator, correct_option)