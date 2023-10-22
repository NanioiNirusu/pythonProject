
# f(x, b) = (x^b + b) * (x^(b-1) + (b-1)) * (x^(b-2) + (b-2))....(x^0+0)

# man nav skaidrs isti kadam jaizskatas grafam

import matplotlib.pyplot as plt
def pow(x, pow):
    result = 1
    for i in range(pow):
        result *= x
    return result
def f(x, b):
    result = 1
    index = 0
    line = []
    while index <= b:
        each = pow(x, b-index) + (b-index)
        result *= each
        index += 1
        line.append(each)
    plt.plot(line)
    plt.show()
    return result

print(f(2, 3))