def square_Root(num, estim, eps):
    step = eps ** 2
    numGuesses = 0

    while abs(estim ** 2 - num) >= eps and estim <= num:
        if estim ** 2 >= num:
            estim -= step
        else:
            estim += step
        numGuesses += 1

    if abs(estim ** 2 - num) >= eps:
        return f'numGuesses is {numGuesses}, and Fail on square root of {num}'
    else:
        return f'numGuesses is {numGuesses}, and {estim:.4f} is the square root of {num}'

print(square_Root(27, 5.0, 0.001))
print(square_Root(27, 6.0, 0.001))
