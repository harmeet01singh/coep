# Virtual MathLab COEP-VESIT
## 1. Package installation
```
cd Package
python setup.py install
```

## 2. How Branching Works
##### 1. Create your Github account [here](https://github.com/)
##### 2. Install git into your computer by using this  [tutorial](https://youtu.be/2j7fD92g-gE)
- Note 
 1. follow everything which is given in the above mentioned tutorial 
 2. instead of git bash you can also use your command prompt.

##### 3. Create new folder named ‘vmathlab’ and navigate into it using cmd ‘cd’

##### 4. Run this 3 commands

```
git init
git remote add origin https://github.com/harmeetsingh01/coep.git
git pull origin YOUR GROUP BRANCH
```
Note each group will work on different branch
| Group leader | Branch name |
| :---: | :---: |
| Rohan’s group | rp-se |
| Harmeet’s group | hs-se |
| Mohit’s group | mk-se |
| Shubhra’s group | sj-se |
| Hemkesh’s group | hr-se |
| Aryan’s group | ar-se |

I.e. for Rohan’s group members command will look like this
```
git pull origin rp-se
```

##### 5. To shift in your respective branch run command 
```
git checkout YOUR GROUP BRANCH
```

##### 6. When you will be done with your algorithms and your respective senior has allowed you to update code on git, Use this commands - 
```
git add .
git commit -m “THE CHANGES WHICH ARE DONE”
git pull origin YOUR GROUP BRANCH
git push origin YOUR GROUP BRANCH
```

## 3. Algorithms Mapping
| Module Code | Question No. | Variation No. | Author name | Author VES Id |
| :---: | :---: | :---: | :---: | :---: |
| 030101 | 1 | 1 | Harmeet Singh | 2018.harmeet.kathoda@ves.ac.in |
