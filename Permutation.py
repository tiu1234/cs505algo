result = []


def permutation(orig, tmp):
    if len(orig) == 0:
        result.append(tmp)
        return

    permutation(orig[1::], tmp.copy())
    tmp.append(orig[0])
    permutation(orig[1::], tmp.copy())

permutation(["a", "b", "c"], [])
print(result)

permutation(["a", "r", "b", "c"], [])
print(result)