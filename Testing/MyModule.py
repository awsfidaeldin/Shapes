def fact(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact

def power(x,y):
    p=1
    for i in range(1,y+1):
        p=p*x
    return p