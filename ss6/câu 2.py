flag = True
for passwork in range(1,4):
    passwork = input("Nhập mật khẩu: ")
    if passwork == "123456":
        print("Đăng nhập thành công")
        flag = False
        break
    else:
        print("Mật khẩu sai, vui lòng nhập lại!")
if flag:
    print("Tài khoản đã bị khóa!")

