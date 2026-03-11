import random
name=input('Enter the names separated by comma:')
names_list=name.split(",")
print(names_list)
a=random.choice(names_list)
print(f'{a} will pay the bill')
