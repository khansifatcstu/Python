import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!','@','#','$','%','^','&','*','(',')']
print('Welcome to password generator:')
n_letter=int(input('How many letters you want in your password?\n'))
n_symbol=int(input('How many symbols you want in your password?\n'))
n_number=int(input('How many numbers you want in your password?\n'))
password=[]
for i in range(n_letter+1):
    char=random.choice(letters)
    password+=char
for i in range(n_symbol+1):
    sym=random.choice(symbols)
    password+=sym
for i in range(n_number+1):
    num=random.choice(numbers)
    password+=num
random.shuffle(password)
final_password=''
for i in password:
    final_password+=i
print(final_password)
