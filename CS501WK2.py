def findMedian():
    list = []
    for i in range(3):
        tmp = int(input())
        list.append(tmp)
    list.sort()
    return list[1]

def printTriangle(n):
    number = 0
    for i in range(n):
        line = str(number)
        number += 1
        for j in range(i):
            line += " " + str(number)
            number += 1
        print(line)

print(findMedian())
print()
printTriangle(5)