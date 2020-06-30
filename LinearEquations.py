# File: LinearEquations.py
# Description: HW11: Linear Equations
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 10/29/19
# Date Last Modified: 10/31/19

################################################################################

class LinearEquation():

    # initializer with slope (m) and y-intercept(b)
    def __init__(self,m,b):
        self.m = m
        self.b = b

    # shows linear equation as a string
    def showEq(self):
        # if slope is 0, check all possible cases for y-int
        if (self.m==0):
            if (self.b>0):
                return str(self.b)
            elif (self.b==0):
                return ""
            else:
                return "- " + str(abs(self.b))
        # if slope is positive, check all possible cases for y-int
        if (self.m>0):
            if (self.b>0):
                return str(self.m) + "x" + " + " + str(self.b)
            elif (self.b==0):
                return str(self.m) + "x"
            else:
                return str(self.m) + "x" + " - " + str(abs(self.b))
        # slope is negative, check all possible cases for y-int
        else:
            if (self.b>0):
                return "- " + str(abs(self.m)) + "x" + " + " + str(self.b)
            elif (self.b==0):
                return "- " + str(abs(self.m)) + "x"
            else:
                return "- " + str(abs(self.m)) + "x" + " - " + str(abs(self.b))

    # adds two linear equations together
    def add(self,other):
        newM = self.m + other.m
        newB = self.b + other.b 
        return LinearEquation(newM,newB)

    # subtracts one linear equation from another
    def sub(self,other):
        newM = self.m - other.m
        newB = self.b - other.b
        return LinearEquation(newM,newB)

    # composition of two linear equations
    def compose(self,other):
        newM = self.m * other.m
        newB = self.m * other.b + self.b
        return LinearEquation(newM,newB)

    # evaluates a value in the linear equation
    def evaluate(self,value):
        return self.m * value + self.b

# main program was provided  
def main():

   f = LinearEquation(5,3)
   print("f(x) =",f.showEq())
   print("f(3) =",f.evaluate(3),"\n")
         
   g = LinearEquation(-2,-6)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")

   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")

   k = f.compose(g)
   print("f(g(x)) =",k.showEq(),"\n")
   
   m = g.compose(f)
   print("g(f(x)) =",m.showEq(),"\n")

   g = LinearEquation(5,-3)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")
   
   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")
   
main()
        
