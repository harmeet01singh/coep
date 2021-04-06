import random as rd
from coep_package.latex import latex
from coep_package.csv import database_fn, putInCsv

def is_prime(num):
    f=0
    for i in range(2,num):
        if(num%i==0):
            f=1
            break

    if(f==1):
        return 0
    else:
        return 1      

def factors(num):
    list=[]
    for i in range(2,num+1):
        if(num%i==0):
            list.append(i)
    
    return list



def generate_expression():
    
    e0=rd.randint(40,250)
    while(is_prime(e0)):
        e0=rd.randint(40,250)
    
    # print(e0)

    #x is list of factors
    x=factors(e0)
    x.remove(e0)
    rd.shuffle(x)
    key=rd.randint(0,len(x)-1)
    # print('key',key)
    e1=x[key]

    return [e0,e1]    


def getName():
    names={'He':['Ramesh','Suresh','Dinesh','Abdul','Atharva','Lalit','John'],'She':['Geeta','Tina','Rekha','Ismat','Diya','Disha'],'eatable':['apples','mangoes','bananas','rasgullas','chocolates','pedhas']}
    p=rd.choice(['He','She'])
    name=rd.choice(names[p])
    e=rd.choice(names['eatable'])
    return [name,p,e]

def print_questions(exp=[]):
    name,p,e= getName()
    if(p=='He'):
         k ='his'
    else:
        k='her'
    
    key=rd.randint(0,1)
    global Question
    if(key):
        k=rd.choice(['splitted','distributed'])
        e='cookies'
        Question='\n\n{} baked {} cookies and {} them equally into {} packs. How many cookies did {} put in each packet?Let {} put $k$ cookies in each packet.Select the correct statements from below.<br>'.format(name,latex(exp[0]),k,latex(exp[1]),name,name)
        print(Question)
        #print('\nLet {} put k cookies in each packet.'.format(name))
    else:
        Question='\n\n{} had {} {}. {} distributes all {} evenly among {} friends.How many {} did {} gave to each of {} friends?Let each friend of {} gets $k$ {}.Select the correct statements from below.<br>'.format(name,latex(exp[0]),e,p,e,latex(exp[1]),e,name,k,name,e)
        print(Question)
        #print('\nLet each friend of {} gets k {}.'.format(name,e))

    return[name,k,e,key]
     

def print_options(ans=[]):
    
    options=[]
    
    global Correct_op,Wrong_op1,Wrong_op2,Wrong_op3

    options.append(latex('({}\\times k)\div {} = {}\div{} '.format(ans[1],ans[1],ans[0],ans[1])))
    Correct_op=options[0]
    options.append(latex('k+{} = {}+{} '.format(ans[1],ans[0],ans[1])))
    options.append(latex('{} \\times k = {} \\times {} '.format(ans[1],ans[0],ans[1])))
    options.append(latex('k-{} = {}-{} '.format(ans[1],ans[0],ans[1])))
    
    #print(Correct_op)
    Wrong_op1=options[1]
    Wrong_op2=options[2]
    Wrong_op3=options[3]
    #Now shuffling options
    rd.shuffle(options)

    print('''\nOptions:<br>
             \n1) {}<br>
             \n2) {}<br>
             \n3) {}<br>
             \n4) {}<br>'''.format(options[0],options[1],options[2],options[3]))
   
    i=0
    answer=options[0]
    t=latex('({}\\times k)\div {} = {}\div{} '.format(ans[1],ans[1],ans[0],ans[1]))
    while(answer!=t):
        i+=1
        answer=options[i]

    return (i+1)   


def take_input(cor_op):
    ans = None
    
    while(ans==None):
        ans = input('\n--------------------------------\nEnter your answer - \n')
        if(int(ans)>=5 or int(ans)<1 or ans.isalpha()):
            print('\nInvalid option...')
            ans=None
            continue
        else:
            ans = int(ans)
            break

    if(ans == cor_op):
        print('\n--------------------------------\nYour answer is right')
    else:
        print('\n--------------------------------\nYour answer is Wrong!!')


def question2(exp=[]):
    global Solution
    Solution='''\nTo answer these questions we need to use Dividing both the sides of equations by some non zero number.<br>
            \nLet each friend of {} gets $k$ {}.<br>
            \nNow, total {} {} had been distributed among {} friends and each one got $k$ number of {} .<br>
            \nThen according to given conditions we get this equation :-<br> ${}k = {}$<br>
            \n${}k\div{} = {}\div{}$ \t   (Dividing both sides by {})'''.format(exp[2],exp[4],exp[0],exp[4],exp[1],exp[4],exp[1],exp[0],exp[1],exp[1],exp[0],exp[1],exp[1])
    print(Solution)
    

    
    # print('\n∴ 1k = {} '.format(exp[0]/exp[1]))
    # print('\n∴ k = {} '.format(exp[0]/exp[1]))
    # print('\nTherefore, {} gave {} {} to each of his friends.'.format(exp[2],exp[0]/exp[1],exp[4]))


##print(rowdict)
def question1(exp=[]):
    global Solution
    Solution='''\nTo answer these questions we need to use Dividing both the sides of equations by some non zero number.<br>
            \nLet {} put $k$ cookies in each packet.<br>
            \nNow, total {} {} had been {} into {} packs and each packet got $k$ number of {}.<br>
            \nThen according to given conditions we get this equation :-<br> ${}k = {}$<br>
            \n${}k\div{} = {}\div{}$ \t   (Dividing both sides by {})'''.format(exp[2],exp[0],exp[4],exp[3],exp[1],exp[4],exp[1],exp[0],exp[1],exp[1],exp[0],exp[1],exp[1])
    print(Solution)


    # print('''\small( \dfrac{({}k)}{} = \dfrac{({})}{} ) '''.format(exp[1],exp[1],exp[0],exp[1]))
    # print('\n∴ 1k = {} '.format(exp[0]/exp[1]))
    # print('\n∴ k = {} '.format(exp[0]/exp[1]))
    # print('\nTherefore, {} putted {} {} in each packet.'.format(exp[2],exp[0]/exp[1],exp[4]))



def print_solution(exp=[]):
    #exp[1] contains no of friends
    #exp[0] contains total distributed
    #exp[2] contains name of person
    #exp[3] contains his/her
    #exp[4] contains object
    #exp[5] contains key of question number
    if(exp[5]):
        question1(exp)
    else:
        question2(exp)    
   
def main():
    e0,e1=generate_expression()
    name,p,e,key=print_questions([e0,e1])
    correct_option=print_options([e0,e1])
    #take_input(correct_option)
    print_solution([e0,e1,name,p,e,key])

    database_dict= database_fn(
        Answer_Type='1',
        Topic_Number='030202',
        Variation='v1',
        Question=Question,
        Correct_Answer_1=Correct_op,
        Wrong_Answer_1=Wrong_op1,
        Wrong_Answer_2=Wrong_op2,
        Wrong_Answer_3=Wrong_op3,
        ContributorMail='2019hanish.valecha@ves.ac.in',
        Solution_text=Solution
    )
    return database_dict
    
#if you want N questions in your csv file pass N as the value for Number of Iteraions
putInCsv(
    Topic_Number='030202',
    Number_Of_Iterations=10,
    Main_Function=main,
    Filename='v1_4'
)

main()