import random
from coep_package.latex import latex
from coep_package.csv import database_fn, putInCsv
places = ['Home','School','Tuition','Library','Stationary','Restaurant','Mall','Supermarket','Coffee Shop','Theatre','Playground','Salon','Hospital','Medicine Shop','Petrol Pump','Factory','Office','Police Station','Bus Stop']
A = random.choice(places)
places.remove(A)
B = random.choice(places)
places.remove(B)
C = random.choice(places)
distchoice = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950]
x = random.choice(distchoice)
distchoice.remove(x)
y = random.choice(distchoice)
center = []
ans = []
coptstr = ''
if(x<y):
    center.append('B')
    Boptions = [f'{B} is at same distance from {A} and {C}',f'{C} is at same distance from {A} and {B}',f'{A} is nearer to {B} than {C}',f'{C} is nearer to {B} than {A}']
    if(y-x == x):
        ans.append('BeAC')
        coptstr += f'{B} is at same distance from {A} and {C}'
        Boptions.remove(coptstr)
    elif(y-x == y):
        ans.append('CeAB')
        coptstr += f'{C} is at same distance from {A} and {B}'
        Boptions.remove(coptstr)
    elif(x < y-x):
        ans.append('AnBtC')
        coptstr += f'{A} is nearer to {B} than {C}'
        Boptions.remove(coptstr)
    elif(y-x < x):
        ans.append('CnBtA')
        coptstr += f'{C} is nearer to {B} than {A}'
        Boptions.remove(coptstr)
elif(y<x):
    center.append('C')
    Coptions = [f'{B} is at same distance from {A} and {C}',f'{C} is at same distance from {A} and {B}',f'{A} is nearer to {C} than {B}',f'{B} is nearer to {C} than {A}']
    if(x-y == x):
        ans.append('BeAC')
        coptstr += f'{B} is at same distance from {A} and {C}'
        Coptions.remove(coptstr)
    elif(x-y == y):
        ans.append('CeAB')
        coptstr += f'{C} is at same distance from {A} and {B}'
        Coptions.remove(coptstr)
    elif(y < x-y):
        ans.append('AnCtB')
        coptstr += f'{A} is nearer to {C} than {B}'
        Coptions.remove(coptstr)
    elif(x-y < y):
        ans.append('BnCtA')
        coptstr += f'{B} is nearer to {C} than {A}'
        Coptions.remove(coptstr)

def getQuestion():
    return f"{B} is {latex(x)} metres from {A}. {C} is {latex(y)} metres from {A}. Assuming {B} and {C} are in the same direction from {A} which of the following statement is correct?"

def getCorrOption():
    return coptstr

def getWrongOptions():
    if(center[0]=='B'):
        wrongoptions = [Boptions[0],Boptions[1],Boptions[2]]
        random.shuffle(wrongoptions)
        return wrongoptions
    elif(center[0]=='C'):
        wrongoptions = [Coptions[0],Coptions[1],Coptions[2]]
        random.shuffle(wrongoptions)
        return wrongoptions

