height=input('enter all the heght seperated by space:')
list=height.split()
count=0
for i in list:
    count=count+1
for j in range(count):
    list[j]=int(list[j])
total=0
for k in list:
    total+=k
avg=total/count
print('Average height is:',round(avg))
