dai = int(input("Nhập chiều dài: "))
rong = int(input("Nhập chiều rộng: "))

def cv_dt(pheptinh,dai,rong):
    if pheptinh == "chuvi":
        return (dai + rong)*2
    else:
        return dai * rong  
print("Chu vi: ",cv_dt("chuvi",dai,rong))
print("Diện tích: ",cv_dt("dientich",dai,rong)) 


def ve_hinh(dai,rong):
    for i in range(rong):
        print("*" * dai)
print("Hình chữ nhật: ") 
ve_hinh(dai,rong)     