def soln():
    slnstr = ''
    if(center[0]=='B'):
        slnstr += f"Let the distance between {A} and {B} be {latex('x')}, and the distance between {A} and {C} be {latex('y')}.\n"
        slnstr += f"Here {latex('x=')}{latex(x)}{latex('m')} and {latex('y=')}{latex(y)}{latex('m')}.\n"
        slnstr += f"{A}---{latex(x)}{latex('m')}--->{B}\n"
        slnstr += f"{A}-----{latex(y)}{latex('m')}----->{C}\n"
        if(ans[0]=='BeAC'):
            #print("The distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(B,C,A,B,A,C))
            slnstr += f"Distance between {B} and {C} {latex('= ')}{latex(y)}{latex('-')}{latex(x)}{latex(' = ')}{latex(y-x)}{latex('m')}"
            slnstr += f"    ...([distance between {A} & {C}] {latex('-')} [distance between {A} & {B}])\n"
            slnstr += f"{A}----{latex(x)}{latex('m')}---->{B}----{latex(y-x)}{latex('m')}---->{C}\n"
            slnstr += f"As we can see that the distance between {A} and {B} is {latex(x)}{latex('m')}, and the distance between {B} and {C} is also {latex(y-x)}{latex('m')}.\n"
            #print("Therefore we can conclude that B is at same distance from A and C.")
            slnstr += coptstr
            return slnstr
        elif(ans[0]=='CeAB'):
            #print("The distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(B,C,A,B,A,C))
            slnstr += f"Distance between {B} and {C} {latex('= ')}{latex(y)}{latex('-')}{latex(x)}{latex(' = ')}{latex(y-x)}{latex('m')}"
            slnstr += f"    ...([distance between {A} & {C}] {latex('-')} [distance between {A} & {B}])\n"
            slnstr += f"{A}----{latex(x)}{latex('m')}---->{B}----{latex(y-x)}{latex('m')}---->{C}\n"
            slnstr += f"As we can see that the distance between {A} and {C} is {latex(y)}{latex('m')}, and the distance between {B} and {C} is also {latex(y-x)}{latex('m')}.\n"
            #print("Therefore we can conclude that C is at same distance from A and B.")
            slnstr += coptstr
            return slnstr
        elif(ans[0]=='AnBtC'):
            #print("The distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(B,C,A,B,A,C))
            slnstr += f"Distance between {B} and {C} {latex('= ')}{latex(y)}{latex('-')}{latex(x)}{latex(' = ')}{latex(y-x)}{latex('m')}"
            slnstr += f"    ...([distance between {A} & {C}] {latex('-')} [distance between {A} & {B}])\n"
            slnstr += f"{A}----{latex(x)}{latex('m')}---->{B}----{latex(y-x)}{latex('m')}---->{C}\n"
            slnstr += f"As we can see that the distance between {A} and {B} is {latex(x)}{latex('m')}, and the distance between {B} and {C} is {latex(y-x)}{latex('m')}.\n"
            slnstr += f"Since the distance between {A} and {B} {latex('<')} distance between {B} and {C}\n"
            #print("We can conclude that A is nearer to B than C.")
            slnstr += coptstr
            return slnstr
        elif(ans[0]=='CnBtA'):
            #print("The distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(B,C,A,B,A,C))
            slnstr += f"Distance between {B} and {C} {latex('= ')}{latex(y)}{latex('-')}{latex(x)}{latex(' = ')}{latex(y-x)}{latex('m')}"
            slnstr += f"    ...([distance between {A} & {C}] {latex('-')} [distance between {A} & {B}])\n"
            slnstr += f"{A}----{latex(x)}{latex('m')}---->{B}----{latex(y-x)}{latex('m')}---->{C}\n"
            slnstr += f"As we can see that the distance between {A} and {B} is {latex(x)}{latex('m')}, and the distance between {B} and {C} is {latex(y-x)}{latex('m')}.\n"
            slnstr += f"Since the distance between {B} and {C} {latex('<')} distance between {A} and {B}\n"
            #print("We can conclude that C is nearer to B than A.")
            slnstr += coptstr
            return slnstr
    elif(center[0]=='C'):
        slnstr += f"Let the distance between {A} and {B} be {latex('x')}, and the distance between {A} and {C} be {latex('y')}.\n"
        slnstr += f"Here {latex('x=')}{latex(x)}{latex('m')} and {latex('y=')}{latex(y)}{latex('m')}.\n"
        slnstr += f"{A}---{latex(y)}{latex('m')}--->{C}\n"
        slnstr += f"{A}-----{latex(x)}{latex('m')}----->{B}\n"
        if(ans[0]=='BeAC'):
            #print("The distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(B,C,A,C,A,B))
            slnstr += f"Distance between {B} and {C} {latex('= ')}{latex(x)}{latex('-')}{latex(y)}{latex(' = ')}{latex(x-y)}{latex('m')}"
            slnstr += f"    ...([distance between {A} & {B}] {latex('-')} [distance between {A} & {C}])\n"
            slnstr += f"{A}----{latex(y)}{latex('m')}---->{C}----{latex(x-y)}{latex('m')}---->{B}\n"
            slnstr += f"As we can see that the distance between {A} and {B} is {latex(x)}{latex('m')}, and the distance between {B} and {C} is also {latex(x-y)}{latex('m')}.\n"
            #print("Therefore we can conclude that B is at same distance from A and C.")
            slnstr += coptstr
            return slnstr
        elif(ans[0]=='CeAB'):
            #print("The distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(B,C,A,C,A,B))
            slnstr += f"Distance between {B} and {C} {latex('= ')}{latex(x)}{latex('-')}{latex(y)}{latex(' = ')}{latex(x-y)}{latex('m')}"
            slnstr += f"    ...([distance between {A} & {B}] {latex('-')} [distance between {A} & {C}])\n"
            slnstr += f"{A}----{latex(y)}{latex('m')}---->{C}----{latex(x-y)}{latex('m')}---->{B}\n"
            slnstr += f"As we can see that the distance between {A} and {C} is {latex(y)}{latex('m')}, and the distance between {B} and {C} is also {latex(x-y)}{latex('m')}.\n"
            #print("Therefore we can conclude that C is at same distance from A and B.")
            slnstr += coptstr
            return slnstr
        elif(ans[0]=='AnCtB'):
            #print("The distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(B,C,A,C,A,B))
            slnstr += f"Distance between {B} and {C} {latex('= ')}{latex(x)}{latex('-')}{latex(y)}{latex(' = ')}{latex(x-y)}{latex('m')}"
            slnstr += f"    ...([distance between {A} & {B}] {latex('-')} [distance between {A} & {C}])\n"
            slnstr += f"{A}----{latex(y)}{latex('m')}---->{C}----{latex(x-y)}{latex('m')}---->{B}\n"
            slnstr += f"As we can see that the distance between {A} and {C} is {latex(y)}{latex('m')}, and the distance between {B} and {C} is {latex(x-y)}{latex('m')}.\n"
            slnstr += f"Since the distance between {A} and {C} {latex('<')} distance between {B} and {C}\n"
            #print("We can conclude that A is nearer to C than B.")
            slnstr += coptstr
            return slnstr
        elif(ans[0]=='BnCtA'):
            #print("The distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(B,C,A,C,A,B))
            slnstr += f"Distance between {B} and {C} {latex('= ')}{latex(x)}{latex('-')}{latex(y)}{latex(' = ')}{latex(x-y)}{latex('m')}"
            slnstr += f"    ...([distance between {A} & {B}] {latex('-')} [distance between {A} & {C}])\n"
            slnstr += f"{A}----{latex(y)}{latex('m')}---->{C}----{latex(x-y)}{latex('m')}---->{B}\n"
            slnstr += f"As we can see that the distance between {A} and {C} is {latex(y)}{latex('m')}, and the distance between {B} and {C} is {latex(x-y)}{latex('m')}.\n"
            slnstr += f"Since the distance between {B} and {C} {latex('<')} distance between {A} and {C}\n"
            #print("We can conclude that B is nearer to C than A.")
            slnstr += coptstr
            return slnstr

