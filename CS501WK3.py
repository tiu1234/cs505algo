import time


def fibIterative(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    v1 = 0
    v2 = 1
    for i in range(3, n):
        tmp = v1 + v2
        v1 = v2
        v2 = tmp
    return v1 + v2


def fibRecusive(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1

    return fibRecusive(n-1) + fibRecusive(n-2)


start = time.time()
print(fibIterative(20))
end = time.time()

print(end - start)

start = time.time()
print(fibRecusive(20))
end = time.time()

print(end - start)
