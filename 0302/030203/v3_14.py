import random
from coep_package.csv_module import putInCsv, database_fn
from coep_package.latex import latex, to_frac
from IndianNameGenerator import *


def main_function():
    n1 = randomMarathi()

    r2 = random.randint(1, 25)

    r1 = random.randint(30, 100)

    # option 1
    x1 = (r1 + r2 + 1)

    # option 2
    x4 = abs(r1 - r2 - 1)

    # option 3
    x3 = (r1 + r2)

    # option 4
    x2 = abs(r1 - r2)

    items = ['sheeps', 'books', 'pens', 'sheets', 'toys', 'candies', 'pencils', 'shirts', 'pants', 'T-shirts',
             'jackets',
             'bananas', 'chocolates', 'watermelons', 'cookies']

    i = random.choice(items)

    # print( n1+' and '+n2+' have a total of '+str(r1)+' ',i,'.')
    # print(
    #     n1 + ' has some ' + i + '.' + 'After buying ' + str(r2) + ' more from the market,' + n1 + ' has ' + str(
    #         r1), i + '.How many', i, n1 + ' had initially?')
    # # print('How many', i, n1 + ' have initially?')
    r = random.randint(1, 5)

    # temp1 = n1 + ' has a total of ' + str(r1) + ' ' + i + '.'
    temp1 = n1 + ' has some ' + i + '.' + 'After buying ' + str(r2) + ' more from the market,' + n1 + ' has ' + str(
        r1) + ' ' + i + '.'

    # temp2 = 'If ' + n2 + ' has ' + str(r2) + ' more ' + i + ' than ' + n1 + ', how many ' + i + ' does each one have?\n'
    temp2 = 'How many ' + i + ' ' + n1 + ' had initially?'
    #
    question = temp1 + temp2
    print(question)

    op = ["", "", "", ""]
    sq = [0, 1, 2, 3]
    # option variables
    o1 = n1 + ''' has ''' + str(int(x1)) + ''' ''' + i
    o2 = n1 + ''' has ''' + str(int(x4)) + ''' ''' + i
    o3 = n1 + ''' has ''' + str(int(x2)) + ''' ''' + i
    o4 = n1 + ''' has ''' + str(int(x3)) + ''' ''' + i

    ra = random.randint(0, 3)
    op[ra] = o3
    sq.remove(ra)
    op[sq[0]] = o1
    op[sq[1]] = o2
    op[sq[2]] = o4
    # PRINTING OPTIONS
    for z in range(1, 5):
        print("Option", z, ":", op[z - 1])
    print("")
    value = 3  # int(input("Enter the option number:"))

    def sol():
        sol = 'Let the number of ' + i + " with " + str(n1) + ' initially be ' + latex(
            'x') + '.' + '<br/> After buying ' + str(r2) + ' ' + i + ' ' + str(n1) + ' has ' + str(
            r1) + ' ' + i + ' left' + '<br/> Total number of ' + i + ' = Initial number of ' + i + ' + Number of ' + i + ' bought ' + '<br/> Therefore ' + latex(
            'x + ' + str(r2) + ' = ' + str(r1)) + '<br/>' + latex(
            '<br/> x + ' + str(r2) + ' ''- ' + str(r2) + ' = ' + str(r1) + ' - ' + str(r2)) + '  (Subtract ' + latex(str(
            r2)) + ' from both sides)' 
        a = r1 - r2
        sol = sol + '<br/>' + latex('<br/> x + 0 = ') + latex(str(a)) + '<br/>'
        sol = sol + latex("<br/> x = ") + latex(str(a))
        sol = sol + '<br/> Therefore, ' + latex('x' + ' = ' + str(a))
        sol = sol + '<br/> Thus, there were ' + latex(str(a)) + ' ' + i + ' with ' + n1 + ' initially'

        return sol

    if value == ra + 1:
        print("\nYour answer is Correct!!!")
        print("~********** SOLUTION **********~")
        sol()
    elif value != ra + 1 and value < 5 and value > 0:
        print("\nYour answer is incorrect!!")
        print("~********** SOLUTION **********~")
        sol()
    else:
        print("Invalid Choice")

    database_dict = database_fn(
        Answer_Type='1',
        Topic_Number='030203',
        Variation='v3_14',
        Question=question,
        Correct_Answer_1=o3,
        Wrong_Answer_1=o1,
        Wrong_Answer_2=o2,
        Wrong_Answer_3=o4,
        ContributorMail='2019simran.bhoneja@ves.ac.in',
        Solution_text=sol()
    )
    return database_dict


putInCsv(
    Topic_Number='030203',
    Number_Of_Iterations=15,
    Main_Function=main_function,
    Filename='v3_14')
