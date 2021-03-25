from mmap import ALLOCATIONGRANULARITY
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
#distchoice.remove(x)
y = random.choice(distchoice)
center = [] 
ans = []
coptstr = ''
if(x<=y):
    center.append('B')
    Boptions = [f'{B} is at same distance from {A} and {C}',f'{C} is at same distance from {A} and {B}',f'{A} is nearer to {B} than {C}',f'{C} is nearer to {B} than {A}']
    if(y == x):
        ans.append('BeAC')
        coptstr += f'{B} is at same distance from {A} and {C}'
        Boptions.remove(coptstr)
    elif(x+y == y):
        ans.append('CeAB')
        coptstr += f'{C} is at same distance from {A} and {B}'
        Boptions.remove(coptstr)
    elif(x < y):
        ans.append('AnBtC')
        coptstr += f'{A} is nearer to {B} than {C}'
        Boptions.remove(coptstr)
    elif(y < x):
        ans.append('CnBtA')
        coptstr += f'{C} is nearer to {B} than {A}'
        Boptions.remove(coptstr)
elif(x>y):
    center.append('BC')
    BCoptions = [f'{B} is at same distance from {A} and {C}',f'{C} is at same distance from {A} and {B}',f'{A} is at same distance from {B} and {C}','None of the point is equidistant from the other two points']
    if(x==y):
        ans.append('BeAC')
        coptstr += f'{B} is at same distance from {A} and {C}'
        BCoptions.remove(coptstr)
    elif(x+y==y or x-y==y):
        ans.append('CeAB')
        coptstr += f'{C} is at same distance from {A} and {B}'
        BCoptions.remove(coptstr)
    elif(x+y==x or x-y==x):
        ans.append('AeBC')
        coptstr += f'{A} is at same distance from {B} and {C}'
        BCoptions.remove(coptstr)
    else:
        ans.append('NeABC')
        coptstr += 'None of the point is equidistant from the other two points'
        BCoptions.remove(coptstr)

def getQuestion():
    return f"{B} is {latex(x)} metres from {A}. {C} is {latex(y)} metres from {B}. Assuming {B} and {C} are in the same direction from {A} which of the following statement is correct?"

def getCorrOption():
    return coptstr

def getWrongOptions():
    if(center[0]=='B'):
        wrongoptions = [Boptions[0],Boptions[1],Boptions[2]]
        random.shuffle(wrongoptions)
        return wrongoptions
    elif(center[0]=='BC'):
        wrongoptions = [BCoptions[0],BCoptions[1],BCoptions[2]]
        random.shuffle(wrongoptions)
        return wrongoptions

