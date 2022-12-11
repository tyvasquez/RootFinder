#
import matplotlib.pyplot as plt
import numpy as np


class RootFinder:

    def __init__(self,function,x1,x2,method):
        self.func = self.funcVal*np.exp(2) - 5
        self.x1 = x1
        self.x2 = x2
        self.method = method
        self.maxIter = 30
        self.root = 0
        self.funcVal = 0


    def pickMethod(self):
        if self.method == 'bisection':
            return self.bisection()
        elif self.method == 'newton':
            return self.newton()
        elif self.method == 'secant':
            return self.secant()
        else:
            raise ValueError('The method entered is invalid. Valid methods are "bisection", "newton", and "secant"')

    def bisection(self):
        self.a = self.x1
        self.b = self.x2
        if self.a > self.b:
            raise ValueError('A must be less than b')
        if self.a * self.b > 0:
            raise ValueError('A times B must be less than 0')
        self.funcVal = self.a
        if self.func >0:
            raise ValueError('The function value f(a) is larger than 0 ')
        self.funcVal = self.b
        if self.func <0:
            raise ValueError('The function value f(b) is smaller than 0 ')
        midpoint = (self.a +self.b)/2







    def newton(self):
        self.root = 6
        return self.root

    def secant(self):
        self.root = 7
        return self.root

    def __str__(self):
        return f'The root is {self.pickMethod()}'

    # de plot(self):
    #     #     x= np.arange(-1.5,1.5,.01)
    #     #     plt.figure()
    #     #     plt.plot(x, x*np.exp(2)-3, 'r-')
    #     #     plt.xlabel('x')
    #     #     plt.ylabel('y')
    #     #     plt.title('Figure 1', loc='center')
    #     #     plt.legend(['y =x^2 +1'])
    #     #     plt.grid()
    #     #     plt.text(0, 0, r'$y = x^2 +1')
    #     #     plt.show()


r1 = RootFinder(2,3,4,'bisection')
print(r1)