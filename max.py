import random
list=[]

list.append(random.randint(0,4))
while len(list) < 5:
    for i in range(5):
        r=random.randint(1,5)
        if r not in list:
            list.append(r)
print(list)
