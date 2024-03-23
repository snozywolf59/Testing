# Loại khách: V
# Giá tiền: P
import sys


def thanhToan(v, p):
    if p <= 0:
        print("Hoa don khong hop le!")
        return
    if p > 5000:
        print("Hoa don khong hop le!")
        return
    if not v:
        if p < 100:
            print("Khong uu dai")
            return
        if p < 1000:
            print("Giam 5%")
            return
        print("Giam 5%, tang voucher")
        return
    if p < 100:
        print("Tang voucher")
        return
    if p < 1000:
        print("Giam 5%, tang voucher")
        return
    print("Giam 10%, tang voucher")
    pass


V = False
P = 1000
print(sys.maxsize)
thanhToan(V, P)
