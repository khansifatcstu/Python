size=input('Input the pizza size:')
bill=0
if size=='S' or size=='s':
    bill+=100
    print('Small pizza price is 100')
elif size=='M' or size=='m':
    bill+=200
    print('Medium pizza price is 200')
else:
    bill+=300
    print('Large pizza price is 300') 
pepperoni=input('Do you want pepperoni(Y/N)?')
if pepperoni=='Y' or pepperoni=='y':
    if size=='S' or 's':
       bill+=30
    else:
        bill+=50
extra_cheese=input('Do you want extra_cheese(Y/N)?')
if extra_cheese=='Y' or extra_cheese=='y':
    if size=='S' or 's':
       bill+=20
print(f'Your total bill is {bill}')
