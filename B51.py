def ktra_gtri():
     n = input("Nhập n: ")
     if n.replace('.','',1).replace('-','',1).isdigit():
         n = float(n)
         if -89 <= n <= 90:
             return n
         print("Không hợp lệ, nhập lại.")
         return ktra_gtri()

if __name__=="__main__":
    print(ktra_gtri())
     