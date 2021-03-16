import string
import random
from math import gcd
# from ..packages.latex_module import superscript, to_frac, convert_to_term
#print('\n\033[4m'+'3' + '\033[0m'+'\n2')

# dod = int(input("Select degree of difficulty:\n1.Easy\n2.Hard\nEnter option number:"))

variable_set = random.choice(['ab', 'mn', 'xy'])
variable1 = variable_set[0]
variable2 = variable_set[1]

def superscript(variable, power):
    return f'{variable}^{ {power} }'

def convert_to_term(coefficient, variable1, power1, variable2, power2):
    return (str(coefficient) if coefficient != 1 else '') + superscript(variable1, power1) + superscript(variable2, power2)

def to_frac(numerator, denominator):
    return f'$\\frac{{{numerator}}}{{{denominator}}}$'

def terms(is_numerator):
    if is_numerator:
        coefficient = random.randint(1, 50)
        power1 = random.randint(-9, 9)
        power2 = random.randint(-9, 9)
        return [ coefficient, variable1, power1, variable2, power2, convert_to_term(coefficient, variable1, power1, variable2, power2)]
    else:
        coefficient = random.randint(1, 5) * 2
        power1 = random.randint(-9, 9)
        power2 = random.randint(-9, 9)
        return [ coefficient, variable1, power1, variable2, power2, convert_to_term(coefficient, variable1, power1, variable2, power2)]

def sol(n, d, qcoefficient, qpower1, qpower2, ans_num, ans_den):
    print("\n--------------------------------SOLUTION--------------------------------------")
    print("We have numerator as: " + n + " and the denominator as: " + d)
    print("So by simplifying the coefficients we get the fraction as:" + underline(str(qcoefficient)) + '\n\t\t\t\t\t\t\t   ' + ans_den)
    print("Further subtrating the powers of variables in the denominator with that of numerator we get the two variables as: " + superscript(variable1, qpower1) + " and " + superscript(variable2, qpower2))
    print("So we have the answer as: " + to_frac( ans_num, ans_den))

def correct_sign(nsign, dsign):
    if nsign == '+' and dsign == '+':
        return ''
    elif nsign == '-' and dsign == '-':
        return ''
    else:
        return '-'

def options(n, d, correct_option, nsign, dsign):
    qcoefficient, qpower1, qpower2 = ( n[0]//gcd(n[0], d[0]), n[2]-d[2], n[4]-d[4])
    ans_num = convert_to_term(qcoefficient, variable1, qpower1, variable2, qpower2)
    ans_den = str( d[0]//gcd(n[0], d[0]) )
    if n[0]%d[0] == 0:
        ans_den = '1'
    asign = correct_sign(nsign, dsign)
    option_array = []

    for i in range(4):
        if i + 1 == correct_option:
            option_array.append( to_frac(asign + ans_num, ans_den ) )
        else:
            random_number = random.choice([ -qcoefficient, qcoefficient ])
            power1 = random.choice([ -qpower1, n[2]+d[2], n[2]//d[2] if d[2] != 0 else n[2] ])
            power2 = random.choice([ -qpower2, n[4]+d[4], n[4]//d[4] if d[4] != 0 else n[4] ])
            opt_den = random.choice([ -int(ans_den), int(ans_den)])
            option_array.append( to_frac(convert_to_term( random_number, variable1, power1, variable2, power2 ), str(opt_den) ))

    for i in range(1, 5):
        print(str(i) + '. ' + option_array[i-1])
    
    selected = int(input("Select any one option:"))
    
    if selected == correct_option:
        print("You have Selected the right option")
        sol(n[5], d[5], qcoefficient, qpower1, qpower2, ans_num, ans_den)
    else:
        print("The selected option is wrong")
        sol(n[5], d[5], qcoefficient, qpower1, qpower2, ans_num, ans_den)

def underline(term):
    return '\033[4m'+ term + '\033[0m'

nsign = random.choice('+-')
dsign = random.choice('+-')
numerator = terms(True)
denominator = terms(False)

print("Divide the following monomials and select the correct options: " + to_frac( (nsign if nsign == '-' else '') + numerator[5] , (dsign if dsign == '-' else '') + denominator[5] ))
correct_option = random.randint(1, 4)
options(numerator, denominator, correct_option, nsign, dsign)