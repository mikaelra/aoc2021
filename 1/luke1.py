n = []
with open('input.txt') as my_file:
    for line in my_file:
        n.append(int(line))

asum = 0
for i in range(0,len(n)-3):
    first = n[i] + n[i+1] + n[i+2]
    second = n[i+1] + n[i+2] + n[i+3]
    if (first < second):
        asum+= 1

print("sum: " + str(asum))
print("first num: " + str(n[0]))
print("las num: " + str(n[-1])) 
