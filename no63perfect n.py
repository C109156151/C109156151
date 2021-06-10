data1=0
data2=int(input("請輸入正整數n："))
for i in range(1,data2):
    if data2 % i == 0:
        data1 += i
if data1 == data2:
    print("Perfect")
else:
    print("deficient")