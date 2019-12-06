def switch(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b


def maxInThree(a, b, c):
    if a < b:
        if b < c:
            return c
        else:
            return b
    elif a < c:
        max = c
        return c
    else:
        return a

def maxInFive():
    max = None
    for i in range(5):
        tmp = int(input())
        if max is None or tmp > max:
            max = tmp

    return max


print(switch(1, 2))
print(maxInThree(1, 2, 3))
print(maxInFive())