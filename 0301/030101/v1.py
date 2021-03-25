import random

def sol():
    print("\n--------------------------------------SOLUTION-------------------------------------------")
    print(f"Since we don't know the exact number of {item} in the {container}. Let us represent the number of {item} as variable '{variable}'".format(item=item, container=container, variable=variable))

container = random.choice([ 'container', 'box', 'jar', 'pouch', 'drawer'])
item = random.choice([ 'pencils', 'erasers', 'staplers', 'sharperners', 'rulers', 'pens', 'brushes', 'crayons'])
variable = random.choice('abckmnxyz')

print(f"In a {container} there are few {item}. How many {item} are there?")
options = [ random.randint(0,10), variable, random.randint(0,10), random.randint(0,10) ]
random.shuffle(options)

for i in range(1,5):
    print( str(i) + ". " + str(options[i-1]))
selected = int(input("Select your option: "))
if options[selected-1] == variable:
    print("\nYou have selected the right option")
    sol()
else:
    print("\nYou have selected the wrong option")
    sol()