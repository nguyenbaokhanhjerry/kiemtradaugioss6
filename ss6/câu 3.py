total_product = 0
container = 0

while True:
    quantity = int(input("Nhập số lượng của từng thùng: "))

    if quantity < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
    elif quantity == 0:
        print("Chương trình hiểu là đã kiểm đếm xong")
        break
    else:
        total_product += quantity
        container += 1

print("Tổng số thùng hàng hợp lệ đã đếm.:",  container)
print("Tổng số sản phẩm thu được.: ",total_product)

