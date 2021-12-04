n = []
with open('input.txt') as my_file:
    for line in my_file:
        n.append(line)

# sumOfOnes = [0 for x in range(len(n[0])-1)]
# print(sumOfOnes)

# for i in range(len(n)):
#     for j in range(len(n[0])):
#         if n[i][j] == "1":
#             sumOfOnes[j] += 1

# sumOfOnes > 500 på hver er binære koden
oxyGenRating = 0
# Iterate through all 12, pick most for each
c02ScrubRating = 0
# Iterate through all 12, pick least for each
#### decimal = int(binary, 2) ####

sumOfOnes = 0
indexOfOnes = []
indexOfZero = []
templist = n

for i in range(12):
    for j in range(len(templist)):
        if n[j][i] == "1":
            sumOfOnes += 1
            indexOfOnes.append(j)
        else:
            indexOfZero.append(j)
    if sumOfOnes >= 500:
        templist = [templist[i] for i in indexOfOnes]
    else:
        templist = [templist[i] for i in indexOfZero]
    sumOfOnes = 0
    indexOfZero = []
    indexOfOnes = []
    print(len(templist))
    if len(templist) == 1:
        oxyGenRating = templist[0]
        break;

print(int(oxyGenRating, 2))

sumOfOnes = 0
indexOfOnes = []
indexOfZero = []
templist = n

for i in range(12):
    for j in range(len(templist)):
        if n[j][i] == "1":
            sumOfOnes += 1
            indexOfOnes.append(j)
        else:
            indexOfZero.append(j)
    if sumOfOnes < 500:
        templist = [templist[i] for i in indexOfOnes]
    else:
        templist = [templist[i] for i in indexOfZero]

    #if i > 8:
        #print("AAAAAAA" + str(i))
        #print(templist)
    sumOfOnes = 0
    indexOfZero = []
    indexOfOnes = []
    print(len(templist))
    if len(templist) == 1:
        c02ScrubRating = templist[0]
        break;
print(c02ScrubRating)

c02ScrubRatingdec = [int("100111110011", 2) * int(oxyGenRating, 2), int("101101001101", 2) * int(oxyGenRating, 2)]
print(c02ScrubRatingdec )