def changequestion():
    global A,B,C,places,x,y,coptstr,center,ans,Boptions,Coptions
    places = ['Home','School','Tuition','Library','Stationary','Restaurant','Mall','Supermarket','Coffee Shop','Theatre','Playground','Salon','Hospital','Medicine Shop','Petrol Pump','Factory','Office','Police Station','Bus Stop']
    A = random.choice(places)
    places.remove(A)
    B = random.choice(places)
    places.remove(B)
    C = random.choice(places)
    distchoice = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950]
    x = random.choice(distchoice)
    distchoice.remove(x)
    y = random.choice(distchoice)
    center = []
    ans = []
    coptstr = ''
    if(x<y):
        center.append('B')
        Boptions = [f'{B} is at same distance from {A} and {C}',f'{C} is at same distance from {A} and {B}',f'{A} is nearer to {B} than {C}',f'{C} is nearer to {B} than {A}']
        if(y-x == x):
            ans.append('BeAC')
            coptstr += f'{B} is at same distance from {A} and {C}'
            Boptions.remove(coptstr)
        elif(y-x == y):
            ans.append('CeAB')
            coptstr += f'{C} is at same distance from {A} and {B}'
            Boptions.remove(coptstr)
        elif(x < y-x):
            ans.append('AnBtC')
            coptstr += f'{A} is nearer to {B} than {C}'
            Boptions.remove(coptstr)
        elif(y-x < x):
            ans.append('CnBtA')
            coptstr += f'{C} is nearer to {B} than {A}'
            Boptions.remove(coptstr)
    elif(y<x):
        center.append('C')
        Coptions = [f'{B} is at same distance from {A} and {C}',f'{C} is at same distance from {A} and {B}',f'{A} is nearer to {C} than {B}',f'{B} is nearer to {C} than {A}']
        if(x-y == x):
            ans.append('BeAC')
            coptstr += f'{B} is at same distance from {A} and {C}'
            Coptions.remove(coptstr)
        elif(x-y == y):
            ans.append('CeAB')
            coptstr += f'{C} is at same distance from {A} and {B}'
            Coptions.remove(coptstr)
        elif(y < x-y):
            ans.append('AnCtB')
            coptstr += f'{A} is nearer to {C} than {B}'
            Coptions.remove(coptstr)
        elif(x-y < y):
            ans.append('BnCtA')
            coptstr += f'{B} is nearer to {C} than {A}'
            Coptions.remove(coptstr)

def main_function():
    changequestion()
    Question = getQuestion()
    Corr_op = getCorrOption()
    wrong_op1,wrong_op2,wrong_op3 = getWrongOptions()
    Solution = soln()

    database_dict= database_fn(
        Answer_Type='text',
        Topic_Number='030102',
        Variation=7,
        Question=Question,
        Correct_Answer_1=Corr_op,
        Wrong_Answer_1=wrong_op1,
        Wrong_Answer_2=wrong_op2,
        Wrong_Answer_3=wrong_op3,
        ContributorMail='2016.mohit.kale@ves.ac.in',
        Solution_text=Solution
    )
    return database_dict

putInCsv('030102',10,main_function,'v7_1')