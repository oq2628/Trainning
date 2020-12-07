# 2. cho trước 2 số y, x (y > x). Có 2 cách thay đổi giá trị của x:
# 	- tăng gấp đôi x
# 	- bớt x đi 1 đơn vị
# Tìm số bước nhỏ nhất để x = y.

x, y = eval(input("Nhập: "))
counter = 0
while x < y:
    if y % 2 != 0:
        y = y + 1
        y = y / 2
        counter += 2
        if y <= x:
            counter = counter + x - y
            break
    else:
        y = y / 2
        counter += 1
        if y <= x:
            counter = counter + x - y
            break
print("Số bước nhảy là: ", round(counter))
