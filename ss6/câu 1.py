price = float(input("Nhập đơn giá của sản phẩm: "))
quantity = int(input("Nhập số lượng sản phẩm: "))

total_price = price * quantity
if total_price >= 1000000:
    discount = total_price * 0.1
    print(f"Giảm giá: {discount}")
else:
    print("Không giảm giá")

    