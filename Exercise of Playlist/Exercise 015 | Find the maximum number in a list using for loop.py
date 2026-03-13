number=input('enter all the number seperated by space:')
list=number.split()
count=0
for i in list:
    count=count+1
for j in range(count):
    list[j]=int(list[j])
maximum=0
for k in list:
    if k>maximum:
        maximum=k
print(f'Maximum number is:{maximum}')
