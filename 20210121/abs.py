x = complex(input('x = '))

def my_abs(x):
    if x.imag == 0:
        return (x.real **2)**0.5
    else:
        return ((x.real **2) + (x.imag **2))**0.5

print(my_abs(x))