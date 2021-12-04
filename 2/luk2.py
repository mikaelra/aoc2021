n = []
with open('input.txt') as my_file:
    for line in my_file:
        n.append(line)

forwardn = 0
depth = 0

for i in range(len(n)):
    text = n[i].split(' ')[0]
    number = int(n[i].split(' ')[1])

    if text == "forward":
        forwardn += number
    elif text == "down":
        depth += number
    elif text == "up":
        depth -= number
    else:
        print("error")

print(depth*forwardn)

################################################


forwardn = 0
depth = 0
aim = 0

for i in range(len(n)):
    text = n[i].split(' ')[0]
    number = int(n[i].split(' ')[1])

    if text == "forward":
        forwardn += number
        depth = depth + (aim*number)
    elif text == "down":
        #depth += number
        aim += number
    elif text == "up":
        aim -= number
        #depth -= number
    else:
        print("error")

print(depth*forwardn)