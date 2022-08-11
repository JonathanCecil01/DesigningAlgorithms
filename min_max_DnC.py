import sys

def find_min(x):
    n = len(x)
    if len(x)==2:
        print(x)
        return min(x)
    elif len(x)==1:
        print(x)
        return x[0]
    else:
        print(x)
        return(min(find_min(x[:int(n/2)]),
        find_min(x[int(n/2):])))
        
def find_max(x):
    n = len(x)
    if len(x)==2:
        print(x)
        return max(x)
    elif len(x)==1:
        print(x)
        return x[0]
    else:
        print(x)
        return(max(find_max(x[:int(n/2)]),
        find_max(x[int(n/2):]))) 
elements = [2, 678,5, 23,32, 21, 234, 33, 9]
n = len(elements)
print(find_max(elements))
