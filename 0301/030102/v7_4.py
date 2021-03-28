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
ans = []
coptstr = ''
while(x>y):
    y = random.choice(distchoice)
Aoptions = [f'{A} is at same distance from {B} and {C}',f'{B} is nearer to {A} than {C}',f'{C} is nearer to {A} than {B}',f'{B} is nearer to {C} than {A}']
if(x == y-x):
    ans.append('AeBC')
    coptstr += f'{A} is at same distance from {B} and {C}'
    Aoptions.remove(coptstr)
elif(x<y-x):
    ans.append('BnAtC')
    coptstr += f'{B} is nearer to {A} than {C}'
    Aoptions.remove(coptstr)
elif(x>y-x):
    ans.append('CnAtB')
    coptstr += f'{C} is nearer to {A} than {B}'
    Aoptions.remove(coptstr)
elif(y<y-x):
    ans.append('BnCtA')
    coptstr += f'{B} is nearer to {C} than {A}'
    Aoptions.remove(coptstr)

def getQuestion():
    return f"{B} is {latex(x)} metres from {A}. {C} is {latex(y)} metres from {B}. Assuming {B} and {C} are in the opposite direction from {A} which of the following statement is correct?"

def getCorrOption():
    return coptstr

def getWrongOptions():
    wrongoptions = [Aoptions[0],Aoptions[1],Aoptions[2]]
    random.shuffle(wrongoptions)
    return wrongoptions

def soln():
    slnstr = ''
    slnstr += f"Let the distance between {A} and {B} be {latex('x')}, and the distance between {B} and {C} be {latex('y')}.\n"
    slnstr += f"Here {latex('x=')}{latex(x)}{latex('m')} and {latex('y=')}{latex(y)}{latex('m')}.\n"
    slnstr += f"{B}---{latex(x)}{latex('m')}--->{A}\n"
    slnstr += f"{B}-----{latex(y)}{latex('m')}----->{C}\n"
    if(ans[0]=='AeBC'):
        #print("The distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(A,C,A,B,B,C))
        slnstr += f"Distance between {A} and {C} {latex('= ')}{latex(y)}{latex('-')}{latex(x)}{latex(' = ')}{latex(y-x)}{latex('m')}"
        slnstr += f"    ...([distance between {B} & {C}] {latex('-')} [distance between {A} & {B}])\n"
        slnstr += f"{B}---{latex(x)}{latex('m')}--->{A}---{latex(y-x)}{latex('m')}--->{C}\n"
        slnstr += f"As we can see that the distance between {A} and {B} is {latex(x)}{latex('m')}, and the distance between {A} and {C} is also {latex(y-x)}{latex('m')}.\n"
        #print("Therefore we can conclude that {} is at same distance from {} and {}.".format(A,B,C))
        slnstr += coptstr
        return slnstr
    elif(ans[0]=='BnAtC'):
        #print("The distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(A,C,A,B,B,C))
        slnstr += f"Distance between {A} and {C} {latex('= ')}{latex(y)}{latex('-')}{latex(x)}{latex(' = ')}{latex(y-x)}{latex('m')}"
        slnstr += f"    ...([distance between {B} & {C}] {latex('-')} [distance between {A} & {B}])\n"
        slnstr += f"{B}---{latex(x)}{latex('m')}--->{A}---{latex(y-x)}{latex('m')}--->{C}\n"
        slnstr += f"As we can see that the distance between {A} and {B} is {latex(x)}{latex('m')}, and the distance between {A} and {C} is {latex(y-x)}{latex('m')}.\n"
        slnstr += f"Since the distance between {A} and {B} {latex('<')} distance between {A} and {C}\n"
        #print("We can conclude that {} is nearer to {} than {}.".format(B,A,C))
        slnstr += coptstr
        return slnstr
    elif(ans[0]=='CnAtB'):
        #print("The distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(A,C,A,B,B,C))
        slnstr += f"Distance between {A} and {C} {latex('= ')}{latex(y)}{latex('-')}{latex(x)}{latex(' = ')}{latex(y-x)}{latex('m')}"
        slnstr += f"    ...([distance between {B} & {C}] {latex('-')} [distance between {A} & {B}])\n"
        slnstr += f"{B}---{latex(x)}{latex('m')}--->{A}---{latex(y-x)}{latex('m')}--->{C}\n"
        slnstr += f"As we can see that the distance between {A} and {B} is {latex(x)}{latex('m')}, and the distance between {A} and {C} is {latex(y-x)}{latex('m')}.\n"
        slnstr += f"Since the distance between {A} and {C} {latex('<')} distance between {A} and {B}\n"
        #print("We can conclude that C is nearer to A than B.")
        slnstr += coptstr
        return slnstr
    elif(ans[0]=='BnCtA'):
        #print("The distance between {} and {} can be found out by subtracting the distance between {} and {} from the distance between {} and {}.\n".format(A,C,A,B,B,C))
        slnstr += f"Distance between {A} and {C} {latex('= ')}{latex(y)}{latex('-')}{latex(x)}{latex(' = ')}{latex(y-x)}{latex('m')}"
        slnstr += f"    ...([distance between {B} & {C}] {latex('-')} [distance between {A} & {B}])\n"
        slnstr += f"{B}---{latex(x)}{latex('m')}--->{A}---{latex(y-x)}{latex('m')}--->{C}\n"
        slnstr += f"As we can see that the distance between {A} and {C} is {latex(y-x)}{latex('m')}, and the distance between {B} and {C} is {latex(y)}{latex('m')}.\n"
        slnstr += f"Since the distance between {B} and {C} {latex('<')} distance between {A} and {C}\n"
        #print("We can conclude that B is nearer to C than A.")
        slnstr += coptstr
        return slnstr

def changequestion():
    global A,B,C,places,x,y,coptstr,ans,Aoptions
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
    ans = []
    coptstr = ''
    while(x>y):
        y = random.choice(distchoice)
    Aoptions = [f'{A} is at same distance from {B} and {C}',f'{B} is nearer to {A} than {C}',f'{C} is nearer to {A} than {B}',f'{B} is nearer to {C} than {A}']
    if(x == y-x):
        ans.append('AeBC')
        coptstr += f'{A} is at same distance from {B} and {C}'
        Aoptions.remove(coptstr)
    elif(x<y-x):
        ans.append('BnAtC')
        coptstr += f'{B} is nearer to {A} than {C}'
        Aoptions.remove(coptstr)
    elif(x>y-x):
        ans.append('CnAtB')
        coptstr += f'{C} is nearer to {A} than {B}'
        Aoptions.remove(coptstr)
    elif(y<y-x):
        ans.append('BnCtA')
        coptstr += f'{B} is nearer to {C} than {A}'
        Aoptions.remove(coptstr)

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

putInCsv('030102',10,main_function,'v7_4')