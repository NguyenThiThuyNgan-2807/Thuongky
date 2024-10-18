# Bài 52
#a
def canbac(x,n):
    return x**(1/n)

#b
def sodao(n):
    # str: chuỗi, chữ số
    # return str(n)[::-1] (còn số 0)
    return int(str(n)[::-1])

#b_CÃ¡ch 3: tÃ­nh toÃ¡n
def dao(n):
    dao = 0
    while n>0:
        dao = dao*10+n%10
        n//=10
    return dao
    
#c
import math
def chinhphuong(n):
    return int(math.sqrt(n))**2 == n

#d
def ktra_ngto(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

#e
def tich_sole(n):
    tich = 1
    for i in range(1,n+1):
        if int(i)%2 != 0:
            tich *= int(i)
    return tich

#f
def tong_ngto(n):
    tong_ngto=0
    for i in range(2,n):
        if ktra_ngto(i):
            tong_ngto += i
    return tong_ngto
    
#g
def tong_chinhphuong(n):
    tong = 0
    for i in range(1,n):
        if chinhphuong(i):
            tong += i
    return tong

#h
def tong_uoc(n):
    tong = 0
    for i in range(1,n+1):
        if n%i == 0:
            tong += i
    return tong 


if __name__ == "__main__":
    # n = int(input("Nhap n: ")) (Nếu đề kêu nhập)
    print(canbac(8,3))
    print(sodao(123450))
    print(dao(123450))
    print(chinhphuong(1))
    print(ktra_ngto(2))
    print(tich_sole(15))
    print(tong_ngto(9))
    print(tong_chinhphuong(9))
    print(tong_uoc(9))
    