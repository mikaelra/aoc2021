# Imports

n = []
with open('input.txt') as my_file:
    for line in my_file:
        n.append(line)

valuesString = n[0].split(',')
inputValues = [int(x) for x in valuesString]

calculatedInput = inputValues
for i in range(80):
    print(i)
    currInput = calculatedInput

    for i in range(len(currInput)):
        currInput[i] = currInput[i]-1
    
    for i in range(len(currInput)):
        if currInput[i] == -1:
            currInput[i] = 6
            currInput.append(8)
    
    calculatedInput = currInput

print(len(calculatedInput))

# Needs optimizing for 256