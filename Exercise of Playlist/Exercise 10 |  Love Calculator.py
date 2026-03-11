name1 = input('What is your name?')
name2 = input('What is his/her name?')
combined_name = name1+name2
lower = combined_name.lower()

t = lower.count('t')
r = lower.count('r')
u = lower.count('u')
e = lower.count('e')
true = t+r+u+e
l = lower.count('l')
o = lower.count('o')
v = lower.count('v')
e = lower.count('e')
love = l+o+v+e
love_score = int(str(true)+str(love))
if love_score<10 or love_score>90:
    print(f'Your love score is {love_score} and you go together coke and mentos')
elif love_score>=40 and love_score<=50:
    print(f'Your love score is {love_score} and you are alright together')
else:
    print (f'Your love score is {love_score}')
