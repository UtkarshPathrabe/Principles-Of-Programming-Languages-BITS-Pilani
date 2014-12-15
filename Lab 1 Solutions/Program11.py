def add(m, n):
    a = m.real + n.real
    b = m.imag + n.imag
    return(complex(a,b))

def subtract(m, n):
    a = m.real - n.real
    b = m.imag - n.imag
    return(complex(a,b))

def multiply(m, n):
    a = m.real*n.real - m.imag*n.imag
    b = m.real*n.imag + n.real*m.imag
    return(complex(a,b))

def conjugate(m):
    return(complex(m.real, -m.imag))

def divide(m, n):
    o = conjugate(n)
    p = multiply(n, o)
    q = multiply(m, o)
    return(complex(q.real/p, q.imag/p))
