import matplotlib.pyplot as plt
import numpy as np


class RootFinder:

    def __init__(self, x1, x2, method):

        self.x1 = x1
        self.x2 = x2
        self.method = method
        self.maxIter = 0
        self.root = 0
        self.funcVal = 0
        self.tolerance = 0.000001
        self.func = 0
        self.valListx = []
        self.valListy = []

    def f(self, funcVal):
        self.func = pow(funcVal, 3) - (5 * funcVal) + 1
        return self.func

    def fPrime(self, funcVal):
        self.funcP = (3 * pow(funcVal, 2) - 5)
        return self.funcP

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
        midpoint = 1

        if self.a > self.b:
            raise ValueError('A must be less than b')

        self.funcVal = self.a
        if self.f(self.funcVal) > 0:
            raise ValueError('The function value f(a) is larger than 0 ')

        self.funcVal = self.b
        if self.f(self.funcVal) < 0:
            raise ValueError('The function value f(b) is smaller than 0 ')

        while midpoint != 0 or self.maxIter < 30:

            midpoint = (self.a + self.b) / 2
            self.funcVal = midpoint

            if self.f(self.funcVal) == 0:
                self.root = self.funcVal
                midpoint = 0

            else:

                if self.f(self.funcVal) < 0:
                    self.a = self.funcVal

                if self.f(self.funcVal) > 0:
                    self.b = self.funcVal

            if self.a - self.b <= self.tolerance:
                self.root = self.funcVal
                midpoint = 0

            self.maxIter += 1
        return self.root

    def newton(self):
        self.a = 0
        self.b = self.x1
        count = 0

        if self.b <= 0:
            raise ValueError('A must be greater than 0')

        while count <= 30:
            self.a = self.b
            self.b = self.b - ((self.f(self.b)) / (self.fPrime(self.b)))

            if (abs(self.a) - abs(self.b)) <= self.tolerance:
                self.root = self.f(self.b)
                count = 31
            else:
                self.root = self.f(self.b)
                self.valListx.append(self.b)
                self.valListy.append(self.f(self.b))
                self.plot()
                count += 1
        return self.root

    def secant(self):
        self.a = self.x1
        self.b = self.x2
        count = 0
        c = 0

        if self.a > self.b:
            raise ValueError('A must be less than b')

        while count <= 30:
            c = self.b
            self.b = (self.b) - (((self.a - self.b) / (self.f(self.a) - self.f(self.b))) * self.f(self.b))
            self.a = c
            if (abs(self.a) - abs(self.b)) <= self.tolerance:
                self.root = self.f(self.b)
                count = 31
            else:
                self.root = self.f(self.b)
                self.valListx.append(self.b)
                self.valListy.append(self.f(self.b))
                self.plot()
                count += 1
        return self.root

    def __str__(self):
        return f'The root is {self.pickMethod()}'

    def plot(self):
        x = np.linspace(self.x1, self.x2, 400)
        plt.figure()
        plt.plot(self.valListx, self.valListy, 's--m', x, pow(x, 2) - 3)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Root Finder', loc='center')
        plt.legend(['Points', 'y =x^2 -3'])
        plt.grid()
        plt.text(0, 0, r'$y = x^2 -3')
        plt.show()


r1 = RootFinder(1, 0, 'newton')
print(r1)






