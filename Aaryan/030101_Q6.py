#. In a 'Tug of War' if no side wins it is an equation - True or False

import random

def main():
    
    eq=["In a Tug of War if no side wins","A weighing scale having its needle in center","Two persons sitting on either side of a See-Saw, having equal weights"]
    nteq=["A See-Saw having only one person sitting on a side","Two persons sitting on either side of a See-Saw, having unequal weights","In a Tug of War if a side wins","A weighing machine having 2 Kg  rice on one side and 1 Kg sugar on the other side"]
    #same time same speed same distance
    q1=random.choice([eq,nteq])
    cop=random.choice(q1)
    print(cop,", it is an equation.\n")

    o1="option 1 : True"
    o2="option 2 : False"

##    r=random.randint(0,5)
##    if r>3:
##        o1="option 1 : False"
##        o2="option 2 : True"

    print(o1)
    print(o2)
    print("")
    val=int(input("Enter the option number : "))
    if val==1 and cop in eq:
            print("Your answer is correct")
            print("------------ SOLUTION -------------")
            print("Since, we know that, an equation is defined as a statement consisting of two algebraic expressions having the same value.\nThus,",cop," will form an equation")
            return
    if val==2 and cop in nteq:
            print("Your answer is correct")
            print("------------ SOLUTION -------------")
            print("Since, we know that, an equation is defined as a statement consisting of two algebraic expressions having the same value.\nThus,",cop," will not form an equation")
            return
    elif val not in [1,2]:
            print("Invalid Choice")
    else:
            print("Your answer is incorrect")
            if cop in eq:
                print("------------ SOLUTION ------------- ")
                print("Since, we know that, an equation is defined as a statement consisting of two algebraic expressions having the same value.\nThus,",cop," will form an equation")
                return
            elif cop in nteq:
                print("------------ SOLUTION --------------- ")
                print("Since, we know that, an equation is defined as a statement consisting of two algebraic expressions having the same value.\nThus,",cop," will not form an equation")
                return
main()
