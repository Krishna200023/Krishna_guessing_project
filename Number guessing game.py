import random
cnumber =random.randrange(1,101)
userinput = int(input('Enter your number:---'))
if userinput> cnumber:
    print('Computer number', cnumber)
    print('Your guess number is high')
elif cnumber>userinput:
    print('Computer number', cnumber)
    print('Your guess number is low')
else :
    print('Computer number', cnumber)
    print('Your guess number is equal')