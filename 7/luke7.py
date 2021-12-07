# Imports

n = []
with open('input.txt') as my_file:
    for line in my_file:
        n.append(line)

valuesString = n[0].split(',')
inputValues = [int(x) for x in valuesString]

endSum = 10000000000000000000000
for i in range(len(inputValues)):
    startPoint = inputValues[i]
    tempSum = 0
    for j in range(len(inputValues)):
        tempSum += abs(startPoint-inputValues[j])
    if tempSum < endSum:
        endSum = tempSum

print(endSum)

#### Task 2 ####

def DistanceBetweenPoints(point1, point2):
    dist = abs(point1 - point2)
    temp = 0
    for i in range(dist):
        temp += i
    return temp


endSum = 10000000000000000000000
for i in range(len(inputValues)):
    startPoint = inputValues[i]
    tempSum = 0
    for j in range(len(inputValues)):
        tempSum += DistanceBetweenPoints(startPoint, inputValues[j])
    if tempSum < endSum:
        endSum = tempSum

print(endSum)