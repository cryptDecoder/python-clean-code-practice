def numberGenerator(n):
    if n < 20:
        number = 0
        while number < n:
            yield number
            number += 1
    else:
        return


print(list(numberGenerator(19)))
