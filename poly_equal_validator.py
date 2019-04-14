'''You are given a polynomial P of a single indeterminate (or variable), x. 
You are also given the values of x and y. Your task is to verify if P(x) = k.'''

x = input()
k = int(x.split()[1])
x = int(x[0])
poly = input()
if k == eval(poly):
    print("True")
else:
    print("False")