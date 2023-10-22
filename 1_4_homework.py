import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.sin(2*x) + 2*np.exp(3*x)
x = np.linspace(-np.pi, np.pi, 100)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of sin(2x) + 2e^(3x)')
plt.show()


print(f(2))