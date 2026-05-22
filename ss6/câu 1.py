price = float(input("Nhập đơn giá của sản phẩm: "))
quantity = int(input("Nhập số lượng sản phẩm: "))

sum = price * quantity
if sum >= 1000000:
    discount = sum * 0.1
    print(f"Giảm giá: {discount}")
    total_price = sum - discount
else:
    print("Không giảm giá")
    total_price = sum
print("Tổng tiền phải trả: ",total_price)
