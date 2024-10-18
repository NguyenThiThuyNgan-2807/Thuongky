def ktra_so(n):
    if n<0 and n%2 != 0:
        return -1
    elif n>0 and n%2 == 0:
        return 1
    else:
        return 0

if __name__=="__main__":
    print(ktra_so(4))