def soln():
    slnstr = ''
    if(center[0]=='B'):
        slnstr += f"Let the distance between {A} and {B} be {latex('x')}, and the distance between {B} and {C} be {latex('y')}.\n"
        slnstr += f"Here {latex('x=')}{latex(x)}{latex('m')} and {latex('y=')}{latex(y)}{latex('m')}.\n"
        slnstr += f"{A}---{latex(x)}{latex('m')}--->{B}---{latex(y)}{latex('m')}--->{C}\n"
        if(ans[0]=='BeAC'):
            slnstr += f"As we can see that the distance between {A} and {B} is {latex(x)}{latex('m')}, and the distance between {B} and {C} is also {latex(y)}{latex('m')}.\n"
            #print("Therefore we can conclude that B is at same distance from A and C.")
            slnstr += coptstr
            return slnstr
        elif(ans[0]=='CeAB'):
            slnstr += f"The distance between {A} and {C} can be found out by adding the distance between {A} and {B} and the distance between {B} and {C}.\n"
            slnstr += f"Therefore, distance between {A} and {C} {latex('= ')}{latex(x)}{latex('+')}{latex(y)}{latex(' = ')}{latex(x+y)}{latex('m')}"
            slnstr += f"As we can see that the distance between {A} and {C} is {latex(x+y)}{latex('m')}, and the distance between {B} and {C} is also {latex(y)}{latex('m')}."
            #print("Therefore we can conclude that C is at same distance from A and B.")
            slnstr += coptstr
            return slnstr
        elif(ans[0]=='AnBtC'):
            slnstr += f"As we can see that the distance between {A} and {B} is {latex(x)}{latex('m')}, and the distance between {B} and {C} is {latex(y)}{latex('m')}.\n"
            slnstr += f"Since the distance between {A} and {B} {latex('<')} distance between {B} and {C}\n"
            #print("We can conclude that A is nearer to B than C.")
            slnstr += coptstr
            return slnstr
        elif(ans[0]=='CnBtA'):
            slnstr += f"As we can see that the distance between {A} and {B} is {latex(x)}{latex('m')}, and the distance between {B} and {C} is {latex(y)}{latex('m')}.\n"
            slnstr += f"Since the distance between {B} and {C} {latex('<')} distance between {A} and {B}\n"
            #print("We can conclude that C is nearer to B than A.")
            slnstr += coptstr
            return slnstr
    elif(center[0]=='BC'):
        slnstr += f"Let the distance between {A} and {B} be {latex('x')}, and the distance between {B} and {C} be {latex('y')}.\n"
        slnstr += f"Here {latex('x=')}{latex(x)}{latex('m')} and {latex('y=')}{latex(y)}{latex('m')}.\n"
        slnstr += f"There are two possible ways in which {A}, {B}, {C} can be arranged.\n"
        slnstr += "Arrangement 1:-\n"
        slnstr += f"{A}---{latex(x)}{latex('m')}--->{B}---{latex(y)}{latex('m')}--->{C}\n"
        slnstr += "Arrangement 2:-\n"
        slnstr += f"{A}-----{latex(x)}{latex('m')}----->{B}\n".format(A,x,B)
        slnstr += f"{C}<---{latex(y)}{latex('m')}---{B}\n"
        #print("Distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(A,C,B,C,A,B))
        slnstr += f"Distance between {A} and {C} {latex('= ')}{latex(x)}{latex('-')}{latex(y)}{latex(' = ')}{latex(x-y)}{latex('m')}"
        slnstr += f"    ...([distance between {A} & {B}] {latex('-')} [distance between {B} & {C}])\n"
        slnstr += f"{A}----{latex(x-y)}{latex('m')}---->{C}----{latex(y)}{latex('m')}---->{B}\n"
        if(ans[0]=='BeAC'):
            slnstr += f"We can see that the distance between {A} and {B} is {latex(x)}{latex('m')}, and the distance between {B} and {C} is also {latex(y)}{latex('m')}.\n"
            #print("Therefore we can conclude that B is at same distance from A and C.")
            slnstr += coptstr
            return slnstr
        elif(ans[0]=='CeAB'):
            slnstr += f"According to Arrangement-2 the distance between {A} and {C} can be found out by subtracting the distance between {B} and {C} from the distance between {A} and {B}.\n".format(A,C,B,C,A,B)
            slnstr += f"Therefore, distance between {A} and {C} {latex('= ')}{latex(x)}{latex('-')}{latex(y)}{latex(' = ')}{latex(x-y)}{latex('m')}"
            slnstr += f"As we can see that the distance between {A} and {C} is {latex(x-y)}{latex('m')}, and the distance between {B} and {C} is also {latex(y)}{latex('m')}.\n"
            #print("Therefore we can conclude that C is at same distance from A and B.")
            slnstr += coptstr
            return slnstr
        elif(ans[0]=='AeBC'):
            slnstr += f"According to Arrangement-2 the distance between {A} and {C} can be found out by subtracting the distance between {B} and {C} from the distance between {A} and {B}.\n".format(A,C,B,C,A,B)
            slnstr += f"Therefore, distance between {A} and {C} {latex('= ')}{latex(x)}{latex('-')}{latex(y)}{latex(' = ')}{latex(x-y)}{latex('m')}"
            slnstr += f"As we can see that the distance between {A} and {C} is {latex(x-y)}{latex('m')}, and the distance between {A} and {B} is also {latex(x)}{latex('m')}.\n"
            #print("Therefore we can conclude that A is at same distance from B and C.")
            slnstr += coptstr
            return slnstr
        else:
            slnstr += "It is evident from both the Arrangements that no point is at the same distance from the other two points."
            return slnstr

def changequestion():
    global A,B,C,places,x,y,coptstr,center,ans,Boptions,BCoptions
    places = ['Home','School','Tuition','Library','Stationary','Restaurant','Mall','Supermarket','Coffee Shop','Theatre','Playground','Salon','Hospital','Medicine Shop','Petrol Pump','Factory','Office','Police Station','Bus Stop']
    A = random.choice(places)
    places.remove(A)
    B = random.choice(places)
    places.remove(B)
    C = random.choice(places)
    distchoice = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950]
    x = random.choice(distchoice)
    #distchoice.remove(x)
    y = random.choice(distchoice)
    center = [] 
    ans = []
    coptstr = ''
    if(x<=y):
        center.append('B')
        Boptions = [f'{B} is at same distance from {A} and {C}',f'{C} is at same distance from {A} and {B}',f'{A} is nearer to {B} than {C}',f'{C} is nearer to {B} than {A}']
        if(y == x):
            ans.append('BeAC')
            coptstr += f'{B} is at same distance from {A} and {C}'
            Boptions.remove(coptstr)
        elif(x+y == y):
            ans.append('CeAB')
            coptstr += f'{C} is at same distance from {A} and {B}'
            Boptions.remove(coptstr)
        elif(x < y):
            ans.append('AnBtC')
            coptstr += f'{A} is nearer to {B} than {C}'
            Boptions.remove(coptstr)
        elif(y < x):
            ans.append('CnBtA')
            coptstr += f'{C} is nearer to {B} than {A}'
            Boptions.remove(coptstr)
    elif(x>y):
        center.append('BC')
        BCoptions = [f'{B} is at same distance from {A} and {C}',f'{C} is at same distance from {A} and {B}',f'{A} is at same distance from {B} and {C}','None of the point is equidistant from the other two points']
        if(x==y):
            ans.append('BeAC')
            coptstr += f'{B} is at same distance from {A} and {C}'
            BCoptions.remove(coptstr)
        elif(x+y==y or x-y==y):
            ans.append('CeAB')
            coptstr += f'{C} is at same distance from {A} and {B}'
            BCoptions.remove(coptstr)
        elif(x+y==x or x-y==x):
            ans.append('AeBC')
            coptstr += f'{A} is at same distance from {B} and {C}'
            BCoptions.remove(coptstr)
        else:
            ans.append('NeABC')
            coptstr += 'None of the point is equidistant from the other two points'
            BCoptions.remove(coptstr)

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

putInCsv('030102',10,main_function,'v7_3')