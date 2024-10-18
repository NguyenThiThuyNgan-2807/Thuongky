#a
def tong_a(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s

#b
def tong_b(n):
    s = 0 
    for i in range(1,n+1):
        s += i**2
    return s

#c
def tong_c(n):
    s = 0
    for i in range(1,n+1):
        s += 1/i
    return s
    
#d
def tong_d(n):
    s = 0
    giaithua = 1
    for i in range(1,n+1):
        giaithua += i
        s += giaithua
    return s

#e
def tong_e(n):
    giaithua = 1
    for i in range(1,n+1):
        giaithua *= i
    return giaithua

if __name__=="__main__":
    print(tong_a(4))
    print(tong_b(4))
    print(tong_c(4))
    print(tong_d(4))
    print(tong_e(4))