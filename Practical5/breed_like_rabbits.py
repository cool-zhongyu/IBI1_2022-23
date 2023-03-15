#two rabits
# every generation doubles last generation
#if the number exceed 100
#it stops
#loops
x=1
y=2
while y in range(2,100):
    y=y*2
    x+=1
print("at generation", x,"over 100 rabbits have been born")
