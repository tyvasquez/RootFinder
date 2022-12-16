import matplotlib.pyplot as plt
import numpy as np


class RootFinder:
    '''
    This class finds the root of a function using 3 differenth methods
    bisection, newton's and secant
    '''

    def __init__(self, x1, x2, method):
        '''
        Defines attributes and takes input
        :param x1:
        :param x2:
        :param method:
        '''

        self.x1 = x1
        self.x2 = x2
        self.method = method
        self.maxIter = 0
        self.root = 0
        self.funcVal = 0
        self.tolerance = 0.0001
        self.func = 0
        self.valListx = []
        self.valListy = []

    def f(self, funcVal):
        '''
        The function of which we are finding the root of
        :param funcVal:
        :return:
        '''
        self.func = pow(funcVal, 2) - 3 #x^2 -3
        return self.func

    def fPrime(self, funcVal):
        '''
        Derivative of our function
        :param funcVal:
        :return:
        '''

        self.funcP = (2*funcVal) #2x
        return self.funcP

    def pickMethod(self):
        '''
        Based on the user's input selects a method
        :return:
        '''
        if self.method == 'bisection':
            return self.bisection()
        elif self.method == 'newton':
            return self.newton()
        elif self.method == 'secant':
            return self.secant()
        else:
            raise ValueError('The method entered is invalid. Valid methods are "bisection", "newton", and "secant"')

    def bisection(self):
        '''
        Finds the root of the function using the bisection method
        :return:
        '''

        self.a = self.x1
        self.b = self.x2
        midpoint = 1

        if self.a > self.b: #checks if a less than b
            raise ValueError('A must be less than b')

        self.funcVal = self.a
        if self.f(self.funcVal) > 0: #checks if f(a) is greater than 0
            raise ValueError('The function value f(a) is larger than 0 ')

        self.funcVal = self.b
        if self.f(self.funcVal) < 0: # checks if f(b) is less than 0
            raise ValueError('The function value f(b) is smaller than 0 ')

        while midpoint != 0 or self.maxIter < 10: # runs until 10 iterations for midpoint is found

            midpoint = (self.a + self.b)/2
            self.funcVal = midpoint
            self.valListx.append(midpoint)  #stores x component of midpoint
            self.valListy.append(self.f(midpoint))  #stores y component of midpoint
            self.plot() #calls the plotting function which plots our point

            if self.f(self.funcVal) < 0:
                self.a = self.funcVal

            if self.f(self.funcVal) > 0:
                self.b = self.funcVal

            if self.a - self.b <= self.tolerance: #checks if our root is found by verifying if it is below tolerance
                self.root = self.funcVal
                midpoint = 0

            self.maxIter += 1 #counter
        return self.root

    def newton(self):
        '''
         Finds the root of the function using newton's method
        :return:
        '''

        self.a = 0
        self.b = self.x2
        count = 0

        if self.b <= 0: #checks b is greater than 0
            raise ValueError('b must be greater than 0')

        while count <= 10: # runs until 10 iterations or root is foujnd
            self.valListx.append(self.b)   #appends x coordinate
            self.valListy.append(self.f(self.b))  #appends y coordinate
            self.plot()  #calls plotting function

            self.a = self.b #sets x of n
            self.b = self.b - ((self.f(self.b)) / (self.fPrime(self.b))) #calculates x of n+1

            if (abs(self.a) - abs(self.b)) <= self.tolerance: # checks if root is found
                self.root = self.b
                count = 11
            else:
                self.root = self.b

                count += 1
        return self.root

    def secant(self):
        '''
         Finds the root of the function using the secant method
        :return:
        '''
        self.a = self.x1
        self.b = self.x2
        count = 0
        c = 0

        if self.a > self.b: #confirms a is less than b
            raise ValueError('A must be less than b')

        while count <= 10:  #runs 10 times or until root is found
            self.valListx.append(self.b) #appends x coord
            self.valListy.append(self.f(self.b))  #append y coord
            self.plot() #calls plotting function
            c = self.b #stores x of n
            self.b = (self.b) - (((self.a - self.b) / (self.f(self.a) - self.f(self.b))) * self.f(self.b)) #calculates x of n+1
            self.a = c  # sets x of n-1
            if (abs(self.a) - abs(self.b)) <= self.tolerance: #checks if root is found by seeing if value less than tolerance
                self.root = self.b
                count = 11
            else:
                self.root = self.b

                count += 1 #counter
        return self.root
    def plot(self):
        '''
        Plots each iteration of the root finding method
        :return:
        '''
        x = np.linspace(self.x1, self.x2, 400)
        plt.figure() # plots figure
        plt.plot(self.valListx, self.valListy, 's--m', x,pow(x, 2) - 3)  #plots points and equations
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Root Finder', loc='center')
        plt.legend(['Points', 'y =x^2 -3'])
        plt.grid()
        plt.text(0, 0, r'y = x^2 -3')
        plt.show()

    def __str__(self):
        '''
        Returns the value of our root
        :return:
        '''

        return f'The root is {self.pickMethod()}'

method = input(str('Please input desired method of root calculation for the function x^2 - 3 (bisection, newton, or secant).\nBisection will calculate the root of the function by finding a midpoint between the two given points then iteratively separating the interval between the points and subdividing the interval where the root is.\nThe method will then narrow the gap between the positive and negative intervals until it finds the correct answer.\nNewtons method works by using a single initial guess to approximate the geometry of a function through its tangent lines. It iterates through x coordinates until it finds the root of the function.\nSecant method works by using a succession of roots of secant lines to approximate the root of the function, similar to how Newtons method uses tangent lines.\nInput your choice here: '))

root1 = RootFinder(1, 2, method) #creates root object
print(root1)






