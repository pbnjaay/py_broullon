def eureka(i, j):
    som = 0
    result = []
    for x in range(i, j + 1):
        for z in range(1, len(str(x)) + 1):
            som += int(str(x)[z - 1]) ** z
        if som == x:
            result.append(x)
        som = 0
    return result


def unique_in_order(to_clean):
    result = [to_clean[0]]
    for x in to_clean:
        if x != result[len(result) - 1]:
            result.append(x)
    return result


def kha(nbr):
    i = 1
    while i <= nbr:
        print(i * ' ' + (nbr - i) * '*')
        i += 1


def kha2(nbr):
    i = nbr
    esp = 1
    while i >= 1:
        print(esp*' ' + i*'X')
        i -= 1
        esp += 1


kha2(6)
